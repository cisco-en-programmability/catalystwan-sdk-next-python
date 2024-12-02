===============
admin.usergroup
===============


Operation: GET /dataservice/admin/usergroup
-------------------------------------------


Get all user groups

.. code:: python

    def find_user_groups() -> List[Any]: ...


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
        client.admin.usergroup.find_user_groups()


Operation: POST /dataservice/admin/usergroup
--------------------------------------------


Create user group

.. code:: python

    def create_user_group(payload: Optional[Any] = None) -> None: ...


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
        client.admin.usergroup.create_user_group()


Operation: PUT /dataservice/admin/usergroup/{userGroupId}
---------------------------------------------------------


Update user group

.. code:: python

    def update_user_group(
        user_group_id: str, payload: Optional[Any] = None
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
        client.admin.usergroup.update_user_group()


Operation: DELETE /dataservice/admin/usergroup/{userGroupId}
------------------------------------------------------------


Delete user group

.. code:: python

    def delete_user_group(user_group_id: str) -> None: ...


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
        client.admin.usergroup.delete_user_group()


.. toctree::
    :maxdepth: 1

    definition
    keyvalue

