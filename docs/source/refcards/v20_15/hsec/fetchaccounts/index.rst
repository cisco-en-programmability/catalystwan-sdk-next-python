==================
hsec.fetchaccounts
==================


Operation: GET /dataservice/hsec/fetchaccounts
----------------------------------------------


Authenticate User and Sync Licenses

.. code:: python

    def fetch_sava_accounts(
        username: Optional[str] = None,
        pwd: Optional[str] = None,
        mode: Optional[str] = None,
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
        client.hsec.fetchaccounts.fetch_sava_accounts()


Operation: POST /dataservice/hsec/fetchaccounts
-----------------------------------------------


Authenticate User and Sync Licenses

.. code:: python

    def fetch_accounts_1(
        payload: Optional[FetchAccounts1PostRequest] = None,
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
        client.hsec.fetchaccounts.fetch_accounts_1()


.. toctree::
    :maxdepth: 1

    models

