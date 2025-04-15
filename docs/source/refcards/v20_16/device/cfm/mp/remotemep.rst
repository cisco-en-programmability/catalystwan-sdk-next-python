=======================
device.cfm.mp.remotemep
=======================


Operation: GET /dataservice/device/cfm/mp/remotemep
---------------------------------------------------


Get mp remote mep from device

.. code:: python

    def get(
        device_id: str,
        domain: Optional[str] = None,
        service: Optional[str] = None,
        local_mep_id: Optional[int] = None,
        remote_mep_id: Optional[int] = None,
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
        client.device.cfm.mp.remotemep.get()


