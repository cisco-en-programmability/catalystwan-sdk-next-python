=======================
health.devices.overview
=======================


Operation: GET /dataservice/health/devices/overview
---------------------------------------------------


gets devices health overview

.. code:: python

    def get_devices_health_overview(
        vpn_id: Optional[str] = None,
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
        client.health.devices.overview.get_devices_health_overview()


