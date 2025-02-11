=========================
template.device.migration
=========================


Operation: GET /dataservice/template/device/migration
-----------------------------------------------------


Generate a list of templates which require migration<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

.. code:: python

    def generate_template_for_migration(
        has_aaa: Optional[bool] = None,
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
        client.template.device.migration.generate_template_for_migration()


Operation: POST /dataservice/template/device/migration
------------------------------------------------------


Migrate the device templates given the template Ids

.. code:: python

    def migrate_templates(
        id: List[str],
        prefix: Optional[str] = "cisco",
        include_all: Optional[bool] = True,
    ) -> Any: ...


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
        client.template.device.migration.migrate_templates()


