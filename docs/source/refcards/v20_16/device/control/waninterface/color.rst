=================================
device.control.waninterface.color
=================================


Operation: GET /dataservice/device/control/waninterface/color
-------------------------------------------------------------


Get port hop colors

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
        client.device.control.waninterface.color.get()


