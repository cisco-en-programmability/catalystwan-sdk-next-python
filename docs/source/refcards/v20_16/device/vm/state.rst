===============
device.vm.state
===============


Operation: GET /dataservice/device/vm/state
-------------------------------------------


Get vm lifecycle state

.. code:: python

    def get_vm_life_cycle_state(device_id: str) -> Any: ...


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
        client.device.vm.state.get_vm_life_cycle_state()


