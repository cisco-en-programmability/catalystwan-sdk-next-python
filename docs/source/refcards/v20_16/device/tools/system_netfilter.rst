=============================
device.tools.system_netfilter
=============================


Operation: GET /dataservice/device/tools/system-netfilter
---------------------------------------------------------


Get system netfilter info from device

.. code:: python

    def get_system_netfilter(device_id: str) -> Any: ...


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
        client.device.tools.system_netfilter.get_system_netfilter()


