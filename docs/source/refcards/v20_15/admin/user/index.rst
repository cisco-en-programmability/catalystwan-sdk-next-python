==========
admin.user
==========


Operation: GET /dataservice/admin/user
--------------------------------------


Get all users

.. code:: python

    def get() -> List[Any]: ...


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
        client.admin.user.get()


Operation: POST /dataservice/admin/user
---------------------------------------


Create a user

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
        client.admin.user.post()


Operation: PUT /dataservice/admin/user/{userName}
-------------------------------------------------


Update user

.. code:: python

    def put(user_name: str, payload: Any) -> None: ...


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
        client.admin.user.put()


Operation: DELETE /dataservice/admin/user/{userName}
----------------------------------------------------


Delete user

.. code:: python

    def delete(user_name: str) -> None: ...


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
        client.admin.user.delete()


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

