=====================
app_registry.saasfeed
=====================


Operation: GET /dataservice/app-registry/saasfeed
-------------------------------------------------


Get All Saas feed details

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
        client.app_registry.saasfeed.get()


.. toctree::
    :maxdepth: 1

    app/index

