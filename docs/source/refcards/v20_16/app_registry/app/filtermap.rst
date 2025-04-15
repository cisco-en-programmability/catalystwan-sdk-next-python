==========================
app_registry.app.filtermap
==========================


Operation: GET /dataservice/app-registry/app/filtermap
------------------------------------------------------


Get all available filters for applist

.. code:: python

    def get() -> List[Any]: ...


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
        client.app_registry.app.filtermap.get()


