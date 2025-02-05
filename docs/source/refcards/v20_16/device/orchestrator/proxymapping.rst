================================
device.orchestrator.proxymapping
================================


Operation: GET /dataservice/device/orchestrator/proxymapping
------------------------------------------------------------


Get reverse proxy mapping from vbond

.. code:: python

    def create_reverse_proxy_mapping_list(device_id: str) -> Any: ...


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
        client.device.orchestrator.proxymapping.create_reverse_proxy_mapping_list()


