===================
multicloud.accounts
===================


Operation: POST /dataservice/multicloud/accounts
------------------------------------------------


Add Cloud Account

.. code:: python

    def post(payload: PostAccounts) -> PostAccountsResponse: ...


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
        client.multicloud.accounts.post()


Operation: PUT /dataservice/multicloud/accounts/{accountId}
-----------------------------------------------------------


Obtain all accounts for all clouds

.. code:: python

    def put(account_id: str, payload: PutAccounts) -> None: ...


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
        client.multicloud.accounts.put()


Operation: DELETE /dataservice/multicloud/accounts/{accountId}
--------------------------------------------------------------


Obtain all accounts for all clouds

.. code:: python

    def delete(account_id: str) -> None: ...


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
        client.multicloud.accounts.delete()


Operation: GET /dataservice/multicloud/accounts
-----------------------------------------------


.. code:: python

    @overload
    def get(
        cloud_type: Optional[str] = None,
        cloud_gateway_enabled: Optional[str] = None,
    ) -> List[GetAccounts]: ...


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
        client.multicloud.accounts.get()


Operation: GET /dataservice/multicloud/accounts/{accountId}
-----------------------------------------------------------


.. code:: python

    @overload
    def get(account_id: str) -> GetAccounts: ...


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
        client.multicloud.accounts.get()


.. toctree::
    :maxdepth: 1

    edge/index
    credentials/index
    models

