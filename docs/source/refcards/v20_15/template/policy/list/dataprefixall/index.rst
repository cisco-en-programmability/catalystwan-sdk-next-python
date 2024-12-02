==================================
template.policy.list.dataprefixall
==================================


Operation: GET /dataservice/template/policy/list/dataprefixall
--------------------------------------------------------------


Get policy lists for all data prefixes

.. code:: python

    def get_lists_for_all_data_prefixes() -> List[Any]: ...


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
        client.template.policy.list.dataprefixall.get_lists_for_all_data_prefixes()


Operation: POST /dataservice/template/policy/list/dataprefixall
---------------------------------------------------------------


Create policy list

.. code:: python

    def create_policy_list_9(payload: Optional[Any] = None) -> Any: ...


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
        client.template.policy.list.dataprefixall.create_policy_list_9()


Operation: DELETE /dataservice/template/policy/list/dataprefixall
-----------------------------------------------------------------


Delete policy lists with specific info tag

.. code:: python

    def delete_policy_lists_with_info_tag_9(
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
        client.template.policy.list.dataprefixall.delete_policy_lists_with_info_tag_9()


Operation: GET /dataservice/template/policy/list/dataprefixall/{id}
-------------------------------------------------------------------


Get a specific policy list based on the id

.. code:: python

    def get_lists_by_id_9(id: str) -> Any: ...


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
        client.template.policy.list.dataprefixall.get_lists_by_id_9()


Operation: PUT /dataservice/template/policy/list/dataprefixall/{id}
-------------------------------------------------------------------


Edit policy list entries for a specific type of policy list

.. code:: python

    def edit_policy_list_9(
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
        client.template.policy.list.dataprefixall.edit_policy_list_9()


Operation: DELETE /dataservice/template/policy/list/dataprefixall/{id}
----------------------------------------------------------------------


Delete policy list entry for a specific type of policy list

.. code:: python

    def delete_policy_list_9(id: str) -> None: ...


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
        client.template.policy.list.dataprefixall.delete_policy_list_9()


.. toctree::
    :maxdepth: 1

    filtered
    preview

