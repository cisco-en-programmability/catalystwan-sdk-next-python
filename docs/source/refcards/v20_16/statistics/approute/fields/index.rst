==========================
statistics.approute.fields
==========================


Operation: GET /dataservice/statistics/approute/fields
------------------------------------------------------


Get fields and type

.. code:: python

    def get_stat_data_fields_3() -> List[AppRouteDocCountResponse]: ...


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
        client.statistics.approute.fields.get_stat_data_fields_3()


.. toctree::
    :maxdepth: 1

    models

