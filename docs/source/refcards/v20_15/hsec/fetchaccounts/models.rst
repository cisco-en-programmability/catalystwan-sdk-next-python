======
Models
======


.. code:: python

    from typing import List, Any, Optional, Literal, Dict, Union

    ValueType = Literal[
        "ARRAY", "FALSE", "NULL", "NUMBER", "OBJECT", "STRING", "TRUE"
    ]


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


    class FetchAccounts1PostRequest:
        empty: Optional[bool]
        value_type: Optional[ValueType]


