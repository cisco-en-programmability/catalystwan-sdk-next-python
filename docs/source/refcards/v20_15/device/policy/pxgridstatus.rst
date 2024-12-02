==========================
device.policy.pxgridstatus
==========================


Operation: GET /dataservice/device/policy/pxgridstatus
------------------------------------------------------


show Pxgrid status From Vsmart

.. code:: python

    def show_vsmart_px_grid_status(device_id: str) -> Any: ...


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
        client.device.policy.pxgridstatus.show_vsmart_px_grid_status()


