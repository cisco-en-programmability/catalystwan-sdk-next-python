============================
container_manager.deactivate
============================


Operation: POST /dataservice/container-manager/deactivate/{containerName}
-------------------------------------------------------------------------


Deactivate container on remote host

.. code:: python

    def post(
        container_name: str, host_ip: Optional[str] = None
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
        client.container_manager.deactivate.post()


