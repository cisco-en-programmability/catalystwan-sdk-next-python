============================
admin.user.password.validate
============================


Operation: POST /dataservice/admin/user/password/validate
---------------------------------------------------------


Deprecated!!!

Validate user password

.. code:: python

    def post(payload: Any) -> None: ...


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
        client.admin.user.password.validate.post()


