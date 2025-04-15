=====================================
statistics.cflowd.device.applications
=====================================


Operation: GET /dataservice/statistics/cflowd/device/applications
-----------------------------------------------------------------


Deprecated!!!

Generate cflowd flows list in a grid table

.. code:: python

    def get(query: Optional[str] = None) -> Any: ...


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
        client.statistics.cflowd.device.applications.get()


