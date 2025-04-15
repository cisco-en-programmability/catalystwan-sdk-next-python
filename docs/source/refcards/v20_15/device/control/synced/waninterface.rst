==================================
device.control.synced.waninterface
==================================


Operation: GET /dataservice/device/control/synced/waninterface
--------------------------------------------------------------


Get WAN interface list

.. code:: python

    def get(device_id: str) -> List[Any]: ...


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
        client.device.control.synced.waninterface.get()


