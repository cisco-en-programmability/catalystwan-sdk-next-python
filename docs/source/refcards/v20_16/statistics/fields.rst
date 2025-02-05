=================
statistics.fields
=================


Operation: GET /dataservice/statistics/fields
---------------------------------------------


Get fields and type

.. code:: python

    def get_stat_data_fields_14() -> Any: ...


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
        client.statistics.fields.get_stat_data_fields_14()


