======================================
template.policy.list.expandedcommunity
======================================


Operation: GET /dataservice/template/policy/list/expandedcommunity
------------------------------------------------------------------


Get policy lists

.. code:: python

    def get_policy_lists_10() -> List[Any]: ...


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
        client.template.policy.list.expandedcommunity.get_policy_lists_10()


Operation: POST /dataservice/template/policy/list/expandedcommunity
-------------------------------------------------------------------


Create policy list

.. code:: python

    def create_policy_list_11(payload: Optional[Any] = None) -> Any: ...


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
        client.template.policy.list.expandedcommunity.create_policy_list_11()


Operation: DELETE /dataservice/template/policy/list/expandedcommunity
---------------------------------------------------------------------


Delete policy lists with specific info tag

.. code:: python

    def delete_policy_lists_with_info_tag_11(
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
        client.template.policy.list.expandedcommunity.delete_policy_lists_with_info_tag_11()


Operation: GET /dataservice/template/policy/list/expandedcommunity/{id}
-----------------------------------------------------------------------


Get a specific policy list based on the id

.. code:: python

    def get_lists_by_id_11(id: str) -> Any: ...


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
        client.template.policy.list.expandedcommunity.get_lists_by_id_11()


Operation: PUT /dataservice/template/policy/list/expandedcommunity/{id}
-----------------------------------------------------------------------


Edit policy list entries for a specific type of policy list

.. code:: python

    def edit_policy_list_11(
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
        client.template.policy.list.expandedcommunity.edit_policy_list_11()


Operation: DELETE /dataservice/template/policy/list/expandedcommunity/{id}
--------------------------------------------------------------------------


Delete policy list entry for a specific type of policy list

.. code:: python

    def delete_policy_list_11(id: str) -> None: ...


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
        client.template.policy.list.expandedcommunity.delete_policy_list_11()


.. toctree::
    :maxdepth: 1

    filtered
    preview

