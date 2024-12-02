========================
template.policy.list.vpn
========================


Operation: GET /dataservice/template/policy/list/vpn
----------------------------------------------------


Get policy lists

.. code:: python

    def get_policy_lists_39() -> List[Any]: ...


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
        client.template.policy.list.vpn.get_policy_lists_39()


Operation: POST /dataservice/template/policy/list/vpn
-----------------------------------------------------


Create policy list

.. code:: python

    def create_policy_list_42(payload: Optional[Any] = None) -> Any: ...


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
        client.template.policy.list.vpn.create_policy_list_42()


Operation: DELETE /dataservice/template/policy/list/vpn
-------------------------------------------------------


Delete policy lists with specific info tag

.. code:: python

    def delete_policy_lists_with_info_tag_42(
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
        client.template.policy.list.vpn.delete_policy_lists_with_info_tag_42()


Operation: GET /dataservice/template/policy/list/vpn/{id}
---------------------------------------------------------


Get a specific policy list based on the id

.. code:: python

    def get_lists_by_id_42(id: str) -> Any: ...


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
        client.template.policy.list.vpn.get_lists_by_id_42()


Operation: PUT /dataservice/template/policy/list/vpn/{id}
---------------------------------------------------------


Edit policy list entries for a specific type of policy list

.. code:: python

    def edit_policy_list_42(
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
        client.template.policy.list.vpn.edit_policy_list_42()


Operation: DELETE /dataservice/template/policy/list/vpn/{id}
------------------------------------------------------------


Delete policy list entry for a specific type of policy list

.. code:: python

    def delete_policy_list_42(id: str) -> None: ...


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
        client.template.policy.list.vpn.delete_policy_list_42()


.. toctree::
    :maxdepth: 1

    filtered
    preview

