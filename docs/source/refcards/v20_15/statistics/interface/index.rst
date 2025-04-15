====================
statistics.interface
====================


Operation: GET /dataservice/statistics/interface
------------------------------------------------


Get stats raw data

.. code:: python

    def get(
        query: str,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        sort_by: Optional[str] = None,
        sort_order: Optional[SortOrderParam] = None,
    ) -> InterfaceQuery: ...


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
        client.statistics.interface.get()


Operation: POST /dataservice/statistics/interface
-------------------------------------------------


Get stats raw data

.. code:: python

    def post(
        payload: Any,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        sort_by: Optional[str] = None,
        sort_order: Optional[SortOrderParam] = None,
    ) -> List[InterfaceRespWithPageInfo]: ...


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
        client.statistics.interface.post()


.. toctree::
    :maxdepth: 1

    aggregation/index
    app_agg/index
    ccapacity/index
    csv
    doccount
    fields/index
    page/index
    query/index
    type_/index
    models

