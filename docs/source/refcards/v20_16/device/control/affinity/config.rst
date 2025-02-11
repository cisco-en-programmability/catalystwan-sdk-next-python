==============================
device.control.affinity.config
==============================


Operation: GET /dataservice/device/control/affinity/config
----------------------------------------------------------


Get affinity config from device (Real Time)

.. code:: python

    def get_affinity_config(device_id: str) -> Any: ...


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
        client.device.control.affinity.config.get_affinity_config()


