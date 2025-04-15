==============
statistics.dpi
==============


Operation: GET /dataservice/statistics/dpi
------------------------------------------


Get DPI stats raw data

.. code:: python

    def get(
        query: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        sort_by: Optional[str] = None,
        sort_order: Optional[SortOrderParam] = None,
    ) -> DpiResponse: ...


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
        client.statistics.dpi.get()


Operation: POST /dataservice/statistics/dpi
-------------------------------------------


Get DPI stats raw data

.. code:: python

    def post(
        payload: Any,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        sort_by: Optional[str] = None,
        sort_order: Optional[SortOrderParam] = None,
    ) -> DpiResponse: ...


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
        client.statistics.dpi.post()


.. toctree::
    :maxdepth: 1

    agg_app/index
    aggregation/index
    applications/index
    csv
    device/index
    doccount/index
    fields
    page/index
    pktdup/index
    query/index
    recovery/index
    models

