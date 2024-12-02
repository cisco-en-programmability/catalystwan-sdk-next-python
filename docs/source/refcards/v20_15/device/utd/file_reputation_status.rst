=================================
device.utd.file_reputation_status
=================================


Operation: GET /dataservice/device/utd/file-reputation-status
-------------------------------------------------------------


Get UTD file reputation status from device (Real Time)

.. code:: python

    def get_utd_file_reputation_status(device_id: str) -> Any: ...


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
        client.device.utd.file_reputation_status.get_utd_file_reputation_status()


