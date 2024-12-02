=============
device.config
=============


Operation: GET /dataservice/device/config
-----------------------------------------


Get device running configuration

.. code:: python

    def get_device_running_config(device_id: List[str]) -> str: ...


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
        client.device.config.get_device_running_config()


.. toctree::
    :maxdepth: 1

    html

