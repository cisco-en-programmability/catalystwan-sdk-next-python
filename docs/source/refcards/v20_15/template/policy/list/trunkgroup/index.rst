===============================
template.policy.list.trunkgroup
===============================


Operation: GET /dataservice/template/policy/list/trunkgroup
-----------------------------------------------------------


Get policy lists

.. code:: python

    def get_policy_lists_35() -> List[Any]: ...


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
        client.template.policy.list.trunkgroup.get_policy_lists_35()


Operation: POST /dataservice/template/policy/list/trunkgroup
------------------------------------------------------------


Create policy list

.. code:: python

    def create_policy_list_38(payload: Optional[Any] = None) -> Any: ...


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
        client.template.policy.list.trunkgroup.create_policy_list_38()


Operation: DELETE /dataservice/template/policy/list/trunkgroup
--------------------------------------------------------------


Delete policy lists with specific info tag

.. code:: python

    def delete_policy_lists_with_info_tag_38(
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
        client.template.policy.list.trunkgroup.delete_policy_lists_with_info_tag_38()


Operation: GET /dataservice/template/policy/list/trunkgroup/{id}
----------------------------------------------------------------


Get a specific policy list based on the id

.. code:: python

    def get_lists_by_id_38(id: str) -> Any: ...


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
        client.template.policy.list.trunkgroup.get_lists_by_id_38()


Operation: PUT /dataservice/template/policy/list/trunkgroup/{id}
----------------------------------------------------------------


Edit policy list entries for a specific type of policy list

.. code:: python

    def edit_policy_list_38(
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
        client.template.policy.list.trunkgroup.edit_policy_list_38()


Operation: DELETE /dataservice/template/policy/list/trunkgroup/{id}
-------------------------------------------------------------------


Delete policy list entry for a specific type of policy list

.. code:: python

    def delete_policy_list_38(id: str) -> None: ...


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
        client.template.policy.list.trunkgroup.delete_policy_list_38()


.. toctree::
    :maxdepth: 1

    filtered
    preview

