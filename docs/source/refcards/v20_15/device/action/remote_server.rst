===========================
device.action.remote_server
===========================


Operation: GET /dataservice/device/action/remote-server
-------------------------------------------------------


Get list of remote servers

.. code:: python

    def get_remote_server_list() -> Any: ...


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
        client.device.action.remote_server.get_remote_server_list()


Operation: POST /dataservice/device/action/remote-server
--------------------------------------------------------


Add a new remote server entry.

.. code:: python

    def add_remote_server(payload: Optional[Any] = None) -> None: ...


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
        client.device.action.remote_server.add_remote_server()


Operation: GET /dataservice/device/action/remote-server/{id}
------------------------------------------------------------


Get remote server for the specified ID

.. code:: python

    def get_remote_server_by_id(id: str) -> Any: ...


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
        client.device.action.remote_server.get_remote_server_by_id()


Operation: PUT /dataservice/device/action/remote-server/{id}
------------------------------------------------------------


Update remote server for the specified ID

.. code:: python

    def update_remote_server(
        id: str, payload: Optional[str] = None
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
        client.device.action.remote_server.update_remote_server()


Operation: DELETE /dataservice/device/action/remote-server/{id}
---------------------------------------------------------------


Delete remote server for the specified ID

.. code:: python

    def delete_remote_server(
        id: str, payload: Optional[Any] = None
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
        client.device.action.remote_server.delete_remote_server()


