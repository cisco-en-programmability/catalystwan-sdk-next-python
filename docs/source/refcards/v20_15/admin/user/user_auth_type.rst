=========================
admin.user.user_auth_type
=========================


Operation: GET /dataservice/admin/user/userAuthType
---------------------------------------------------


Find user authentication type, whether it is SAML enabled

.. code:: python

    def find_user_auth_type_1() -> Any: ...


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
        client.admin.user.user_auth_type.find_user_auth_type_1()


