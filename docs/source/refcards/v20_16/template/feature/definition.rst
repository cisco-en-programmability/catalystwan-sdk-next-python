===========================
template.feature.definition
===========================


Operation: GET /dataservice/template/feature/definition/{templateId}
--------------------------------------------------------------------


Get the configured template definition for given template Id<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

.. code:: python

    def get(template_id: str) -> Any: ...


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
        client.template.feature.definition.get()


