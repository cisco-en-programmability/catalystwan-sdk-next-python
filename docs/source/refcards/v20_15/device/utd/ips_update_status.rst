============================
device.utd.ips_update_status
============================


Operation: GET /dataservice/device/utd/ips-update-status
--------------------------------------------------------


Get UTD IPS update status from device (Real Time)

.. code:: python

    def get_utd_ips_update_status(device_id: str) -> Any: ...


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
        client.device.utd.ips_update_status.get_utd_ips_update_status()


