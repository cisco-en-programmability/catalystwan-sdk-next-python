=================================
template.policy.list.urlwhitelist
=================================


Operation: GET /dataservice/template/policy/list/urlwhitelist
-------------------------------------------------------------


Get policy lists

.. code:: python

    def get_policy_lists_38() -> List[Any]: ...


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
        client.template.policy.list.urlwhitelist.get_policy_lists_38()


Operation: POST /dataservice/template/policy/list/urlwhitelist
--------------------------------------------------------------


Create policy list

.. code:: python

    def create_policy_list_41(payload: Optional[Any] = None) -> Any: ...


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
        client.template.policy.list.urlwhitelist.create_policy_list_41()


Operation: DELETE /dataservice/template/policy/list/urlwhitelist
----------------------------------------------------------------


Delete policy lists with specific info tag

.. code:: python

    def delete_policy_lists_with_info_tag_41(
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
        client.template.policy.list.urlwhitelist.delete_policy_lists_with_info_tag_41()


Operation: GET /dataservice/template/policy/list/urlwhitelist/{id}
------------------------------------------------------------------


Get a specific policy list based on the id

.. code:: python

    def get_lists_by_id_41(id: str) -> Any: ...


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
        client.template.policy.list.urlwhitelist.get_lists_by_id_41()


Operation: PUT /dataservice/template/policy/list/urlwhitelist/{id}
------------------------------------------------------------------


Edit policy list entries for a specific type of policy list

.. code:: python

    def edit_policy_list_41(
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
        client.template.policy.list.urlwhitelist.edit_policy_list_41()


Operation: DELETE /dataservice/template/policy/list/urlwhitelist/{id}
---------------------------------------------------------------------


Delete policy list entry for a specific type of policy list

.. code:: python

    def delete_policy_list_41(id: str) -> None: ...


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
        client.template.policy.list.urlwhitelist.delete_policy_list_41()


.. toctree::
    :maxdepth: 1

    filtered
    preview

