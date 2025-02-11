===========================
sdavc.cloudconnector.status
===========================


Operation: GET /dataservice/sdavc/cloudconnector/status
-------------------------------------------------------


Get SD_AVC Cloud Connector Status

.. code:: python

    def get_cloud_connector_status() -> Any: ...


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
        client.sdavc.cloudconnector.status.get_cloud_connector_status()


