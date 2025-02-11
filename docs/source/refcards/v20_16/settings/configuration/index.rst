======================
settings.configuration
======================


Operation: GET /dataservice/settings/configuration/{type}
---------------------------------------------------------


Retrieve configuration value by type

.. code:: python

    def get_configuration_by_setting_type(type_: str) -> str: ...


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
        client.settings.configuration.get_configuration_by_setting_type()


Operation: PUT /dataservice/settings/configuration/{type}
---------------------------------------------------------


Update configuration setting

.. code:: python

    def edit_configuration(
        type_: str, payload: Optional[Any] = None
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
        client.settings.configuration.edit_configuration()


Operation: POST /dataservice/settings/configuration/{type}
----------------------------------------------------------


Add new certificate configuration

.. code:: python

    def new_configuration(
        type_: str, payload: Optional[Any] = None
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
        client.settings.configuration.new_configuration()


.. toctree::
    :maxdepth: 1

    analytics/index
    certificate
    cloudx
    google_map_key
    maintenance_window
    microsoft_telemetry
    wani

