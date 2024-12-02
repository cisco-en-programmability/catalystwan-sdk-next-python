======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class AccountData:
        # Access Point Name
        apn: str
        # Authentication method.
        auth_method: str
        # Name of the communication plan associated with default provider.
        comm_plan: str
        # Data packet protocol version
        pdn_type: str
        # Name of the rate plan associated with default provider.
        rate_plan: str
        # Password of the user.
        password: Optional[str]
        # User name.
        user: Optional[str]


    class ProviderAccountDetails:
        #  ID  of the account associated with user using provider service.
        account_id: str
        # Name of the user registered to  the service.
        account_user_name: str
        # API key for the provider service.
        api_key: str
        # Name of the service provider.
        carrier_name: str
        # Boolean value which indicates whether the provider is the default provider .
        is_default: bool
        # Boolean value which indicates if the account user accepts account provider's terms and conditions if they exist.
        accept_terms_and_conditions: Optional[bool]
        account_data: Optional[AccountData]


