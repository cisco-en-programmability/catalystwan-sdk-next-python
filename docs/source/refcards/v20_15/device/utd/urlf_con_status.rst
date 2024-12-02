==========================
device.utd.urlf_con_status
==========================


Operation: GET /dataservice/device/utd/urlf-con-status
------------------------------------------------------


Get UTD URLF Connection status from device (Real Time)

.. code:: python

    def get_utd_urlf_connection_status(device_id: str) -> Any: ...


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
        client.device.utd.urlf_con_status.get_utd_urlf_connection_status()


