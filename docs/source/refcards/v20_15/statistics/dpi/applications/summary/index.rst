===================================
statistics.dpi.applications.summary
===================================


Operation: GET /dataservice/statistics/dpi/applications/summary
---------------------------------------------------------------


Get detailed DPI application flows summary

.. code:: python

    def get_agg_app_flows_summary(
        query: str,
        limit: Optional[int] = None,
        site_id: Optional[str] = None,
    ) -> DpiAppResponse: ...


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
        client.statistics.dpi.applications.summary.get_agg_app_flows_summary()


.. toctree::
    :maxdepth: 1

    models

