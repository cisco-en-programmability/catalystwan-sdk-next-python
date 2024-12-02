=========================
statistics.flowlog.fields
=========================


Operation: GET /dataservice/statistics/flowlog/fields
-----------------------------------------------------


Get fields and type

.. code:: python

    def get_flowlog_fields() -> List[GetStatDataFields]: ...


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
        client.statistics.flowlog.fields.get_flowlog_fields()


.. toctree::
    :maxdepth: 1

    models

