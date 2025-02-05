===================================
template.policy.list.dataipv6prefix
===================================


Operation: GET /dataservice/template/policy/list/dataipv6prefix
---------------------------------------------------------------


Get policy lists

.. code:: python

    def get_policy_lists_8() -> List[Any]: ...


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
        client.template.policy.list.dataipv6prefix.get_policy_lists_8()


Operation: POST /dataservice/template/policy/list/dataipv6prefix
----------------------------------------------------------------


Create policy list

.. code:: python

    def create_policy_list_8(payload: Optional[Any] = None) -> Any: ...


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
        client.template.policy.list.dataipv6prefix.create_policy_list_8()


Operation: DELETE /dataservice/template/policy/list/dataipv6prefix
------------------------------------------------------------------


Delete policy lists with specific info tag

.. code:: python

    def delete_policy_lists_with_info_tag_8(
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
        client.template.policy.list.dataipv6prefix.delete_policy_lists_with_info_tag_8()


Operation: GET /dataservice/template/policy/list/dataipv6prefix/{id}
--------------------------------------------------------------------


Get a specific policy list based on the id

.. code:: python

    def get_lists_by_id_8(id: str) -> Any: ...


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
        client.template.policy.list.dataipv6prefix.get_lists_by_id_8()


Operation: PUT /dataservice/template/policy/list/dataipv6prefix/{id}
--------------------------------------------------------------------


Edit policy list entries for a specific type of policy list

.. code:: python

    def edit_policy_list_8(
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
        client.template.policy.list.dataipv6prefix.edit_policy_list_8()


Operation: DELETE /dataservice/template/policy/list/dataipv6prefix/{id}
-----------------------------------------------------------------------


Delete policy list entry for a specific type of policy list

.. code:: python

    def delete_policy_list_8(id: str) -> None: ...


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
        client.template.policy.list.dataipv6prefix.delete_policy_list_8()


.. toctree::
    :maxdepth: 1

    filtered
    preview

