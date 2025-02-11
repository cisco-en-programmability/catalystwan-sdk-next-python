===================================
template.policy.list.dataprefixfqdn
===================================


Operation: GET /dataservice/template/policy/list/dataprefixfqdn
---------------------------------------------------------------


Get lists for all all data-prefix(IPv4) and Fqdn lists

.. code:: python

    def get_all_data_prefix_and_fqdn_lists() -> List[Any]: ...


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
        client.template.policy.list.dataprefixfqdn.get_all_data_prefix_and_fqdn_lists()


Operation: POST /dataservice/template/policy/list/dataprefixfqdn
----------------------------------------------------------------


Create policy list

.. code:: python

    def create_policy_list_15(payload: Optional[Any] = None) -> Any: ...


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
        client.template.policy.list.dataprefixfqdn.create_policy_list_15()


Operation: DELETE /dataservice/template/policy/list/dataprefixfqdn
------------------------------------------------------------------


Delete policy lists with specific info tag

.. code:: python

    def delete_policy_lists_with_info_tag_15(
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
        client.template.policy.list.dataprefixfqdn.delete_policy_lists_with_info_tag_15()


Operation: GET /dataservice/template/policy/list/dataprefixfqdn/{id}
--------------------------------------------------------------------


Get a specific policy list based on the id

.. code:: python

    def get_lists_by_id_15(id: str) -> Any: ...


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
        client.template.policy.list.dataprefixfqdn.get_lists_by_id_15()


Operation: PUT /dataservice/template/policy/list/dataprefixfqdn/{id}
--------------------------------------------------------------------


Edit policy list entries for a specific type of policy list

.. code:: python

    def edit_policy_list_15(
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
        client.template.policy.list.dataprefixfqdn.edit_policy_list_15()


Operation: DELETE /dataservice/template/policy/list/dataprefixfqdn/{id}
-----------------------------------------------------------------------


Delete policy list entry for a specific type of policy list

.. code:: python

    def delete_policy_list_15(id: str) -> None: ...


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
        client.template.policy.list.dataprefixfqdn.delete_policy_list_15()


.. toctree::
    :maxdepth: 1

    filtered
    preview

