==================
alarms.query.input
==================


Operation: GET /dataservice/alarms/query/input
----------------------------------------------


Get alarm field details

.. code:: python

    def get_field_details() -> AlarmQueryInputResponse: ...


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
        client.alarms.query.input.get_field_details()


.. toctree::
    :maxdepth: 1

    models

