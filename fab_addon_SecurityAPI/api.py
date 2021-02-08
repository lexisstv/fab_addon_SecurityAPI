from flask import current_app
from flask_appbuilder.api import expose, ModelRestApi
from flask_appbuilder.models.sqla.filters import FilterNotEqual
from flask_appbuilder.security.decorators import protect

"""
    Create your Views (but don't register them here, do it on the manager::


    class MyModelView(ModelView):
        datamodel = SQLAInterface(MyModel)

    
"""


class UserModelApi(ModelRestApi):
    resource_name = 'user'
    # datamodel = SQLAInterface(current_app.appbuilder.sm.user_model)
    base_filters = [['username', FilterNotEqual, 'admin']]
    page_size = current_app.config["FAB_ADDON_SECURITYAPI_PAGE_SIZE"]

    available_cols_list = \
        [
            'username',
            # 'password',
            'first_name',
            'last_name',
            'email',
            'active'
        ]

    add_columns = available_cols_list + ['roles']
    list_columns = available_cols_list + ['roles.id']
    edit_columns = available_cols_list + ['roles']
    show_columns = available_cols_list + ['roles']

    add_query_rel_fields = {
        'roles': [['name', FilterNotEqual, current_app.config["AUTH_ROLE_ADMIN"]]]
    }


class RoleModelApi(ModelRestApi):
    resource_name = 'role'
    page_size = current_app.config["FAB_ADDON_SECURITYAPI_PAGE_SIZE"]
    # datamodel = SQLAInterface(current_app.appbuilder.sm.role_model)
    base_filters = [['name', FilterNotEqual, current_app.config["AUTH_ROLE_ADMIN"]]]
    add_columns = ['name', 'permissions']
    list_columns = ['name', 'permissions.id']
    edit_columns = ['name', 'permissions']
    show_columns = ['name', 'permissions']


class PermissionViewModelApi(ModelRestApi):
    # allow_browser_login = True
    resource_name = 'permissionview'
    page_size = current_app.config["FAB_ADDON_SECURITYAPI_PAGE_SIZE"]
    # datamodel = SQLAInterface(current_app.appbuilder.sm.permission_model)
    # base_permissions = ['can_get', 'can_info']
    exclude_route_methods = ("put", "post", "delete")
    list_columns = ['id', 'permission.id', 'permission.name', 'view_menu.id', 'view_menu.name']
    show_columns = ['id', 'permission.id', 'permission.name', 'view_menu.id', 'view_menu.name']

    def pre_get_list(self, data):
        pass

    @expose('/update')
    @protect()
    def update_perms(self):
        """
             Creates all permissions and add them to the ADMIN Role.
        ---
        post:
          description: >-
             Creates all permissions and add them to the ADMIN Role.
          responses:
            200:
              description: Refresh Successful
              content:
                application/json:
            401:
              $ref: '#/components/responses/401'
            500:
              $ref: '#/components/responses/500'
          security:
            - jwt_refresh: []
        """
        current_app.appbuilder.add_permissions(update_perms = True)
        return self.response(200, message = "Ok")

    @expose('/cleanup')
    @protect()
    def greeting(self):
        """
             Cleanup unused permissions from views and roles.
        ---
        post:
          description: >-
             Cleanup unused permissions from views and roles.
          responses:
            200:
              description: Refresh Successful
              content:
                application/json:
            401:
              $ref: '#/components/responses/401'
            500:
              $ref: '#/components/responses/500'
          security:
            - jwt_refresh: []
        """
        current_app.appbuilder.security_cleanup()
        return self.response(200, message = "Ok")
