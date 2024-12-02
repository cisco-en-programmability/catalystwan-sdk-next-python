============================
device.voice.sccp_ccm_groups
============================


Operation: GET /dataservice/device/voice/sccpCcmGroups
------------------------------------------------------


Get DSPFarm SCCP CCM Groups info from device

.. code:: python

    def get_sccp_ccm_groups(device_id: str) -> Any: ...


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
        client.device.voice.sccp_ccm_groups.get_sccp_ccm_groups()


