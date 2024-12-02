================================
stream.device.capture.vnics_info
================================


Operation: GET /dataservice/stream/device/capture/vnicsInfo/{vnfId}
-------------------------------------------------------------------


Get vnic info by vrfId

.. code:: python

    def get_vnic_info_by_vnf_id(vnf_id: str) -> List[VnicInfo]: ...


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
        client.stream.device.capture.vnics_info.get_vnic_info_by_vnf_id()


.. toctree::
    :maxdepth: 1

    models

