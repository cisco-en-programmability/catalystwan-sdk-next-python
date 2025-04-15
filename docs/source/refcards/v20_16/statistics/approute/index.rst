===================
statistics.approute
===================


Operation: GET /dataservice/statistics/approute
-----------------------------------------------


Get stats raw data

.. code:: python

    def get(
        query: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        sort_by: Optional[str] = None,
        sort_order: Optional[SortOrderParam] = None,
    ) -> Any: ...


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
        client.statistics.approute.get()


Operation: POST /dataservice/statistics/approute
------------------------------------------------


Get stats raw data

.. code:: python

    def post(
        payload: Any,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        sort_by: Optional[str] = None,
        sort_order: Optional[SortOrderParam] = None,
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
        client.statistics.approute.post()


.. toctree::
    :maxdepth: 1

    aggregation/index
    app_agg/index
    csv
    device/index
    doccount
    fec/index
    fields/index
    page/index
    query/index
    tloc/index
    transport/index
    tunnel/index
    tunnels/index
    models

