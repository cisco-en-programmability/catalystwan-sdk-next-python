====================
device.control.count
====================


Operation: GET /dataservice/device/control/count
------------------------------------------------


Get number of vedges and vsmart device in different control states

.. code:: python

    def get(
        is_cached: Optional[bool] = False, site_id: Optional[str] = None
    ) -> Any: ...


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
        client.device.control.count.get()


