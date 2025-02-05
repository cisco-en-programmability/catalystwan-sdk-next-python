=====================================
msla.monitoring.licensed_device_count
=====================================


Operation: GET /dataservice/msla/monitoring/licensedDeviceCount
---------------------------------------------------------------


Get licenses associated to device

.. code:: python

    def get_device_details_for_dashboard() -> Any: ...


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
        client.msla.monitoring.licensed_device_count.get_device_details_for_dashboard()


