==========
admin.user
==========


Operation: GET /dataservice/admin/user
--------------------------------------


Get all users

.. code:: python

    def find_users_1() -> List[Any]: ...


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
        client.admin.user.find_users_1()


Operation: POST /dataservice/admin/user
---------------------------------------


Create a user

.. code:: python

    def create_user_1(payload: Optional[Any] = None) -> None: ...


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
        client.admin.user.create_user_1()


Operation: PUT /dataservice/admin/user/{userName}
-------------------------------------------------


Update user

.. code:: python

    def update_user_1(
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
        client.admin.user.update_user_1()


Operation: DELETE /dataservice/admin/user/{userName}
----------------------------------------------------


Delete user

.. code:: python

    def delete_user_1(user_name: str) -> None: ...


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
        client.admin.user.delete_user_1()


.. toctree::
    :maxdepth: 1

    active_sessions
    admin/index
    lock_user
    password/index
    profile/index
    remove_sessions
    reset
    role
    user_auth_type

