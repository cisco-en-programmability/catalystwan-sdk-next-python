==========================
template.policy.list.color
==========================


Operation: GET /dataservice/template/policy/list/color
------------------------------------------------------


Get policy lists

.. code:: python

    def get_policy_lists_6() -> List[Any]: ...


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
        client.template.policy.list.color.get_policy_lists_6()


Operation: POST /dataservice/template/policy/list/color
-------------------------------------------------------


Create policy list

.. code:: python

    def create_policy_list_6(payload: Optional[Any] = None) -> Any: ...


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
        client.template.policy.list.color.create_policy_list_6()


Operation: DELETE /dataservice/template/policy/list/color
---------------------------------------------------------


Delete policy lists with specific info tag

.. code:: python

    def delete_policy_lists_with_info_tag_6(
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
        client.template.policy.list.color.delete_policy_lists_with_info_tag_6()


Operation: GET /dataservice/template/policy/list/color/{id}
-----------------------------------------------------------


Get a specific policy list based on the id

.. code:: python

    def get_lists_by_id_6(id: str) -> Any: ...


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
        client.template.policy.list.color.get_lists_by_id_6()


Operation: PUT /dataservice/template/policy/list/color/{id}
-----------------------------------------------------------


Edit policy list entries for a specific type of policy list

.. code:: python

    def edit_policy_list_6(
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
        client.template.policy.list.color.edit_policy_list_6()


Operation: DELETE /dataservice/template/policy/list/color/{id}
--------------------------------------------------------------


Delete policy list entry for a specific type of policy list

.. code:: python

    def delete_policy_list_6(id: str) -> None: ...


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
        client.template.policy.list.color.delete_policy_list_6()


.. toctree::
    :maxdepth: 1

    filtered
    preview

