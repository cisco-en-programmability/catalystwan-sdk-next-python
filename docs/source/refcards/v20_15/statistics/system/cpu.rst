=====================
statistics.system.cpu
=====================


Operation: GET /dataservice/statistics/system/cpu
-------------------------------------------------


Get device system CPU stats list

.. code:: python

    def get(query: str, device_id: str) -> Any: ...


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
        client.statistics.system.cpu.get()


