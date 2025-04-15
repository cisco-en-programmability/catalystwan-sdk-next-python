===================
alarms.query.fields
===================


Operation: GET /dataservice/alarms/query/fields
-----------------------------------------------


Get query fields

.. code:: python

    def get() -> Any: ...


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
        client.alarms.query.fields.get()


