=============
device.status
=============


Operation: GET /dataservice/device/status
-----------------------------------------


Get devices status for vSmart,vBond,vEdge, and cEdge

.. code:: python

    def get_all_device_status() -> List[Any]: ...


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
        client.device.status.get_all_device_status()


