==============
device.vm.nics
==============


Operation: GET /dataservice/device/vm/nics
------------------------------------------


Get vbranch vm lifecycle state (NIC)

.. code:: python

    def get_vbranch_vm_lifecycle_nics(device_id: str) -> Any: ...


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
        client.device.vm.nics.get_vbranch_vm_lifecycle_nics()


