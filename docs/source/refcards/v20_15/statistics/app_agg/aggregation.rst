==============================
statistics.app_agg.aggregation
==============================


Operation: POST /dataservice/statistics/app-agg/aggregation
-----------------------------------------------------------


Get aggregated data based on input query and filters. The data can be filtered on time and other unique parameters based upon necessity and intended usage

.. code:: python

    def get_post_aggregation_app_data_by_query(
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
        client.statistics.app_agg.aggregation.get_post_aggregation_app_data_by_query()


