===============
device.keyvalue
===============


Operation: GET /dataservice/device/keyvalue
-------------------------------------------


Get vEdge inventory as key value (key as systemIp value as hostName)

.. code:: python

    def get_device_list_as_key_value(
        site_id: Optional[str] = None,
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
        client.device.keyvalue.get_device_list_as_key_value()


