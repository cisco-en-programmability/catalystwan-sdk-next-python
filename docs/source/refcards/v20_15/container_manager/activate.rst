==========================
container_manager.activate
==========================


Operation: POST /dataservice/container-manager/activate/{containerName}
-----------------------------------------------------------------------


Activate container on remote host

.. code:: python

    def post(
        container_name: str,
        url: Optional[str] = None,
        host_ip: Optional[str] = None,
        checksum: Optional[str] = None,
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
        client.container_manager.activate.post()


