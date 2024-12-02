============================================
template.device.config.duplicatelocationname
============================================


Operation: POST /dataservice/template/device/config/duplicatelocationname
-------------------------------------------------------------------------


Detects duplicate system IP from a list of devices<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

.. code:: python

    def get_devices_with_duplicate_location_name(
        payload: Optional[Any] = None,
    ) -> List[Any]: ...


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
        client.template.device.config.duplicatelocationname.get_devices_with_duplicate_location_name()


