=======================
device.bfd.state.device
=======================


Operation: GET /dataservice/device/bfd/state/device
---------------------------------------------------


Get device BFD state summary

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
        client.device.bfd.state.device.get()


.. toctree::
    :maxdepth: 1

    tloc
    tloc_interface_map

