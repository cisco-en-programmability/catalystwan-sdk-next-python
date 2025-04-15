==============================
dca.statistics.settings.status
==============================


Operation: POST /dataservice/dca/statistics/settings/status
-----------------------------------------------------------


Get statistics setting status

.. code:: python

    def post(payload: Any) -> Any: ...


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
        client.dca.statistics.settings.status.post()


