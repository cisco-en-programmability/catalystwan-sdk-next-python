==============================
statistics.cflowd.applications
==============================


Operation: GET /dataservice/statistics/cflowd/applications
----------------------------------------------------------


Deprecated!!!

Generate cflowd flows list in a grid table

.. code:: python

    def get(
        vpn: Optional[str] = None,
        device_id: Optional[str] = None,
        limit: Optional[int] = None,
        query: Optional[str] = None,
    ) -> Any: ...


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
        client.statistics.cflowd.applications.get()


.. toctree::
    :maxdepth: 1

    summary

