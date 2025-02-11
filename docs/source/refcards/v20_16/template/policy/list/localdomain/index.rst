================================
template.policy.list.localdomain
================================


Operation: GET /dataservice/template/policy/list/localdomain
------------------------------------------------------------


Get policy lists

.. code:: python

    def get_policy_lists_20() -> List[Any]: ...


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
        client.template.policy.list.localdomain.get_policy_lists_20()


Operation: POST /dataservice/template/policy/list/localdomain
-------------------------------------------------------------


Create policy list

.. code:: python

    def create_policy_list_23(payload: Optional[Any] = None) -> Any: ...


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
        client.template.policy.list.localdomain.create_policy_list_23()


Operation: DELETE /dataservice/template/policy/list/localdomain
---------------------------------------------------------------


Delete policy lists with specific info tag

.. code:: python

    def delete_policy_lists_with_info_tag_23(
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
        client.template.policy.list.localdomain.delete_policy_lists_with_info_tag_23()


Operation: GET /dataservice/template/policy/list/localdomain/{id}
-----------------------------------------------------------------


Get a specific policy list based on the id

.. code:: python

    def get_lists_by_id_23(id: str) -> Any: ...


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
        client.template.policy.list.localdomain.get_lists_by_id_23()


Operation: PUT /dataservice/template/policy/list/localdomain/{id}
-----------------------------------------------------------------


Edit policy list entries for a specific type of policy list

.. code:: python

    def edit_policy_list_23(
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
        client.template.policy.list.localdomain.edit_policy_list_23()


Operation: DELETE /dataservice/template/policy/list/localdomain/{id}
--------------------------------------------------------------------


Delete policy list entry for a specific type of policy list

.. code:: python

    def delete_policy_list_23(id: str) -> None: ...


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
        client.template.policy.list.localdomain.delete_policy_list_23()


.. toctree::
    :maxdepth: 1

    filtered
    preview

