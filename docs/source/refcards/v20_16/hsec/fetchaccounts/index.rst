==================
hsec.fetchaccounts
==================


Operation: GET /dataservice/hsec/fetchaccounts
----------------------------------------------


Authenticate User and Sync Licenses

.. code:: python

    def get(
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
        client.hsec.fetchaccounts.get()


Operation: POST /dataservice/hsec/fetchaccounts
-----------------------------------------------


Authenticate User and Sync Licenses

.. code:: python

    def post(
        payload: FetchAccounts1PostRequest,
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
        client.hsec.fetchaccounts.post()


.. toctree::
    :maxdepth: 1

    models

