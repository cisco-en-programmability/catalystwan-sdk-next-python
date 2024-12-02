==================================
statistics.approute.tunnels.health
==================================


Operation: GET /dataservice/statistics/approute/tunnels/health/{type}
---------------------------------------------------------------------


Get tunnel health

.. code:: python

    def get_app_route_tunnel_health(
        type_: str,
        limit: Optional[int] = 10,
        last_n_hours: Optional[int] = 3,
        last_n_minutes: Optional[int] = None,
        device_ip: Optional[str] = None,
        site_id: Optional[str] = None,
        region_name: Optional[str] = None,
    ) -> List[AppRouteTunnenSummarResp]: ...


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
        client.statistics.approute.tunnels.health.get_app_route_tunnel_health()


.. toctree::
    :maxdepth: 1

    models

