==================
event.query.fields
==================


Operation: GET /dataservice/event/query/fields
----------------------------------------------


Get query fields

.. code:: python

    def get_query_fields() -> EventQueryInputResponse: ...


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
        client.event.query.fields.get_query_fields()


.. toctree::
    :maxdepth: 1

    models

