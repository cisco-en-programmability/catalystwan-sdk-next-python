===========================
statistics.dpi.applications
===========================


Operation: GET /dataservice/statistics/dpi/applications
-------------------------------------------------------


Get detailed DPI application flows list in a grid table

.. code:: python

    def get(
        query: str, limit: Optional[int] = None
    ) -> DpiAppResponse: ...


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
        client.statistics.dpi.applications.get()


.. toctree::
    :maxdepth: 1

    summary/index
    models

