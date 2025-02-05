==========================================
settings.configuration.microsoft_telemetry
==========================================


Operation: GET /dataservice/settings/configuration/microsoftTelemetry
---------------------------------------------------------------------


Deprecated!!!

Retrieve Microsoft telemetry configuration value

.. code:: python

    def get_microsoft_telemetry_configuration() -> Any: ...


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
        client.settings.configuration.microsoft_telemetry.get_microsoft_telemetry_configuration()


Operation: PUT /dataservice/settings/configuration/microsoftTelemetry
---------------------------------------------------------------------


Deprecated!!!

Update Microsoft telemetry configuration setting

.. code:: python

    def edit_microsoft_telemetry_configuration(
        payload: Optional[str] = None,
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
        client.settings.configuration.microsoft_telemetry.edit_microsoft_telemetry_configuration()


Operation: POST /dataservice/settings/configuration/microsoftTelemetry
----------------------------------------------------------------------


Deprecated!!!

Add new Microsoft telemetry configuration

.. code:: python

    def new_microsoft_telemetry_configuration(
        payload: Optional[str] = None,
    ) -> str: ...


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
        client.settings.configuration.microsoft_telemetry.new_microsoft_telemetry_configuration()


