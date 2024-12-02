==================
device.system.info
==================


Operation: GET /dataservice/device/system/info
----------------------------------------------


Get device information list

.. code:: python

    def create_device_info_list(device_id: List[str]) -> Any: ...


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
        client.device.system.info.create_device_info_list()


