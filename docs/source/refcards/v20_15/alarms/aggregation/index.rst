==================
alarms.aggregation
==================


Operation: GET /dataservice/alarms/aggregation
----------------------------------------------


Get aggregated count of alarms based on given query.

.. code:: python

    def get_aggregation_data(
        query: str, site_id: Optional[str] = None
    ) -> AlarmAggregationResponse: ...


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
        client.alarms.aggregation.get_aggregation_data()


Operation: POST /dataservice/alarms/aggregation
-----------------------------------------------


Get aggregated count of alarms based on given query.

.. code:: python

    def post_aggregation_data(
        payload: Optional[Any] = None, site_id: Optional[str] = None
    ) -> AlarmAggregationResponse: ...


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
        client.alarms.aggregation.post_aggregation_data()


.. toctree::
    :maxdepth: 1

    models

