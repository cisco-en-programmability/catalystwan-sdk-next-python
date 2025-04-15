=========================
app_registry.app.category
=========================


Operation: GET /dataservice/app-registry/app/category
-----------------------------------------------------


Get the stats of all type of apps

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
        client.app_registry.app.category.get()


