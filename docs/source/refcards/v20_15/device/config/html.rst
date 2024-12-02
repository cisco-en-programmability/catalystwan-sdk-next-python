==================
device.config.html
==================


Operation: GET /dataservice/device/config/html
----------------------------------------------


Deprecated!!!

Get device running configuration in HTML format

.. code:: python

    def get_device_running_config_html(device_id: List[str]) -> str: ...


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
        client.device.config.html.get_device_running_config_html()


