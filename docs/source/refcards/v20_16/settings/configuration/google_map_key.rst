=====================================
settings.configuration.google_map_key
=====================================


Operation: GET /dataservice/settings/configuration/googleMapKey
---------------------------------------------------------------


Retrieve Google map key

.. code:: python

    def get_google_map_key() -> str: ...


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
        client.settings.configuration.google_map_key.get_google_map_key()


