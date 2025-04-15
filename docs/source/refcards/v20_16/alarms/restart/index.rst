==============
alarms.restart
==============


Operation: GET /dataservice/alarms/restart
------------------------------------------


Restart correlation engine.

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
        client.alarms.restart.get()


.. toctree::
    :maxdepth: 1

    models

