==========================
statistics.qos.aggregation
==========================


Operation: GET /dataservice/statistics/qos/aggregation
------------------------------------------------------


Monitoring - QoS

.. code:: python

    def get_aggregation_data_by_query_13(
        query: Optional[str] = None,
    ) -> List[QoSAggResp]: ...


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
        client.statistics.qos.aggregation.get_aggregation_data_by_query_13()


Operation: POST /dataservice/statistics/qos/aggregation
-------------------------------------------------------


Get aggregated data based on input query and filters. The data can be filtered on time and other unique parameters based upon necessity and intended usage

.. code:: python

    def get_post_aggregation_data_by_query_13(
        payload: Optional[Any] = None,
    ) -> List[QoSAggResp]: ...


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
        client.statistics.qos.aggregation.get_post_aggregation_data_by_query_13()


.. toctree::
    :maxdepth: 1

    models

