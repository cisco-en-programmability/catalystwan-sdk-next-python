==============================
dca.statistics.settings.status
==============================


Operation: POST /dataservice/dca/statistics/settings/status
-----------------------------------------------------------


Get statistics setting status

.. code:: python

    def get_stats_db_index_status(
        payload: Optional[Any] = None,
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
        client.dca.statistics.settings.status.get_stats_db_index_status()


