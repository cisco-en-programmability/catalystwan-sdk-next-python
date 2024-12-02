===============================
template.policy.list.dataprefix
===============================


Operation: GET /dataservice/template/policy/list/dataprefix
-----------------------------------------------------------


Get policy lists

.. code:: python

    def get_policy_lists_9() -> List[Any]: ...


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
        client.template.policy.list.dataprefix.get_policy_lists_9()


Operation: POST /dataservice/template/policy/list/dataprefix
------------------------------------------------------------


Create policy list

.. code:: python

    def create_policy_list_10(payload: Optional[Any] = None) -> Any: ...


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
        client.template.policy.list.dataprefix.create_policy_list_10()


Operation: DELETE /dataservice/template/policy/list/dataprefix
--------------------------------------------------------------


Delete policy lists with specific info tag

.. code:: python

    def delete_policy_lists_with_info_tag_10(
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
        client.template.policy.list.dataprefix.delete_policy_lists_with_info_tag_10()


Operation: GET /dataservice/template/policy/list/dataprefix/{id}
----------------------------------------------------------------


Get a specific policy list based on the id

.. code:: python

    def get_lists_by_id_10(id: str) -> Any: ...


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
        client.template.policy.list.dataprefix.get_lists_by_id_10()


Operation: PUT /dataservice/template/policy/list/dataprefix/{id}
----------------------------------------------------------------


Edit policy list entries for a specific type of policy list

.. code:: python

    def edit_policy_list_10(
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
        client.template.policy.list.dataprefix.edit_policy_list_10()


Operation: DELETE /dataservice/template/policy/list/dataprefix/{id}
-------------------------------------------------------------------


Delete policy list entry for a specific type of policy list

.. code:: python

    def delete_policy_list_10(id: str) -> None: ...


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
        client.template.policy.list.dataprefix.delete_policy_list_10()


.. toctree::
    :maxdepth: 1

    filtered
    preview

