import logging

from flask_appbuilder.basemanager import BaseManager
from flask_appbuilder.models.sqla.interface import SQLAInterface

log = logging.getLogger(__name__)


class SecurityAPIAddOnManager(BaseManager):

    def __init__(self, appbuilder):
        """
             Use the constructor to setup any config keys specific for your app. 
        """
        super(SecurityAPIAddOnManager, self).__init__(appbuilder)
        # also config FAB_API_MAX_PAGE_SIZE !
        self.appbuilder.get_app.config.setdefault('FAB_ADDON_SECURITYAPI_PAGE_SIZE', 1000)

    def register_views(self):
        """
            This method is called by AppBuilder when initializing, use it to add you views
        """
        from fab_addon_SecurityAPI.api import UserModelApi, RoleModelApi, PermissionViewModelApi
        UserModelApi.datamodel = SQLAInterface(self.appbuilder.sm.user_model)
        self.appbuilder.add_api(UserModelApi)
        RoleModelApi.datamodel = SQLAInterface(self.appbuilder.sm.role_model)
        self.appbuilder.add_api(RoleModelApi)
        PermissionViewModelApi.datamodel = SQLAInterface(self.appbuilder.sm.permissionview_model)
        self.appbuilder.add_api(PermissionViewModelApi)

        # self.appbuilder.add_permissions(update_perms=True)
        pass

    def pre_process(self):
        pass

    def post_process(self):
        pass

