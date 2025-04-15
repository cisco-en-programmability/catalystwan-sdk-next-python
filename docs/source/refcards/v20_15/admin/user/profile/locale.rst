=========================
admin.user.profile.locale
=========================


Operation: PUT /dataservice/admin/user/profile/locale
-----------------------------------------------------


Update profile locale

.. code:: python

    def put(payload: Any) -> None: ...


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
        client.admin.user.profile.locale.put()


