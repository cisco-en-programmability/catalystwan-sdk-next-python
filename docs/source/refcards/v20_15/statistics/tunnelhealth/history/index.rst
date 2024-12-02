===============================
statistics.tunnelhealth.history
===============================


Operation: GET /dataservice/statistics/tunnelhealth/history
-----------------------------------------------------------


Get all tunnel health history

.. code:: python

    def statistics_approute_tunnelhealth_history_get(
        last_n_hours: Optional[int] = 12,
        site: Optional[str] = None,
        limit: Optional[int] = 30,
    ) -> List[TunnelHealthHistoryItem]: ...


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
        client.statistics.tunnelhealth.history.statistics_approute_tunnelhealth_history_get()


.. toctree::
    :maxdepth: 1

    models

