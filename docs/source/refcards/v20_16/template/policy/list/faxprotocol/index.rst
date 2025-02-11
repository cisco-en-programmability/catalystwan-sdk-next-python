================================
template.policy.list.faxprotocol
================================


Operation: GET /dataservice/template/policy/list/faxprotocol
------------------------------------------------------------


Get policy lists

.. code:: python

    def get_policy_lists_12() -> List[Any]: ...


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
        client.template.policy.list.faxprotocol.get_policy_lists_12()


Operation: POST /dataservice/template/policy/list/faxprotocol
-------------------------------------------------------------


Create policy list

.. code:: python

    def create_policy_list_13(payload: Optional[Any] = None) -> Any: ...


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
        client.template.policy.list.faxprotocol.create_policy_list_13()


Operation: DELETE /dataservice/template/policy/list/faxprotocol
---------------------------------------------------------------


Delete policy lists with specific info tag

.. code:: python

    def delete_policy_lists_with_info_tag_13(
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
        client.template.policy.list.faxprotocol.delete_policy_lists_with_info_tag_13()


Operation: GET /dataservice/template/policy/list/faxprotocol/{id}
-----------------------------------------------------------------


Get a specific policy list based on the id

.. code:: python

    def get_lists_by_id_13(id: str) -> Any: ...


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
        client.template.policy.list.faxprotocol.get_lists_by_id_13()


Operation: PUT /dataservice/template/policy/list/faxprotocol/{id}
-----------------------------------------------------------------


Edit policy list entries for a specific type of policy list

.. code:: python

    def edit_policy_list_13(
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
        client.template.policy.list.faxprotocol.edit_policy_list_13()


Operation: DELETE /dataservice/template/policy/list/faxprotocol/{id}
--------------------------------------------------------------------


Delete policy list entry for a specific type of policy list

.. code:: python

    def delete_policy_list_13(id: str) -> None: ...


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
        client.template.policy.list.faxprotocol.delete_policy_list_13()


.. toctree::
    :maxdepth: 1

    filtered
    preview

