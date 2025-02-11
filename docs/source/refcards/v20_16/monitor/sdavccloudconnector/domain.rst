==================================
monitor.sdavccloudconnector.domain
==================================


Operation: GET /dataservice/monitor/sdavccloudconnector/domain
--------------------------------------------------------------


Get SD AVC App Rules based on Domain for O365

.. code:: python

    def get_cloud_connector_domain_app_rules() -> Any: ...


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
        client.monitor.sdavccloudconnector.domain.get_cloud_connector_domain_app_rules()


