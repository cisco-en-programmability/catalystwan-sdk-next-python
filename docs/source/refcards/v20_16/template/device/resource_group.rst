==============================
template.device.resource_group
==============================


Operation: POST /dataservice/template/device/resource-group/{resourceGroupName}/{templateId}
--------------------------------------------------------------------------------------------


Change template resource group

.. code:: python

    def change_template_resource_group_1(
        template_id: str, resource_group_name: str
    ) -> None: ...


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
        client.template.device.resource_group.change_template_resource_group_1()


