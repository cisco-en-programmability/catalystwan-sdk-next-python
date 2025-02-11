================================
template.policy.list.ipprefixall
================================


Operation: GET /dataservice/template/policy/list/ipprefixall
------------------------------------------------------------


Get lists for all prefixes

.. code:: python

    def get_lists_for_all_prefixes() -> List[Any]: ...


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
        client.template.policy.list.ipprefixall.get_lists_for_all_prefixes()


Operation: POST /dataservice/template/policy/list/ipprefixall
-------------------------------------------------------------


Create policy list

.. code:: python

    def create_policy_list_21(payload: Optional[Any] = None) -> Any: ...


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
        client.template.policy.list.ipprefixall.create_policy_list_21()


Operation: DELETE /dataservice/template/policy/list/ipprefixall
---------------------------------------------------------------


Delete policy lists with specific info tag

.. code:: python

    def delete_policy_lists_with_info_tag_21(
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
        client.template.policy.list.ipprefixall.delete_policy_lists_with_info_tag_21()


Operation: GET /dataservice/template/policy/list/ipprefixall/{id}
-----------------------------------------------------------------


Get a specific policy list based on the id

.. code:: python

    def get_lists_by_id_21(id: str) -> Any: ...


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
        client.template.policy.list.ipprefixall.get_lists_by_id_21()


Operation: PUT /dataservice/template/policy/list/ipprefixall/{id}
-----------------------------------------------------------------


Edit policy list entries for a specific type of policy list

.. code:: python

    def edit_policy_list_21(
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
        client.template.policy.list.ipprefixall.edit_policy_list_21()


Operation: DELETE /dataservice/template/policy/list/ipprefixall/{id}
--------------------------------------------------------------------


Delete policy list entry for a specific type of policy list

.. code:: python

    def delete_policy_list_21(id: str) -> None: ...


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
        client.template.policy.list.ipprefixall.delete_policy_list_21()


.. toctree::
    :maxdepth: 1

    filtered
    preview

