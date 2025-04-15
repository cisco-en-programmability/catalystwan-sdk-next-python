===========================
statistics.approute.tunnels
===========================


Operation: GET /dataservice/statistics/approute/tunnels/{type}
--------------------------------------------------------------


Get tunnel top statistics from device

.. code:: python

    def get(
        type_: str,
        query: Optional[str] = None,
        limit: Optional[int] = None,
    ) -> List[AppRouteRespWithPageInfo]: ...


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
        client.statistics.approute.tunnels.get()


.. toctree::
    :maxdepth: 1

    health/index
    summary/index
    models

