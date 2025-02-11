=====================================
template.policy.list.scalablegrouptag
=====================================


Operation: GET /dataservice/template/policy/list/scalablegrouptag
-----------------------------------------------------------------


Get policy lists

.. code:: python

    def get_policy_lists_29() -> List[Any]: ...


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
        client.template.policy.list.scalablegrouptag.get_policy_lists_29()


Operation: POST /dataservice/template/policy/list/scalablegrouptag
------------------------------------------------------------------


Create policy list

.. code:: python

    def create_policy_list_32(payload: Optional[Any] = None) -> Any: ...


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
        client.template.policy.list.scalablegrouptag.create_policy_list_32()


Operation: DELETE /dataservice/template/policy/list/scalablegrouptag
--------------------------------------------------------------------


Delete policy lists with specific info tag

.. code:: python

    def delete_policy_lists_with_info_tag_32(
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
        client.template.policy.list.scalablegrouptag.delete_policy_lists_with_info_tag_32()


Operation: GET /dataservice/template/policy/list/scalablegrouptag/{id}
----------------------------------------------------------------------


Get a specific policy list based on the id

.. code:: python

    def get_lists_by_id_32(id: str) -> Any: ...


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
        client.template.policy.list.scalablegrouptag.get_lists_by_id_32()


Operation: PUT /dataservice/template/policy/list/scalablegrouptag/{id}
----------------------------------------------------------------------


Edit policy list entries for a specific type of policy list

.. code:: python

    def edit_policy_list_32(
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
        client.template.policy.list.scalablegrouptag.edit_policy_list_32()


Operation: DELETE /dataservice/template/policy/list/scalablegrouptag/{id}
-------------------------------------------------------------------------


Delete policy list entry for a specific type of policy list

.. code:: python

    def delete_policy_list_32(id: str) -> None: ...


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
        client.template.policy.list.scalablegrouptag.delete_policy_list_32()


.. toctree::
    :maxdepth: 1

    filtered
    preview

