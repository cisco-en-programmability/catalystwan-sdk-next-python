==================
multicloud.devices
==================


Operation: GET /dataservice/multicloud/devices/{cloudType}
----------------------------------------------------------


Get cloud devices by cloud type

.. code:: python

    def get_cloud_devices(
        cloud_type: CloudTypeParam,
        cloud_gateway_name: Optional[str] = None,
    ) -> DeviceInfoExtendedResponse: ...


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
        client.multicloud.devices.get_cloud_devices()


.. toctree::
    :maxdepth: 1

    edge
    models

