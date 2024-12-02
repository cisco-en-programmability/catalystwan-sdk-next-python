==============================
v1.config_group.device.preview
==============================


Operation: POST /dataservice/v1/config-group/{configGroupId}/device/{deviceId}/preview
--------------------------------------------------------------------------------------


Get a preview of the configuration for a device

.. code:: python

    def get_config_group_device_configuration_preview(
        config_group_id: str,
        device_id: str,
        payload: Optional[
            GetConfigGroupDeviceConfigurationPreviewPostRequest
        ] = None,
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
        client.v1.config_group.device.preview.get_config_group_device_configuration_preview()


.. toctree::
    :maxdepth: 1

    models

