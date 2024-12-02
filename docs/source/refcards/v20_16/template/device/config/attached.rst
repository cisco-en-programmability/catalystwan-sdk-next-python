===============================
template.device.config.attached
===============================


Operation: GET /dataservice/template/device/config/attached/{masterTemplateId}
------------------------------------------------------------------------------


Get attached device list by master template Id<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

.. code:: python

    def get_attached_device_list(
        master_template_id: str,
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
        client.template.device.config.attached.get_attached_device_list()


