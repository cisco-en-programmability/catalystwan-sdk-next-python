========================================
template.policy.list.preferredcolorgroup
========================================


Operation: GET /dataservice/template/policy/list/preferredcolorgroup
--------------------------------------------------------------------


Get policy lists

.. code:: python

    def get_policy_lists_25() -> List[Any]: ...


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
        client.template.policy.list.preferredcolorgroup.get_policy_lists_25()


Operation: POST /dataservice/template/policy/list/preferredcolorgroup
---------------------------------------------------------------------


Create policy list

.. code:: python

    def create_policy_list_28(payload: Optional[Any] = None) -> Any: ...


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
        client.template.policy.list.preferredcolorgroup.create_policy_list_28()


Operation: DELETE /dataservice/template/policy/list/preferredcolorgroup
-----------------------------------------------------------------------


Delete policy lists with specific info tag

.. code:: python

    def delete_policy_lists_with_info_tag_28(
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
        client.template.policy.list.preferredcolorgroup.delete_policy_lists_with_info_tag_28()


Operation: GET /dataservice/template/policy/list/preferredcolorgroup/{id}
-------------------------------------------------------------------------


Get a specific policy list based on the id

.. code:: python

    def get_lists_by_id_28(id: str) -> Any: ...


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
        client.template.policy.list.preferredcolorgroup.get_lists_by_id_28()


Operation: PUT /dataservice/template/policy/list/preferredcolorgroup/{id}
-------------------------------------------------------------------------


Edit policy list entries for a specific type of policy list

.. code:: python

    def edit_policy_list_28(
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
        client.template.policy.list.preferredcolorgroup.edit_policy_list_28()


Operation: DELETE /dataservice/template/policy/list/preferredcolorgroup/{id}
----------------------------------------------------------------------------


Delete policy list entry for a specific type of policy list

.. code:: python

    def delete_policy_list_28(id: str) -> None: ...


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
        client.template.policy.list.preferredcolorgroup.delete_policy_list_28()


.. toctree::
    :maxdepth: 1

    filtered
    preview

