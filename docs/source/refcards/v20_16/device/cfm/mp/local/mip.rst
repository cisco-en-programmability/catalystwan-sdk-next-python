=======================
device.cfm.mp.local.mip
=======================


Operation: GET /dataservice/device/cfm/mp/local/mip
---------------------------------------------------


Get mp local mip from device

.. code:: python

    def get_mp_local_mip(
        device_id: str,
        level: Optional[int] = None,
        port: Optional[str] = None,
        svc_inst: Optional[int] = None,
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
        client.device.cfm.mp.local.mip.get_mp_local_mip()


