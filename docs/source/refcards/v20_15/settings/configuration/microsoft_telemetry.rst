==========================================
settings.configuration.microsoft_telemetry
==========================================


Operation: GET /dataservice/settings/configuration/microsoftTelemetry
---------------------------------------------------------------------


Deprecated!!!

Retrieve Microsoft telemetry configuration value

.. code:: python

    def get() -> Any: ...


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
        client.settings.configuration.microsoft_telemetry.get()


Operation: PUT /dataservice/settings/configuration/microsoftTelemetry
---------------------------------------------------------------------


Deprecated!!!

Update Microsoft telemetry configuration setting

.. code:: python

    def put(payload: str) -> Any: ...


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
        client.settings.configuration.microsoft_telemetry.put()


Operation: POST /dataservice/settings/configuration/microsoftTelemetry
----------------------------------------------------------------------


Deprecated!!!

Add new Microsoft telemetry configuration

.. code:: python

    def post(payload: str) -> str: ...


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
        client.settings.configuration.microsoft_telemetry.post()


