===========================
template.policy.list.mirror
===========================


Operation: GET /dataservice/template/policy/list/mirror
-------------------------------------------------------


Get policy lists

.. code:: python

    def get_policy_lists_21() -> List[Any]: ...


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
        client.template.policy.list.mirror.get_policy_lists_21()


Operation: POST /dataservice/template/policy/list/mirror
--------------------------------------------------------


Create policy list

.. code:: python

    def create_policy_list_24(payload: Optional[Any] = None) -> Any: ...


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
        client.template.policy.list.mirror.create_policy_list_24()


Operation: DELETE /dataservice/template/policy/list/mirror
----------------------------------------------------------


Delete policy lists with specific info tag

.. code:: python

    def delete_policy_lists_with_info_tag_24(
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
        client.template.policy.list.mirror.delete_policy_lists_with_info_tag_24()


Operation: GET /dataservice/template/policy/list/mirror/{id}
------------------------------------------------------------


Get a specific policy list based on the id

.. code:: python

    def get_lists_by_id_24(id: str) -> Any: ...


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
        client.template.policy.list.mirror.get_lists_by_id_24()


Operation: PUT /dataservice/template/policy/list/mirror/{id}
------------------------------------------------------------


Edit policy list entries for a specific type of policy list

.. code:: python

    def edit_policy_list_24(
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
        client.template.policy.list.mirror.edit_policy_list_24()


Operation: DELETE /dataservice/template/policy/list/mirror/{id}
---------------------------------------------------------------


Delete policy list entry for a specific type of policy list

.. code:: python

    def delete_policy_list_24(id: str) -> None: ...


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
        client.template.policy.list.mirror.delete_policy_list_24()


.. toctree::
    :maxdepth: 1

    filtered
    preview

