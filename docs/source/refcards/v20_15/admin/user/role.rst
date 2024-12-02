===============
admin.user.role
===============


Operation: GET /dataservice/admin/user/role
-------------------------------------------


Check whether a user has admin role

.. code:: python

    def find_user_role_1() -> Any: ...


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
        client.admin.user.role.find_user_role_1()


