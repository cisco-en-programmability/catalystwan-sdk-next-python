==============
health.devices
==============


Operation: GET /dataservice/health/devices
------------------------------------------


get the devices health properties

.. code:: python

    def get_devices_health(
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        sort_by: Optional[str] = None,
        sort_order: Optional[str] = None,
        starting_device_id: Optional[str] = None,
        site_id: Optional[str] = None,
        group_id: Optional[str] = None,
        vpn_id: Optional[str] = None,
        reachable: Optional[bool] = None,
        control_status: Optional[str] = None,
        personality: Optional[str] = None,
        health: Optional[str] = None,
        feature_type: Optional[FeatureTypeParam] = None,
        cor_saas_status: Optional[bool] = None,
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
        client.health.devices.get_devices_health()


.. toctree::
    :maxdepth: 1

    overview
    models

