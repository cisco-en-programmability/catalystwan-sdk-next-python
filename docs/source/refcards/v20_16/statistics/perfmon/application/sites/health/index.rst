===========================================
statistics.perfmon.application.sites.health
===========================================


Operation: GET /dataservice/statistics/perfmon/application/sites/health
-----------------------------------------------------------------------


Get one application health for all sites

.. code:: python

    def get(
        application: str,
        is_heat_map: Optional[bool] = None,
        last_n_hours: Optional[LastNHoursParam] = None,
        health: Optional[HealthParam] = None,
    ) -> List[ApplicationSitesItem]: ...


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
        client.statistics.perfmon.application.sites.health.get()


.. toctree::
    :maxdepth: 1

    models

