==========================
admin.usergroup.definition
==========================


Operation: GET /dataservice/admin/usergroup/definition
------------------------------------------------------


Get user groups in a grid table

.. code:: python

    def create_group_grid_columns() -> Any: ...


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
        client.admin.usergroup.definition.create_group_grid_columns()


