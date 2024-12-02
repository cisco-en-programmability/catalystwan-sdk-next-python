=============================
template.policy.list.localapp
=============================


Operation: GET /dataservice/template/policy/list/localapp
---------------------------------------------------------


Get policy lists

.. code:: python

    def get_policy_lists_19() -> List[Any]: ...


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
        client.template.policy.list.localapp.get_policy_lists_19()


Operation: POST /dataservice/template/policy/list/localapp
----------------------------------------------------------


Create policy list

.. code:: python

    def create_policy_list_22(payload: Optional[Any] = None) -> Any: ...


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
        client.template.policy.list.localapp.create_policy_list_22()


Operation: DELETE /dataservice/template/policy/list/localapp
------------------------------------------------------------


Delete policy lists with specific info tag

.. code:: python

    def delete_policy_lists_with_info_tag_22(
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
        client.template.policy.list.localapp.delete_policy_lists_with_info_tag_22()


Operation: GET /dataservice/template/policy/list/localapp/{id}
--------------------------------------------------------------


Get a specific policy list based on the id

.. code:: python

    def get_lists_by_id_22(id: str) -> Any: ...


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
        client.template.policy.list.localapp.get_lists_by_id_22()


Operation: PUT /dataservice/template/policy/list/localapp/{id}
--------------------------------------------------------------


Edit policy list entries for a specific type of policy list

.. code:: python

    def edit_policy_list_22(
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
        client.template.policy.list.localapp.edit_policy_list_22()


Operation: DELETE /dataservice/template/policy/list/localapp/{id}
-----------------------------------------------------------------


Delete policy list entry for a specific type of policy list

.. code:: python

    def delete_policy_list_22(id: str) -> None: ...


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
        client.template.policy.list.localapp.delete_policy_list_22()


.. toctree::
    :maxdepth: 1

    filtered
    preview

