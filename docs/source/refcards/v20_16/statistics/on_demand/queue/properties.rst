=====================================
statistics.on_demand.queue.properties
=====================================


Operation: GET /dataservice/statistics/on-demand/queue/properties
-----------------------------------------------------------------


gets current size of on-demand queue

.. code:: python

    def get_queue_properties() -> Any: ...


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
        client.statistics.on_demand.queue.properties.get_queue_properties()


