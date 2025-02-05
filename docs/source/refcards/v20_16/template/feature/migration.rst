==========================
template.feature.migration
==========================


Operation: GET /dataservice/template/feature/migration
------------------------------------------------------


Generate a list of templates which require migration<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

.. code:: python

    def get_template_for_migration() -> List[Any]: ...


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
        client.template.feature.migration.get_template_for_migration()


