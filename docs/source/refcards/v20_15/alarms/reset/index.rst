============
alarms.reset
============


Operation: GET /dataservice/alarms/reset
----------------------------------------


Reset correlation engine.

.. code:: python

    def get() -> SimpleMessageResponse: ...


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
        client.alarms.reset.get()


.. toctree::
    :maxdepth: 1

    models

