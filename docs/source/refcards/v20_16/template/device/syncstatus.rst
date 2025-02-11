==========================
template.device.syncstatus
==========================


Operation: GET /dataservice/template/device/syncstatus
------------------------------------------------------


Get template sync status<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

.. code:: python

    def get_out_of_sync_templates() -> List[Any]: ...


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
        client.template.device.syncstatus.get_out_of_sync_templates()


Operation: GET /dataservice/template/device/syncstatus/{templateId}
-------------------------------------------------------------------


Get out of sync devices<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

.. code:: python

    def get_out_of_sync_devices(template_id: str) -> List[Any]: ...


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
        client.template.device.syncstatus.get_out_of_sync_devices()


