================================
statistics.bridgemac.aggregation
================================


Operation: GET /dataservice/statistics/bridgemac/aggregation
------------------------------------------------------------


Get aggregated data based on input query and filters. The data can be filtered on time and other unique parameters based upon necessity and intended usage

.. code:: python

    def get_aggregation_data_by_query_7(
        query: Optional[str] = None,
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
        client.statistics.bridgemac.aggregation.get_aggregation_data_by_query_7()


Operation: POST /dataservice/statistics/bridgemac/aggregation
-------------------------------------------------------------


Get aggregated data based on input query and filters. The data can be filtered on time and other unique parameters based upon necessity and intended usage

.. code:: python

    def get_post_aggregation_data_by_query_7(
        payload: Optional[Any] = None,
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
        client.statistics.bridgemac.aggregation.get_post_aggregation_data_by_query_7()


