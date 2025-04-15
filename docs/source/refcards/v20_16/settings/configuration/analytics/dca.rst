====================================
settings.configuration.analytics.dca
====================================


Operation: POST /dataservice/settings/configuration/analytics/dca
-----------------------------------------------------------------


Create analytics data file

.. code:: python

    def post() -> str: ...


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
        client.settings.configuration.analytics.dca.post()


