============================
statistics.sitehealth.common
============================


Operation: GET /dataservice/statistics/sitehealth/common
--------------------------------------------------------


Get all site health

.. code:: python

    def get_site_health(
        is_heat_map: Optional[str] = "false",
        last_n_hours: Optional[int] = None,
        interval: Optional[int] = 30,
        health: Optional[HealthParam] = None,
        start_time: Optional[int] = None,
        end_time: Optional[int] = None,
        include_details: Optional[str] = "false",
        include_region: Optional[str] = "false",
        region_name: Optional[str] = None,
        device_type: Optional[DeviceTypeParam] = None,
    ) -> List[SiteHealthItem]: ...


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
        client.statistics.sitehealth.common.get_site_health()


.. toctree::
    :maxdepth: 1

    models

