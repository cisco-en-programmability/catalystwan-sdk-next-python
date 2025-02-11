==============
device.monitor
==============


Operation: GET /dataservice/device/monitor
------------------------------------------


Get all monitoring details of the devices

.. code:: python

    def list_all_monitor_details_devices() -> Any: ...


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
        client.device.monitor.list_all_monitor_details_devices()


