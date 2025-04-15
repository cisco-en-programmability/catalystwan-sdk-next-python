=======================
device.acl.matchcounter
=======================


Operation: GET /dataservice/device/acl/matchcounter
---------------------------------------------------


Get ACL match counters from device (Real Time)

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
        client.device.acl.matchcounter.get()


