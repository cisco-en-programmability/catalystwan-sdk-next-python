===============
admin.usergroup
===============


Operation: GET /dataservice/admin/usergroup
-------------------------------------------


Get all user groups

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
        client.admin.usergroup.get()


Operation: POST /dataservice/admin/usergroup
--------------------------------------------


Create user group

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
        client.admin.usergroup.post()


Operation: PUT /dataservice/admin/usergroup/{userGroupId}
---------------------------------------------------------


Update user group

.. code:: python

    def put(user_group_id: str, payload: Any) -> None: ...


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
        client.admin.usergroup.put()


Operation: DELETE /dataservice/admin/usergroup/{userGroupId}
------------------------------------------------------------


Delete user group

.. code:: python

    def delete(user_group_id: str) -> None: ...


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
        client.admin.usergroup.delete()


.. toctree::
    :maxdepth: 1

    definition
    keyvalue

