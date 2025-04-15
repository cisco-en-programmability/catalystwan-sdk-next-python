===============================
template.feature.resource_group
===============================


Operation: POST /dataservice/template/feature/resource-group/{resourceGroupName}/{templateId}
---------------------------------------------------------------------------------------------


Change template resource group

.. code:: python

    def post(template_id: str, resource_group_name: str) -> None: ...


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
        client.template.feature.resource_group.post()


