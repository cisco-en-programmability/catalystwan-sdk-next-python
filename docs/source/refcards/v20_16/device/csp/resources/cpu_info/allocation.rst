========================================
device.csp.resources.cpu_info.allocation
========================================


Operation: GET /dataservice/device/csp/resources/cpu-info/allocation
--------------------------------------------------------------------


Get NetworkHub CPU allocation info from device

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
        client.device.csp.resources.cpu_info.allocation.get()


