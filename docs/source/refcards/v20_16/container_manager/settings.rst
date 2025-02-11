==========================
container_manager.settings
==========================


Operation: GET /dataservice/container-manager/settings/{containerName}
----------------------------------------------------------------------


Get container settings

.. code:: python

    def get_container_settings(
        container_name: str, host_ip: Optional[str] = None
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
        client.container_manager.settings.get_container_settings()


