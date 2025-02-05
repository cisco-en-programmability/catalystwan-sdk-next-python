==========================
statistics.ipsalert.fields
==========================


Operation: GET /dataservice/statistics/ipsalert/fields
------------------------------------------------------


Get fields and type

.. code:: python

    def get_stat_data_fields_23() -> Any: ...


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
        client.statistics.ipsalert.fields.get_stat_data_fields_23()


