==========================================
statistics.perfmon.application.site.health
==========================================


Operation: POST /dataservice/statistics/perfmon/application/site/health
-----------------------------------------------------------------------


Get one application health for one site

.. code:: python

    def get_application_site_health(
        payload: Optional[Any] = None,
        health: Optional[HealthParam] = None,
    ) -> List[ApplicationSiteItem]: ...


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
        client.statistics.perfmon.application.site.health.get_application_site_health()


.. toctree::
    :maxdepth: 1

    models

