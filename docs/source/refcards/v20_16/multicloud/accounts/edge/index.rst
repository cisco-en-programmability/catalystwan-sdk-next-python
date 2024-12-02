========================
multicloud.accounts.edge
========================


Operation: GET /dataservice/multicloud/accounts/edge
----------------------------------------------------


Deprecated!!!

Get all Multicloud edge accounts

.. code:: python

    def get_edge_accounts(
        edge_type: Optional[EdgeTypeParam] = None,
    ) -> Any: ...


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
        client.multicloud.accounts.edge.get_edge_accounts()


Operation: POST /dataservice/multicloud/accounts/edge
-----------------------------------------------------


Deprecated!!!

Authenticate edge account credentials

.. code:: python

    def validate_edge_account_add(
        payload: Optional[Any] = None,
    ) -> None: ...


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
        client.multicloud.accounts.edge.validate_edge_account_add()


Operation: GET /dataservice/multicloud/accounts/edge/{accountId}
----------------------------------------------------------------


Deprecated!!!

Get edge account by account Id

.. code:: python

    def get_edge_account_details(account_id: str) -> Any: ...


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
        client.multicloud.accounts.edge.get_edge_account_details()


Operation: PUT /dataservice/multicloud/accounts/edge/{accountId}
----------------------------------------------------------------


Deprecated!!!

Update Multicloud edge account

.. code:: python

    def update_edge_account(
        account_id: str, payload: Optional[Any] = None
    ) -> None: ...


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
        client.multicloud.accounts.edge.update_edge_account()


Operation: DELETE /dataservice/multicloud/accounts/edge/{accountId}
-------------------------------------------------------------------


Deprecated!!!

Delete edge account

.. code:: python

    def delete_edge_account(account_id: str) -> None: ...


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
        client.multicloud.accounts.edge.delete_edge_account()


.. toctree::
    :maxdepth: 1

    credentials
    models

