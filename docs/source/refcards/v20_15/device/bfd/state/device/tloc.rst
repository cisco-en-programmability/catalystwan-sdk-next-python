============================
device.bfd.state.device.tloc
============================


Operation: GET /dataservice/device/bfd/state/device/tloc
--------------------------------------------------------


Get device BFD state summary with tloc color

.. code:: python

    def get_device_bfd_state_summary_tloc(device_id: str) -> Any: ...


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
        client.device.bfd.state.device.tloc.get_device_bfd_state_summary_tloc()


