=======================================
device.cedgecflowd.app_fwd_cflowd_flows
=======================================


Operation: GET /dataservice/device/cedgecflowd/app-fwd-cflowd-flows
-------------------------------------------------------------------


Get list of app fwd cflowd flows from device

.. code:: python

    def get(
        device_id: str,
        vpn_id: Optional[int] = None,
        src_addr: Optional[str] = None,
        dst_addr: Optional[str] = None,
        app: Optional[str] = None,
        family: Optional[str] = None,
    ) -> None: ...


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
        client.device.cedgecflowd.app_fwd_cflowd_flows.get()


