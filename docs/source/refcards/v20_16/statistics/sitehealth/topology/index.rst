==============================
statistics.sitehealth.topology
==============================


Operation: GET /dataservice/statistics/sitehealth/topology
----------------------------------------------------------


Get all site health topology

.. code:: python

    def get_site_health_topology(
        last_n_hours: Optional[int] = None,
        start_time: Optional[int] = None,
        end_time: Optional[int] = None,
        interval: Optional[int] = 30,
    ) -> List[SiteHealthTopologyItem]: ...


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
        client.statistics.sitehealth.topology.get_site_health_topology()


.. toctree::
    :maxdepth: 1

    models

