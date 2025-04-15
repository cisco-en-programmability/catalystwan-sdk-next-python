=============================
event.get_events_by_component
=============================


Operation: GET /dataservice/event/getEventsByComponent
------------------------------------------------------


Get event names by component.

.. code:: python

    def get(query: str) -> ComponentEventMapping: ...


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
        client.event.get_events_by_component.get()


.. toctree::
    :maxdepth: 1

    models

