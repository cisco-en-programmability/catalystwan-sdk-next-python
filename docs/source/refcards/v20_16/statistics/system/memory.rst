========================
statistics.system.memory
========================


Operation: GET /dataservice/statistics/system/memory
----------------------------------------------------


Get device system memory stats list

.. code:: python

    def create_device_system_memory_stat(
        query: str, device_id: str
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
        client.statistics.system.memory.create_device_system_memory_stat()


