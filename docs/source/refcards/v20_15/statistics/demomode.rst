===================
statistics.demomode
===================


Operation: GET /dataservice/statistics/demomode
-----------------------------------------------


Enable statistic demo mode

.. code:: python

    def get(enable: Optional[bool] = True) -> Any: ...


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
        client.statistics.demomode.get()


