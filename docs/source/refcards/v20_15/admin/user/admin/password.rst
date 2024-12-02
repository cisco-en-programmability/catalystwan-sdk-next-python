=========================
admin.user.admin.password
=========================


Operation: POST /dataservice/admin/user/admin/password
------------------------------------------------------


Update admin default password

.. code:: python

    def update_admin_password_1(
        payload: Optional[Any] = None,
    ) -> None: ...


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
        client.admin.user.admin.password.update_admin_password_1()


