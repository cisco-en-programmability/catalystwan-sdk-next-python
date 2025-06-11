=====================================
statistics.approute.transport.summary
=====================================


Operation: GET /dataservice/statistics/approute/transport/summary/{type}
------------------------------------------------------------------------


Get application-aware routing statistics summary from device

.. code:: python

    def get(
        type_: str,
        limit: Optional[int] = 5,
        query: Optional[str] = None,
        site_id: Optional[str] = None,
    ) -> List[List[AppRouteFecAggRespInner]]: ...


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
        client.statistics.approute.transport.summary.get()


.. toctree::
    :maxdepth: 1

    models

