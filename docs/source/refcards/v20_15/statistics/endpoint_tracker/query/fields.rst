========================================
statistics.endpoint_tracker.query.fields
========================================


Operation: GET /dataservice/statistics/endpointTracker/query/fields
-------------------------------------------------------------------


Get query fields

.. code:: python

    def get() -> Any: ...


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
        client.statistics.endpoint_tracker.query.fields.get()


