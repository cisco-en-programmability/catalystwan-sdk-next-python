==============================
template.policy.list.community
==============================


Operation: GET /dataservice/template/policy/list/community
----------------------------------------------------------


Get policy lists

.. code:: python

    def get_policy_lists_7() -> List[Any]: ...


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
        client.template.policy.list.community.get_policy_lists_7()


Operation: POST /dataservice/template/policy/list/community
-----------------------------------------------------------


Create policy list

.. code:: python

    def create_policy_list_7(payload: Optional[Any] = None) -> Any: ...


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
        client.template.policy.list.community.create_policy_list_7()


Operation: DELETE /dataservice/template/policy/list/community
-------------------------------------------------------------


Delete policy lists with specific info tag

.. code:: python

    def delete_policy_lists_with_info_tag_7(
        info_tag: Optional[str] = None,
    ) -> List[Any]: ...


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
        client.template.policy.list.community.delete_policy_lists_with_info_tag_7()


Operation: GET /dataservice/template/policy/list/community/{id}
---------------------------------------------------------------


Get a specific policy list based on the id

.. code:: python

    def get_lists_by_id_7(id: str) -> Any: ...


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
        client.template.policy.list.community.get_lists_by_id_7()


Operation: PUT /dataservice/template/policy/list/community/{id}
---------------------------------------------------------------


Edit policy list entries for a specific type of policy list

.. code:: python

    def edit_policy_list_7(
        id: str, payload: Optional[Any] = None
    ) -> Any: ...


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
        client.template.policy.list.community.edit_policy_list_7()


Operation: DELETE /dataservice/template/policy/list/community/{id}
------------------------------------------------------------------


Delete policy list entry for a specific type of policy list

.. code:: python

    def delete_policy_list_7(id: str) -> None: ...


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
        client.template.policy.list.community.delete_policy_list_7()


.. toctree::
    :maxdepth: 1

    filtered
    preview

