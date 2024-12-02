=============================
template.policy.list.identity
=============================


Operation: GET /dataservice/template/policy/list/identity
---------------------------------------------------------


Get policy lists

.. code:: python

    def get_policy_lists_16() -> List[Any]: ...


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
        client.template.policy.list.identity.get_policy_lists_16()


Operation: POST /dataservice/template/policy/list/identity
----------------------------------------------------------


Create policy list

.. code:: python

    def create_policy_list_18(payload: Optional[Any] = None) -> Any: ...


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
        client.template.policy.list.identity.create_policy_list_18()


Operation: DELETE /dataservice/template/policy/list/identity
------------------------------------------------------------


Delete policy lists with specific info tag

.. code:: python

    def delete_policy_lists_with_info_tag_18(
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
        client.template.policy.list.identity.delete_policy_lists_with_info_tag_18()


Operation: GET /dataservice/template/policy/list/identity/{id}
--------------------------------------------------------------


Get a specific policy list based on the id

.. code:: python

    def get_lists_by_id_18(id: str) -> Any: ...


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
        client.template.policy.list.identity.get_lists_by_id_18()


Operation: PUT /dataservice/template/policy/list/identity/{id}
--------------------------------------------------------------


Edit policy list entries for a specific type of policy list

.. code:: python

    def edit_policy_list_18(
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
        client.template.policy.list.identity.edit_policy_list_18()


Operation: DELETE /dataservice/template/policy/list/identity/{id}
-----------------------------------------------------------------


Delete policy list entry for a specific type of policy list

.. code:: python

    def delete_policy_list_18(id: str) -> None: ...


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
        client.template.policy.list.identity.delete_policy_list_18()


.. toctree::
    :maxdepth: 1

    filtered
    preview

