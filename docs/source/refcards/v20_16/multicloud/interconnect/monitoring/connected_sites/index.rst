==================================================
multicloud.interconnect.monitoring.connected_sites
==================================================


Operation: GET /dataservice/multicloud/interconnect/{interconnect-type}/monitoring/connected-sites
--------------------------------------------------------------------------------------------------


API to retrieve Interconnect devices by Interconnect type for monitoring.

.. code:: python

    def get_monitoring_interconnect_connected_sites(
        interconnect_type: str,
        interconnect_gateway_name: Optional[str] = None,
    ) -> List[InterconnectConnectedSite]: ...


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
        client.multicloud.interconnect.monitoring.connected_sites.get_monitoring_interconnect_connected_sites()


.. toctree::
    :maxdepth: 1

    models

