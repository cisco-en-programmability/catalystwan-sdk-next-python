======================
template.feature.types
======================


Operation: GET /dataservice/template/feature/types
--------------------------------------------------


Generate template types<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

.. code:: python

    def generate_template_types(type_: TypeParam) -> List[Any]: ...


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
        client.template.feature.types.generate_template_types()


.. toctree::
    :maxdepth: 1

    definition
    models

