====================
admin.user.lock_user
====================


Operation: PUT /dataservice/admin/user/lockUser/{userName}
----------------------------------------------------------


Lock a user account

.. code:: python

    def lock_user(
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
        client.admin.user.lock_user.lock_user()


