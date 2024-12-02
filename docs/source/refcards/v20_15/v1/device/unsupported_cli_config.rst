================================
v1.device.unsupported_cli_config
================================


Operation: GET /dataservice/v1/device/unsupportedCliConfig/{deviceUUID}
-----------------------------------------------------------------------


Get Unsupported CLI Config for device

.. code:: python

    def get_unsupported_cli_config(
        device_uuid: str,
        highlight_unsupported_clis: Optional[bool] = True,
    ) -> str: ...


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
        client.v1.device.unsupported_cli_config.get_unsupported_cli_config()


