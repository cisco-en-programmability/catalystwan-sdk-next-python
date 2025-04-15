==================================
device.csp.resources.cpu_info.vnfs
==================================


Operation: GET /dataservice/device/csp/resources/cpu-info/vnfs
--------------------------------------------------------------


Get NetworkHub CPU VNF info from device

.. code:: python

    def get(device_id: str) -> Any: ...


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
        client.device.csp.resources.cpu_info.vnfs.get()


