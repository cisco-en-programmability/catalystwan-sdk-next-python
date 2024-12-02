==========================================
multicloud.interconnect.monitoring.devices
==========================================


Operation: GET /dataservice/multicloud/interconnect/{interconnect-type}/monitoring/devices
------------------------------------------------------------------------------------------


API to retrieve Interconnect devices by Interconnect type for monitoring.

.. code:: python

    def get_monitoring_interconnect_devices(
        interconnect_type: str,
        interconnect_gateway_name: Optional[str] = None,
    ) -> List[InterconnectDeviceInfoExtended]: ...


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
        client.multicloud.interconnect.monitoring.devices.get_monitoring_interconnect_devices()


.. toctree::
    :maxdepth: 1

    models

