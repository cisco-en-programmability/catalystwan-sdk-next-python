============================================
statistics.perfmon.applications.sites.health
============================================


Operation: GET /dataservice/statistics/perfmon/applications/sites/health
------------------------------------------------------------------------


Get applications health for all sites

.. code:: python

    def get(
        is_heat_map: Optional[bool] = None,
        last_n_hours: Optional[LastNHoursParam] = None,
        health: Optional[HealthParam] = None,
        include_usage: Optional[bool] = False,
        use_cache: Optional[bool] = True,
    ) -> List[ApplicationsSitesItem]: ...


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
        client.statistics.perfmon.applications.sites.health.get()


.. toctree::
    :maxdepth: 1

    models

