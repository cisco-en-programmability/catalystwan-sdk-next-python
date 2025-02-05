=================
dca.analytics.all
=================


Operation: POST /dataservice/dca/analytics/all
----------------------------------------------


Get all statistics setting data

.. code:: python

    def get_all_stats_data_dca(payload: Optional[Any] = None) -> Any: ...


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
        client.dca.analytics.all.get_all_stats_data_dca()


