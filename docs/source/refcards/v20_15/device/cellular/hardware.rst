========================
device.cellular.hardware
========================


Operation: GET /dataservice/device/cellular/hardware
----------------------------------------------------


Get cellular hardware list from device

.. code:: python

    def create_hardware_list(device_id: str) -> List[Any]: ...


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
        client.device.cellular.hardware.create_hardware_list()


