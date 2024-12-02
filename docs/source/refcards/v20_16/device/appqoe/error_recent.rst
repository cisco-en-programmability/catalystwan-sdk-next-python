==========================
device.appqoe.error_recent
==========================


Operation: GET /dataservice/device/appqoe/error-recent
------------------------------------------------------


Get Appqoe error recent from device

.. code:: python

    def get_appqoe_error_recent(device_id: str) -> Any: ...


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
        client.device.appqoe.error_recent.get_appqoe_error_recent()


