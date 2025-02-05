========================
statistics.system.fields
========================


Operation: GET /dataservice/statistics/system/fields
----------------------------------------------------


Get fields and type

.. code:: python

    def get_stat_data_fields_18() -> Any: ...


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
        client.statistics.system.fields.get_stat_data_fields_18()


