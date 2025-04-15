==================
alarms.aggregation
==================


Operation: GET /dataservice/alarms/aggregation
----------------------------------------------


Get aggregated count of alarms based on given query.

.. code:: python

    def get(
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
        client.alarms.aggregation.get()


Operation: POST /dataservice/alarms/aggregation
-----------------------------------------------


Get aggregated count of alarms based on given query.

.. code:: python

    def post(
        payload: Any,
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
        client.alarms.aggregation.post()


.. toctree::
    :maxdepth: 1

    models

