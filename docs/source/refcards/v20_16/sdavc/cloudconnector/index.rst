====================
sdavc.cloudconnector
====================


Operation: GET /dataservice/sdavc/cloudconnector
------------------------------------------------


Get SD_AVC Cloud Connector Config

.. code:: python

    def get_cloud_connector() -> Any: ...


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
        client.sdavc.cloudconnector.get_cloud_connector()


Operation: PUT /dataservice/sdavc/cloudconnector
------------------------------------------------


Disable SD_AVC Cloud Connector

.. code:: python

    def disable_cloud_connector(
        payload: Optional[DisableCloudConnectorPutRequest] = None,
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
        client.sdavc.cloudconnector.disable_cloud_connector()


Operation: POST /dataservice/sdavc/cloudconnector
-------------------------------------------------


Enable SD_AVC Cloud Connector

.. code:: python

    def enable_cloud_connector(
        payload: Optional[DisableCloudConnectorPutRequest] = None,
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
        client.sdavc.cloudconnector.enable_cloud_connector()


.. toctree::
    :maxdepth: 1

    status
    models

