===============
event.listeners
===============


Operation: GET /dataservice/event/listeners
-------------------------------------------


Retrieve listener information

.. code:: python

    def get_listeners_info() -> str: ...


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
        client.event.listeners.get_listeners_info()


