================================
statistics.tunnelhealth.overview
================================


Operation: GET /dataservice/statistics/tunnelhealth/overview/{type}
-------------------------------------------------------------------


Get all tunnel health overview

.. code:: python

    def statistics_approute_tunnelhealth_overview_type_get(
        type_: str,
        last_n_hours: Optional[int] = 12,
        site: Optional[str] = None,
        limit: Optional[int] = 30,
    ) -> TunnelHealthOverview: ...


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
        client.statistics.tunnelhealth.overview.statistics_approute_tunnelhealth_overview_type_get()


.. toctree::
    :maxdepth: 1

    models

