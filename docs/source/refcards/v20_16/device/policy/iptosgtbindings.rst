=============================
device.policy.iptosgtbindings
=============================


Operation: GET /dataservice/device/policy/iptosgtbindings
---------------------------------------------------------


show ip to sgt binding from Vsmart

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
        client.device.policy.iptosgtbindings.get()


