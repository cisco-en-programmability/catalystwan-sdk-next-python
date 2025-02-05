==============================
device.control.affinity.status
==============================


Operation: GET /dataservice/device/control/affinity/status
----------------------------------------------------------


Get affinity status from device (Real Time)

.. code:: python

    def get_affinity_status(device_id: str) -> Any: ...


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
        client.device.control.affinity.status.get_affinity_status()


