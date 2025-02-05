===========================
admin.user.profile.password
===========================


Operation: PUT /dataservice/admin/user/profile/password
-------------------------------------------------------


Update profile password

.. code:: python

    def update_profile_password_1(
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
        client.admin.user.profile.password.update_profile_password_1()


