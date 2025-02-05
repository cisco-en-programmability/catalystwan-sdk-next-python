=================
event.aggregation
=================


Operation: GET /dataservice/event/aggregation
---------------------------------------------


Get aggregated count of events based on given query.

.. code:: python

    def get_aggregation_data_1(
        query: str,
        site_id: Optional[str] = None,
        include_tenants: Optional[bool] = None,
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
        client.event.aggregation.get_aggregation_data_1()


Operation: POST /dataservice/event/aggregation
----------------------------------------------


Get aggregated count of events based on given query.

.. code:: python

    def post_aggregation_data_1(
        payload: Optional[Any] = None,
        site_id: Optional[str] = None,
        include_tenants: Optional[bool] = None,
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
        client.event.aggregation.post_aggregation_data_1()


.. toctree::
    :maxdepth: 1

    models

