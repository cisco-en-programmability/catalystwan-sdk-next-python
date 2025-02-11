===========================
template.policy.list.aspath
===========================


Operation: GET /dataservice/template/policy/list/aspath
-------------------------------------------------------


Get policy lists

.. code:: python

    def get_policy_lists_5() -> List[Any]: ...


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
        client.template.policy.list.aspath.get_policy_lists_5()


Operation: POST /dataservice/template/policy/list/aspath
--------------------------------------------------------


Create policy list

.. code:: python

    def create_policy_list_5(payload: Optional[Any] = None) -> Any: ...


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
        client.template.policy.list.aspath.create_policy_list_5()


Operation: DELETE /dataservice/template/policy/list/aspath
----------------------------------------------------------


Delete policy lists with specific info tag

.. code:: python

    def delete_policy_lists_with_info_tag_5(
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
        client.template.policy.list.aspath.delete_policy_lists_with_info_tag_5()


Operation: GET /dataservice/template/policy/list/aspath/{id}
------------------------------------------------------------


Get a specific policy list based on the id

.. code:: python

    def get_lists_by_id_5(id: str) -> Any: ...


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
        client.template.policy.list.aspath.get_lists_by_id_5()


Operation: PUT /dataservice/template/policy/list/aspath/{id}
------------------------------------------------------------


Edit policy list entries for a specific type of policy list

.. code:: python

    def edit_policy_list_5(
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
        client.template.policy.list.aspath.edit_policy_list_5()


Operation: DELETE /dataservice/template/policy/list/aspath/{id}
---------------------------------------------------------------


Delete policy list entry for a specific type of policy list

.. code:: python

    def delete_policy_list_5(id: str) -> None: ...


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
        client.template.policy.list.aspath.delete_policy_list_5()


.. toctree::
    :maxdepth: 1

    filtered
    preview

