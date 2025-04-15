======================
settings.configuration
======================


Operation: GET /dataservice/settings/configuration/{type}
---------------------------------------------------------


Retrieve configuration value by type

.. code:: python

    def get(type_: str) -> str: ...


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
        client.settings.configuration.get()


Operation: PUT /dataservice/settings/configuration/{type}
---------------------------------------------------------


Update configuration setting

.. code:: python

    def put(type_: str, payload: Any) -> str: ...


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
        client.settings.configuration.put()


Operation: POST /dataservice/settings/configuration/{type}
----------------------------------------------------------


Add new certificate configuration

.. code:: python

    def post(type_: str, payload: Any) -> str: ...


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
        client.settings.configuration.post()


.. toctree::
    :maxdepth: 1

    analytics/index
    certificate
    cloudx
    google_map_key
    maintenance_window
    microsoft_telemetry
    wani

