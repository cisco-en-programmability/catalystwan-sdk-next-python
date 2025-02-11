==============================
multicloud.cloudgatewaysetting
==============================


Operation: GET /dataservice/multicloud/cloudgatewaysetting/{cloudGatewayName}
-----------------------------------------------------------------------------


Get cloud gateway custom setting by cloud gateway name

.. code:: python

    def get_cgw_custom_setting_details(
        cloud_gateway_name: str,
    ) -> CustomSettings: ...


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
        client.multicloud.cloudgatewaysetting.get_cgw_custom_setting_details()


.. toctree::
    :maxdepth: 1

    models

