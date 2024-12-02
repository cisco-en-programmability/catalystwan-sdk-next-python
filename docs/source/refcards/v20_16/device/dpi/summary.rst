==================
device.dpi.summary
==================


Operation: GET /dataservice/device/dpi/summary
----------------------------------------------


Get DPI summary from device (Real Time)

.. code:: python

    def create_dpi_summary_real_time(device_id: str) -> Any: ...


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
        client.device.dpi.summary.create_dpi_summary_real_time()


