======
Models
======


.. code:: python

    from typing import List, Any, Optional, Literal, Dict, Union

    Mode = Literal["SDWANaaS", "default"]

    Env = Literal["PRODUCTION", "PROD_STAGING", "STAGING"]


    class InitBlobVmanageInitBlobInternalCredentials:
        password: str
        # Url to reset credentials
        reset_url: str
        user_name: str


    class InitBlobVmanageInitBlobJwtCredentials:
        # client id
        client_id: str
        # client secret
        client_secret: str
        # Url to reset credentials
        reset_url: str
        # Url to fetch token
        token_url: str


    class InitBlobVmanageInitBlobPnp:
        # client id
        client_id: str
        # client secret
        client_secret: str
        # Url to reset credentials
        reset_url: str
        # PnP environment
        env: Optional[Env]


    class InitBlobVmanageInitBlob:
        internal_credentials: InitBlobVmanageInitBlobInternalCredentials
        jwt_credentials: InitBlobVmanageInitBlobJwtCredentials
        # vManage Mode
        mode: Mode  # pytype: disable=annotation-type-mismatch
        pnp: InitBlobVmanageInitBlobPnp
        # SDWAN Portal Url
        sdwan_portal_url: Optional[str]
        # Webhook Url to send notifications
        webhook_url: Optional[str]


    class InitBlob:
        vmanage_init_blob: Optional[InitBlobVmanageInitBlob]


