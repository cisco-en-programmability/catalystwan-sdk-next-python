====================
event.types.keyvalue
====================


Operation: GET /dataservice/event/types/keyvalue
------------------------------------------------


Get event types.

.. code:: python

    def get_event_types_as_key_value() -> SimpleKeyValueMapping: ...


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
        client.event.types.keyvalue.get_event_types_as_key_value()


.. toctree::
    :maxdepth: 1

    models

