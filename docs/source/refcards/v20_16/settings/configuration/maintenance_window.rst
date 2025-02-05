=========================================
settings.configuration.maintenance_window
=========================================


Operation: GET /dataservice/settings/configuration/maintenanceWindow
--------------------------------------------------------------------


Retrieve maintenance window

.. code:: python

    def get_maintenance_window() -> str: ...


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
        client.settings.configuration.maintenance_window.get_maintenance_window()


