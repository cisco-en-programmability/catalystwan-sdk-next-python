=============================
device.endpoint_tracker_group
=============================


Operation: GET /dataservice/device/endpointTrackerGroup
-------------------------------------------------------


Get endpoint tracker group info from device

.. code:: python

    def get_endpoint_tracker_group_info(device_id: str) -> Any: ...


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
        client.device.endpoint_tracker_group.get_endpoint_tracker_group_info()


