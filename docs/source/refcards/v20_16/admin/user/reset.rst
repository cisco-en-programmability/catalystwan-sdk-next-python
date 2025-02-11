================
admin.user.reset
================


Operation: POST /dataservice/admin/user/reset
---------------------------------------------


Unlock a user

.. code:: python

    def reset_user_1(payload: Optional[Any] = None) -> None: ...


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
        client.admin.user.reset.reset_user_1()


