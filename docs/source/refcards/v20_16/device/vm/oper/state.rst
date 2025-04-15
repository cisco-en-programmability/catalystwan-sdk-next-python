====================
device.vm.oper.state
====================


Operation: GET /dataservice/device/vm/oper/state
------------------------------------------------


Get vbranch vm lifecycle state

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
        client.device.vm.oper.state.get()


