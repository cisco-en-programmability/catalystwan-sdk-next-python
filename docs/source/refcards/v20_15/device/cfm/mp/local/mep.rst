=======================
device.cfm.mp.local.mep
=======================


Operation: GET /dataservice/device/cfm/mp/local/mep
---------------------------------------------------


Get mp local mep from device

.. code:: python

    def get_mp_local_mep(
        device_id: str,
        domain: Optional[str] = None,
        service: Optional[str] = None,
        mep_id: Optional[int] = None,
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
        client.device.cfm.mp.local.mep.get_mp_local_mep()


