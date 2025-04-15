=============================
statistics.approute.transport
=============================


Operation: GET /dataservice/statistics/approute/transport/{type}
----------------------------------------------------------------


Get application-aware routing statistics from device

.. code:: python

    def get(
        type_: str, limit: int, query: Optional[str] = None
    ) -> AppRouteTransportResp: ...


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
        client.statistics.approute.transport.get()


.. toctree::
    :maxdepth: 1

    summary/index
    models

