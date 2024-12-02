===========================
device.static_route_tracker
===========================


Operation: GET /dataservice/device/staticRouteTracker
-----------------------------------------------------


Get single static route tracker info from device

.. code:: python

    def get_static_route_tracker_info(device_id: str) -> Any: ...


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
        client.device.static_route_tracker.get_static_route_tracker_info()


