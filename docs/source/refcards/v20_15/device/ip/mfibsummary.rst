=====================
device.ip.mfibsummary
=====================


Operation: GET /dataservice/device/ip/mfibsummary
-------------------------------------------------


Get IP MFIB summary list from device (Real Time)

.. code:: python

    def create_ip_mfib_summary_list(device_id: str) -> Any: ...


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
        client.device.ip.mfibsummary.create_ip_mfib_summary_list()


