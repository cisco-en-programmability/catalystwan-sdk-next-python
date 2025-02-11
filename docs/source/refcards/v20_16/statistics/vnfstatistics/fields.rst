===============================
statistics.vnfstatistics.fields
===============================


Operation: GET /dataservice/statistics/vnfstatistics/fields
-----------------------------------------------------------


Get fields and type

.. code:: python

    def get_stat_data_fields_13() -> Any: ...


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
        client.statistics.vnfstatistics.fields.get_stat_data_fields_13()


