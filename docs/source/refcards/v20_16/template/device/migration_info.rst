==============================
template.device.migration_info
==============================


Operation: GET /dataservice/template/device/migration_info
----------------------------------------------------------


Returns the mapping between old and migrated templates<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

.. code:: python

    def migration_info() -> Any: ...


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
        client.template.device.migration_info.migration_info()


