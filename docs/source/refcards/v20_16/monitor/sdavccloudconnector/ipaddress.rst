=====================================
monitor.sdavccloudconnector.ipaddress
=====================================


Operation: GET /dataservice/monitor/sdavccloudconnector/ipaddress
-----------------------------------------------------------------


Get SD AVC App Rules based on IP Address for O365

.. code:: python

    def get_cloud_connector_ip_address_app_rules() -> Any: ...


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
        client.monitor.sdavccloudconnector.ipaddress.get_cloud_connector_ip_address_app_rules()


