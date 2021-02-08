**Flask-appbuilder addon SecurityAPI**
------------------------------------------------------

Addon creates API for User and Roles in flask-appbuilder.
Detailed info avaliable in flask-appbuilder Swagger view (/swagger/v1).

- Install it::

    - for local develop:
        pip install -e <local path to source>

    - for use from git (via tarballs):
        pip install https://github.com/lexisstv/fab_addon_SecurityAPI/archive/master.zip

- Config parameters:
    - FAB_ADDON_SECURITYAPI_PAGE_SIZE - page size on API results (don't forget also configure FAB_API_MAX_PAGE_SIZE) - defalt value 1000.

Added 3 API:
- UserModelApi - user management (not all fields open, build-in 'admin' user filtered).
- RoleModelApi - roles management (not all fields open,  build-in 'admin' role filtered).
- PermissionViewModelApi - readonly information about permissions-views. Added :
    - /permissionview/cleanup - analogue for command `flask fab security-cleanup`, see more https://flask-appbuilder.readthedocs.io/en/latest/cli.html
    - /permissionview/update - analogue for command `flask fab create-permissions`

API based on ModelRestApi https://flask-appbuilder.readthedocs.io/en/latest/rest_api.html#model-rest-api


