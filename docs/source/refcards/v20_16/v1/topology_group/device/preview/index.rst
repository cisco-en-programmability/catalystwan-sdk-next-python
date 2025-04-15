================================
v1.topology_group.device.preview
================================


Operation: POST /dataservice/v1/topology-group/{topologyGroupId}/device/{deviceId}/preview
------------------------------------------------------------------------------------------


Get a preview of the configuration for a device

.. code:: python

    def post(
        topology_group_id: str,
        device_id: str,
        payload: GetTopologyGroupDeviceConfigurationPreviewPostRequest,
    ) -> GetTopologyGroupDeviceConfigurationPreviewPostResponse: ...


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
        client.v1.topology_group.device.preview.post()


.. toctree::
    :maxdepth: 1

    models

