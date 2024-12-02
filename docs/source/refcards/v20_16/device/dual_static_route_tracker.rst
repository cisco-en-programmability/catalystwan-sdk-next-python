================================
device.dual_static_route_tracker
================================


Operation: GET /dataservice/device/dualStaticRouteTracker
---------------------------------------------------------


Get dual static route tracker info from device

.. code:: python

    def get_dual_static_route_tracker_info(device_id: str) -> Any: ...


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
        client.device.dual_static_route_tracker.get_dual_static_route_tracker_info()


