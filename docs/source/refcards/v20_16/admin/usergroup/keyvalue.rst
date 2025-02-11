========================
admin.usergroup.keyvalue
========================


Operation: GET /dataservice/admin/usergroup/keyvalue
----------------------------------------------------


Get user groups as key value map

.. code:: python

    def find_user_groups_as_key_value() -> List[Any]: ...


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
        client.admin.usergroup.keyvalue.find_user_groups_as_key_value()


