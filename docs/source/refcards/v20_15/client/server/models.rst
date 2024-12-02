======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class ClientServerResponseData:
        capabilities: Optional[List[str]]
        cloudx: Optional[str]
        csrf_token: Optional[str]
        description: Optional[str]
        disable_full_config_push: Optional[bool]
        enable_server_events: Optional[bool]
        external_user: Optional[bool]
        general_template: Optional[bool]
        is_rbac_vpn_user: Optional[bool]
        is_saml_user: Optional[bool]
        is_ui_allowed: Optional[bool]
        locale: Optional[str]
        platform_version: Optional[str]
        reverseproxy: Optional[str]
        roles: Optional[List[str]]
        server: Optional[str]
        tenancy_mode: Optional[str]
        tenant_id: Optional[str]
        user: Optional[str]
        user_mode: Optional[str]
        view_mode: Optional[str]
        vmanage_mode: Optional[str]
        vpns: Optional[List[str]]
        vsession_id: Optional[str]


    class ClientServerResponseHeader:
        generated_on: Optional[int]


    class ClientServerInfoResponse:
        data: Optional[ClientServerResponseData]
        header: Optional[ClientServerResponseHeader]


