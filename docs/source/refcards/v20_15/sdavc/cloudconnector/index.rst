====================
sdavc.cloudconnector
====================


Operation: GET /dataservice/sdavc/cloudconnector
------------------------------------------------


Get SD_AVC Cloud Connector Config

.. code:: python

    def get() -> Any: ...


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
        client.sdavc.cloudconnector.get()


Operation: PUT /dataservice/sdavc/cloudconnector
------------------------------------------------


Disable SD_AVC Cloud Connector

.. code:: python

    def put(payload: DisableCloudConnectorPutRequest) -> Any: ...


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
        client.sdavc.cloudconnector.put()


Operation: POST /dataservice/sdavc/cloudconnector
-------------------------------------------------


Enable SD_AVC Cloud Connector

.. code:: python

    def post(payload: EnableCloudConnectorPostRequest) -> Any: ...


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
        client.sdavc.cloudconnector.post()


.. toctree::
    :maxdepth: 1

    status
    models

