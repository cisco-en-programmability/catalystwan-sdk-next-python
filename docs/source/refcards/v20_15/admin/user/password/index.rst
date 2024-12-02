===================
admin.user.password
===================


Operation: PUT /dataservice/admin/user/password/{userName}
----------------------------------------------------------


Update user password

.. code:: python

    def update_password_1(
        user_name: str, payload: Optional[Any] = None
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
        client.admin.user.password.update_password_1()


.. toctree::
    :maxdepth: 1

    validate

