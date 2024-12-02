===========================================
multicloud.interconnect.monitoring.gateways
===========================================


Operation: GET /dataservice/multicloud/interconnect/{interconnect-type}/monitoring/gateways
-------------------------------------------------------------------------------------------


API to retrieve Interconnect gateways by Interconnect type for monitoring.

.. code:: python

    def get_monitoring_interconnect_gateways(
        interconnect_type: str,
    ) -> List[InterconnectGatewayMonitoring]: ...


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
        client.multicloud.interconnect.monitoring.gateways.get_monitoring_interconnect_gateways()


.. toctree::
    :maxdepth: 1

    models

