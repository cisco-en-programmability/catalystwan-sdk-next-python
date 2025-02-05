============================
template.policy.list.policer
============================


Operation: GET /dataservice/template/policy/list/policer
--------------------------------------------------------


Get policy lists

.. code:: python

    def get_policy_lists_23() -> List[Any]: ...


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
        client.template.policy.list.policer.get_policy_lists_23()


Operation: POST /dataservice/template/policy/list/policer
---------------------------------------------------------


Create policy list

.. code:: python

    def create_policy_list_26(payload: Optional[Any] = None) -> Any: ...


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
        client.template.policy.list.policer.create_policy_list_26()


Operation: DELETE /dataservice/template/policy/list/policer
-----------------------------------------------------------


Delete policy lists with specific info tag

.. code:: python

    def delete_policy_lists_with_info_tag_26(
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
        client.template.policy.list.policer.delete_policy_lists_with_info_tag_26()


Operation: GET /dataservice/template/policy/list/policer/{id}
-------------------------------------------------------------


Get a specific policy list based on the id

.. code:: python

    def get_lists_by_id_26(id: str) -> Any: ...


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
        client.template.policy.list.policer.get_lists_by_id_26()


Operation: PUT /dataservice/template/policy/list/policer/{id}
-------------------------------------------------------------


Edit policy list entries for a specific type of policy list

.. code:: python

    def edit_policy_list_26(
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
        client.template.policy.list.policer.edit_policy_list_26()


Operation: DELETE /dataservice/template/policy/list/policer/{id}
----------------------------------------------------------------


Delete policy list entry for a specific type of policy list

.. code:: python

    def delete_policy_list_26(id: str) -> None: ...


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
        client.template.policy.list.policer.delete_policy_list_26()


.. toctree::
    :maxdepth: 1

    filtered
    preview

