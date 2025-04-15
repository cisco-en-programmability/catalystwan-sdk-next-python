===================================
device.sdwan_global_drop_statistics
===================================


Operation: GET /dataservice/device/sdwan-global-drop-statistics
---------------------------------------------------------------


Get SD-WAN global drop statistics detail from device (Real Time)

.. code:: python

    def get(device_id: str) -> Any: ...


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
        client.device.sdwan_global_drop_statistics.get()


