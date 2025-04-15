===========================
statistics.bridgemac.fields
===========================


Operation: GET /dataservice/statistics/bridgemac/fields
-------------------------------------------------------


Get fields and type

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
        client.statistics.bridgemac.fields.get()


