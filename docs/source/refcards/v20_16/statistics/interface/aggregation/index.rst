================================
statistics.interface.aggregation
================================


Operation: GET /dataservice/statistics/interface/aggregation
------------------------------------------------------------


Get aggregated data based on input query and filters. The data can be filtered on time and other unique parameters based upon necessity and intended usage

.. code:: python

    def get_aggregation_data_by_query_11(
        query: str,
    ) -> List[InterfaceAggRespWithPageInfo]: ...


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
        client.statistics.interface.aggregation.get_aggregation_data_by_query_11()


Operation: POST /dataservice/statistics/interface/aggregation
-------------------------------------------------------------


Get aggregated data based on input query and filters. The data can be filtered on time and other unique parameters based upon necessity and intended usage

.. code:: python

    def get_post_aggregation_data_by_query_11(
        payload: Optional[Any] = None,
    ) -> List[InterfaceAggResp]: ...


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
        client.statistics.interface.aggregation.get_post_aggregation_data_by_query_11()


.. toctree::
    :maxdepth: 1

    models

