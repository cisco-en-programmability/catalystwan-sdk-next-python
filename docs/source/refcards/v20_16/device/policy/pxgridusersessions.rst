================================
device.policy.pxgridusersessions
================================


Operation: GET /dataservice/device/policy/pxgridusersessions
------------------------------------------------------------


show Pxgrid sessions From Vsmart

.. code:: python

    def show_vsmart_px_grid_user_sessions(device_id: str) -> Any: ...


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
        client.device.policy.pxgridusersessions.show_vsmart_px_grid_user_sessions()


