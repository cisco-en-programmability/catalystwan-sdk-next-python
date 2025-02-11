=====================================
template.device.is_migration_required
=====================================


Operation: GET /dataservice/template/device/is_migration_required
-----------------------------------------------------------------


Check if any device templates need migration<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

.. code:: python

    def is_migration_required() -> Any: ...


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
        client.template.device.is_migration_required.is_migration_required()


