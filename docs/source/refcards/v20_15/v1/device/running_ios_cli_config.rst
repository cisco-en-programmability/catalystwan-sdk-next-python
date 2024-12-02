================================
v1.device.running_ios_cli_config
================================


Operation: GET /dataservice/v1/device/runningIosCliConfig/{deviceUUID}
----------------------------------------------------------------------


Get Running iOS CLI Config for device

.. code:: python

    def get_running_ios_cli_config(device_uuid: str) -> str: ...


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
        client.v1.device.running_ios_cli_config.get_running_ios_cli_config()


