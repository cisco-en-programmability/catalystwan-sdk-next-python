===========
alarms.dump
===========


Operation: POST /dataservice/alarms/dump
----------------------------------------


Dump correlation engine server cache in log file

.. code:: python

    def dump_correlation_engine_data() -> SimpleMessageResponse: ...


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
        client.alarms.dump.dump_correlation_engine_data()


.. toctree::
    :maxdepth: 1

    models

