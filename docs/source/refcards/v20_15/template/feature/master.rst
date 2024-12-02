=======================
template.feature.master
=======================


Operation: GET /dataservice/template/feature/master/{type_name}
---------------------------------------------------------------


Generate template type definition by device type<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

.. code:: python

    def generate_master_template_definition(type_name: str) -> Any: ...


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
        client.template.feature.master.generate_master_template_definition()


