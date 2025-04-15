=========================
container_manager.inspect
=========================


Operation: GET /dataservice/container-manager/inspect/{containerName}
---------------------------------------------------------------------


Get container inspect data

.. code:: python

    def get(
        container_name: str, host_ip: Optional[str] = None
    ) -> str: ...


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
        client.container_manager.inspect.get()


