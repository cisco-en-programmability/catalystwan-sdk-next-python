===================
device.dot1x.radius
===================


Operation: GET /dataservice/device/dot1x/radius
-----------------------------------------------


Get DOT1x Radius from device (Real Time)

.. code:: python

    def get_dot1x_radius(device_id: str) -> Any: ...


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
        client.device.dot1x.radius.get_dot1x_radius()


