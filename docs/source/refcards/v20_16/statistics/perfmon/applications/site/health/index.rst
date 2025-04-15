===========================================
statistics.perfmon.applications.site.health
===========================================


Operation: GET /dataservice/statistics/perfmon/applications/site/health
-----------------------------------------------------------------------


Get all applications health for one site

.. code:: python

    def get(
        siteid: str,
        is_heat_map: Optional[bool] = None,
        last_n_hours: Optional[LastNHoursParam] = None,
        health: Optional[HealthParam] = None,
        include_usage: Optional[bool] = False,
    ) -> List[ApplicationsSiteItem]: ...


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
        client.statistics.perfmon.applications.site.health.get()


.. toctree::
    :maxdepth: 1

    models

