=======================
template.feature.object
=======================


Operation: GET /dataservice/template/feature/object/{templateId}
----------------------------------------------------------------


Get template object definition for given template Id<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

.. code:: python

    def get_general_template(template_id: str) -> Any: ...


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
        client.template.feature.object.get_general_template()


