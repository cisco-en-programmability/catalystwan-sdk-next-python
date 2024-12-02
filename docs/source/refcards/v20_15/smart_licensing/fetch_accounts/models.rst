======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class SmartLicensingfetchAccountsRespVirtualAccounts:
        default: Optional[bool]
        name: Optional[str]
        virtual_account_id: Optional[str]


    class SmartLicensingfetchAccountsResp:
        account_id: Optional[str]
        name: Optional[str]
        virtual_accounts: Optional[
            List[SmartLicensingfetchAccountsRespVirtualAccounts]
        ]


