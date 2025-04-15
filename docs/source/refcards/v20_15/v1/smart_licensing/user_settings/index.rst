================================
v1.smart_licensing.user_settings
================================


Operation: GET /dataservice/v1/smart-licensing/user-settings
------------------------------------------------------------


Get smart licensing user settings

.. code:: python

    def get() -> UserSettingsResponse: ...


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
        client.v1.smart_licensing.user_settings.get()


.. toctree::
    :maxdepth: 1

    models

