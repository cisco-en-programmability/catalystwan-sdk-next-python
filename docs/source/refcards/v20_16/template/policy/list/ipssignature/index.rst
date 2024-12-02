=================================
template.policy.list.ipssignature
=================================


Operation: GET /dataservice/template/policy/list/ipssignature
-------------------------------------------------------------


Get policy lists

.. code:: python

    def get_policy_lists_17() -> List[Any]: ...


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
        client.template.policy.list.ipssignature.get_policy_lists_17()


Operation: POST /dataservice/template/policy/list/ipssignature
--------------------------------------------------------------


Create policy list

.. code:: python

    def create_policy_list_19(payload: Optional[Any] = None) -> Any: ...


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
        client.template.policy.list.ipssignature.create_policy_list_19()


Operation: DELETE /dataservice/template/policy/list/ipssignature
----------------------------------------------------------------


Delete policy lists with specific info tag

.. code:: python

    def delete_policy_lists_with_info_tag_19(
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
        client.template.policy.list.ipssignature.delete_policy_lists_with_info_tag_19()


Operation: GET /dataservice/template/policy/list/ipssignature/{id}
------------------------------------------------------------------


Get a specific policy list based on the id

.. code:: python

    def get_lists_by_id_19(id: str) -> Any: ...


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
        client.template.policy.list.ipssignature.get_lists_by_id_19()


Operation: PUT /dataservice/template/policy/list/ipssignature/{id}
------------------------------------------------------------------


Edit policy list entries for a specific type of policy list

.. code:: python

    def edit_policy_list_19(
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
        client.template.policy.list.ipssignature.edit_policy_list_19()


Operation: DELETE /dataservice/template/policy/list/ipssignature/{id}
---------------------------------------------------------------------


Delete policy list entry for a specific type of policy list

.. code:: python

    def delete_policy_list_19(id: str) -> None: ...


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
        client.template.policy.list.ipssignature.delete_policy_list_19()


.. toctree::
    :maxdepth: 1

    filtered
    preview

