=================
device.ntp.status
=================


Operation: GET /dataservice/device/ntp/status
---------------------------------------------


Get NTP status list from device (Real Time)

.. code:: python

    def create_ntp_status_list(device_id: str) -> List[Any]: ...


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
        client.device.ntp.status.create_ntp_status_list()


