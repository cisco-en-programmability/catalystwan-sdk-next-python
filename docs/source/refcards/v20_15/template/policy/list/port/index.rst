=========================
template.policy.list.port
=========================


Operation: GET /dataservice/template/policy/list/port
-----------------------------------------------------


Get policy lists

.. code:: python

    def get_policy_lists_24() -> List[Any]: ...


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
        client.template.policy.list.port.get_policy_lists_24()


Operation: POST /dataservice/template/policy/list/port
------------------------------------------------------


Create policy list

.. code:: python

    def create_policy_list_27(payload: Optional[Any] = None) -> Any: ...


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
        client.template.policy.list.port.create_policy_list_27()


Operation: DELETE /dataservice/template/policy/list/port
--------------------------------------------------------


Delete policy lists with specific info tag

.. code:: python

    def delete_policy_lists_with_info_tag_27(
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
        client.template.policy.list.port.delete_policy_lists_with_info_tag_27()


Operation: GET /dataservice/template/policy/list/port/{id}
----------------------------------------------------------


Get a specific policy list based on the id

.. code:: python

    def get_lists_by_id_27(id: str) -> Any: ...


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
        client.template.policy.list.port.get_lists_by_id_27()


Operation: PUT /dataservice/template/policy/list/port/{id}
----------------------------------------------------------


Edit policy list entries for a specific type of policy list

.. code:: python

    def edit_policy_list_27(
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
        client.template.policy.list.port.edit_policy_list_27()


Operation: DELETE /dataservice/template/policy/list/port/{id}
-------------------------------------------------------------


Delete policy list entry for a specific type of policy list

.. code:: python

    def delete_policy_list_27(id: str) -> None: ...


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
        client.template.policy.list.port.delete_policy_list_27()


.. toctree::
    :maxdepth: 1

    filtered
    preview

