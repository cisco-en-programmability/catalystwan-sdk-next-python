=================
event.query.input
=================


Operation: GET /dataservice/event/query/input
---------------------------------------------


Get event field details

.. code:: python

    def create_events_query_config() -> EventQueryInputResponse: ...


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
        client.event.query.input.create_events_query_config()


.. toctree::
    :maxdepth: 1

    models

