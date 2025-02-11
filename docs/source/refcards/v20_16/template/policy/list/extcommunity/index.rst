=================================
template.policy.list.extcommunity
=================================


Operation: GET /dataservice/template/policy/list/extcommunity
-------------------------------------------------------------


Get policy lists

.. code:: python

    def get_policy_lists_11() -> List[Any]: ...


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
        client.template.policy.list.extcommunity.get_policy_lists_11()


Operation: POST /dataservice/template/policy/list/extcommunity
--------------------------------------------------------------


Create policy list

.. code:: python

    def create_policy_list_12(payload: Optional[Any] = None) -> Any: ...


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
        client.template.policy.list.extcommunity.create_policy_list_12()


Operation: DELETE /dataservice/template/policy/list/extcommunity
----------------------------------------------------------------


Delete policy lists with specific info tag

.. code:: python

    def delete_policy_lists_with_info_tag_12(
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
        client.template.policy.list.extcommunity.delete_policy_lists_with_info_tag_12()


Operation: GET /dataservice/template/policy/list/extcommunity/{id}
------------------------------------------------------------------


Get a specific policy list based on the id

.. code:: python

    def get_lists_by_id_12(id: str) -> Any: ...


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
        client.template.policy.list.extcommunity.get_lists_by_id_12()


Operation: PUT /dataservice/template/policy/list/extcommunity/{id}
------------------------------------------------------------------


Edit policy list entries for a specific type of policy list

.. code:: python

    def edit_policy_list_12(
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
        client.template.policy.list.extcommunity.edit_policy_list_12()


Operation: DELETE /dataservice/template/policy/list/extcommunity/{id}
---------------------------------------------------------------------


Delete policy list entry for a specific type of policy list

.. code:: python

    def delete_policy_list_12(id: str) -> None: ...


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
        client.template.policy.list.extcommunity.delete_policy_list_12()


.. toctree::
    :maxdepth: 1

    filtered
    preview

