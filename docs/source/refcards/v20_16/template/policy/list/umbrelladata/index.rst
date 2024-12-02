=================================
template.policy.list.umbrelladata
=================================


Operation: GET /dataservice/template/policy/list/umbrelladata
-------------------------------------------------------------


Get policy lists

.. code:: python

    def get_policy_lists_36() -> List[Any]: ...


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
        client.template.policy.list.umbrelladata.get_policy_lists_36()


Operation: POST /dataservice/template/policy/list/umbrelladata
--------------------------------------------------------------


Create policy list

.. code:: python

    def create_policy_list_39(payload: Optional[Any] = None) -> Any: ...


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
        client.template.policy.list.umbrelladata.create_policy_list_39()


Operation: DELETE /dataservice/template/policy/list/umbrelladata
----------------------------------------------------------------


Delete policy lists with specific info tag

.. code:: python

    def delete_policy_lists_with_info_tag_39(
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
        client.template.policy.list.umbrelladata.delete_policy_lists_with_info_tag_39()


Operation: GET /dataservice/template/policy/list/umbrelladata/{id}
------------------------------------------------------------------


Get a specific policy list based on the id

.. code:: python

    def get_lists_by_id_39(id: str) -> Any: ...


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
        client.template.policy.list.umbrelladata.get_lists_by_id_39()


Operation: PUT /dataservice/template/policy/list/umbrelladata/{id}
------------------------------------------------------------------


Edit policy list entries for a specific type of policy list

.. code:: python

    def edit_policy_list_39(
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
        client.template.policy.list.umbrelladata.edit_policy_list_39()


Operation: DELETE /dataservice/template/policy/list/umbrelladata/{id}
---------------------------------------------------------------------


Delete policy list entry for a specific type of policy list

.. code:: python

    def delete_policy_list_39(id: str) -> None: ...


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
        client.template.policy.list.umbrelladata.delete_policy_list_39()


.. toctree::
    :maxdepth: 1

    filtered
    preview

