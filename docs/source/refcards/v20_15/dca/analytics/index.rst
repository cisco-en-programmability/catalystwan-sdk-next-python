=============
dca.analytics
=============


Operation: PUT /dataservice/dca/analytics
-----------------------------------------


Update collection time of DCARest stat for vAnalytics

.. code:: python

    def create_stats(payload: Optional[Any] = None) -> None: ...


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
        client.dca.analytics.create_stats()


.. toctree::
    :maxdepth: 1

    all

