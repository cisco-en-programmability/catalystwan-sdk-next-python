==========================
statistics.approute.fields
==========================


Operation: GET /dataservice/statistics/approute/fields
------------------------------------------------------


Get fields and type

.. code:: python

    def get() -> List[AppRouteDocCountResponse]: ...


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
        client.statistics.approute.fields.get()


.. toctree::
    :maxdepth: 1

    models

