========================
multicloud.accounts.edge
========================


Operation: POST /dataservice/multicloud/accounts/edge
-----------------------------------------------------


Deprecated!!!

Authenticate edge account credentials

.. code:: python

    def post(payload: Any) -> None: ...


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
        client.multicloud.accounts.edge.post()


Operation: PUT /dataservice/multicloud/accounts/edge/{accountId}
----------------------------------------------------------------


Deprecated!!!

Update Multicloud edge account

.. code:: python

    def put(account_id: str, payload: Any) -> None: ...


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
        client.multicloud.accounts.edge.put()


Operation: DELETE /dataservice/multicloud/accounts/edge/{accountId}
-------------------------------------------------------------------


Deprecated!!!

Delete edge account

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
        client.multicloud.accounts.edge.delete()


Operation: GET /dataservice/multicloud/accounts/edge
----------------------------------------------------


Deprecated!!!

.. code:: python

    @overload
    def get(edge_type: Optional[EdgeTypeParam] = None) -> Any: ...


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
        client.multicloud.accounts.edge.get()


Operation: GET /dataservice/multicloud/accounts/edge/{accountId}
----------------------------------------------------------------


Deprecated!!!

.. code:: python

    @overload
    def get(account_id: str) -> Any: ...


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
        client.multicloud.accounts.edge.get()


.. toctree::
    :maxdepth: 1

    credentials
    models

