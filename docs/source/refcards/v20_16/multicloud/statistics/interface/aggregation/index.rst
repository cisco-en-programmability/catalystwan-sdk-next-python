===========================================
multicloud.statistics.interface.aggregation
===========================================


Operation: POST /dataservice/multicloud/statistics/interface/aggregation
------------------------------------------------------------------------


Get aggregated data based on input query and filter. The data can be filtered on time and other unique parameters based upon necessity and intended usage

.. code:: python

    def get_post_aggregation_data_by_query_30(
        payload: Optional[Any] = None,
    ) -> InlineResponse2001: ...


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
        client.multicloud.statistics.interface.aggregation.get_post_aggregation_data_by_query_30()


.. toctree::
    :maxdepth: 1

    models

