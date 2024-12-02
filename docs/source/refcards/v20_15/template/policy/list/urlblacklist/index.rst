=================================
template.policy.list.urlblacklist
=================================


Operation: GET /dataservice/template/policy/list/urlblacklist
-------------------------------------------------------------


Get policy lists

.. code:: python

    def get_policy_lists_37() -> List[Any]: ...


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
        client.template.policy.list.urlblacklist.get_policy_lists_37()


Operation: POST /dataservice/template/policy/list/urlblacklist
--------------------------------------------------------------


Create policy list

.. code:: python

    def create_policy_list_40(payload: Optional[Any] = None) -> Any: ...


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
        client.template.policy.list.urlblacklist.create_policy_list_40()


Operation: DELETE /dataservice/template/policy/list/urlblacklist
----------------------------------------------------------------


Delete policy lists with specific info tag

.. code:: python

    def delete_policy_lists_with_info_tag_40(
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
        client.template.policy.list.urlblacklist.delete_policy_lists_with_info_tag_40()


Operation: GET /dataservice/template/policy/list/urlblacklist/{id}
------------------------------------------------------------------


Get a specific policy list based on the id

.. code:: python

    def get_lists_by_id_40(id: str) -> Any: ...


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
        client.template.policy.list.urlblacklist.get_lists_by_id_40()


Operation: PUT /dataservice/template/policy/list/urlblacklist/{id}
------------------------------------------------------------------


Edit policy list entries for a specific type of policy list

.. code:: python

    def edit_policy_list_40(
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
        client.template.policy.list.urlblacklist.edit_policy_list_40()


Operation: DELETE /dataservice/template/policy/list/urlblacklist/{id}
---------------------------------------------------------------------


Delete policy list entry for a specific type of policy list

.. code:: python

    def delete_policy_list_40(id: str) -> None: ...


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
        client.template.policy.list.urlblacklist.delete_policy_list_40()


.. toctree::
    :maxdepth: 1

    filtered
    preview

