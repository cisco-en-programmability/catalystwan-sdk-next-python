==============================
smart_licensing.fetch_accounts
==============================


Operation: GET /dataservice/smartLicensing/fetchAccounts
--------------------------------------------------------


fetch sava for sle

.. code:: python

    def fetch_accounts(
        mode: str, payload: Optional[Any] = None
    ) -> SmartLicensingfetchAccountsResp: ...


Example:
^^^^^^^^


.. code:: python

    from catalyswan.core import create_client

    url = "example.com"
    username = "admin"
    password = "password123"

    with create_client(
        url=url, username=username, password=password
    ) as client:
        client.smart_licensing.fetch_accounts.fetch_accounts()


.. toctree::
    :maxdepth: 1

    models

