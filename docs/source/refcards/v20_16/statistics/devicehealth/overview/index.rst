================================
statistics.devicehealth.overview
================================


Operation: GET /dataservice/statistics/devicehealth/overview/{type}
-------------------------------------------------------------------


Get all device health overview

.. code:: python

    def get_device_health_overview(
        type_: str,
        last_n_hours: Optional[int] = 12,
        site: Optional[str] = None,
        personality: Optional[PersonalityParam] = "vedge",
        limit: Optional[int] = 30,
    ) -> DeviceHealthOverview: ...


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
        client.statistics.devicehealth.overview.get_device_health_overview()


.. toctree::
    :maxdepth: 1

    models

