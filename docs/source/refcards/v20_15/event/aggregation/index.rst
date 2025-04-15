=================
event.aggregation
=================


Operation: GET /dataservice/event/aggregation
---------------------------------------------


Get aggregated count of events based on given query.

.. code:: python

    def get(
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
        client.event.aggregation.get()


Operation: POST /dataservice/event/aggregation
----------------------------------------------


Get aggregated count of events based on given query.

.. code:: python

    def post(
        payload: Any, site_id: Optional[str] = None
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
        client.event.aggregation.post()


.. toctree::
    :maxdepth: 1

    models

