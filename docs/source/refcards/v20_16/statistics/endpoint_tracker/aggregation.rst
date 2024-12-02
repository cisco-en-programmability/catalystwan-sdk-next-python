=======================================
statistics.endpoint_tracker.aggregation
=======================================


Operation: GET /dataservice/statistics/endpointTracker/aggregation
------------------------------------------------------------------


Get aggregated data based on input query and filters. The data can be filtered on time and other unique parameters based upon necessity and intended usage

.. code:: python

    def get_aggregation_data_by_query_21(
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
        client.statistics.endpoint_tracker.aggregation.get_aggregation_data_by_query_21()


Operation: POST /dataservice/statistics/endpointTracker/aggregation
-------------------------------------------------------------------


Get aggregated data based on input query and filters. The data can be filtered on time and other unique parameters based upon necessity and intended usage

.. code:: python

    def get_post_aggregation_data_by_query_23(
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
        client.statistics.endpoint_tracker.aggregation.get_post_aggregation_data_by_query_23()


