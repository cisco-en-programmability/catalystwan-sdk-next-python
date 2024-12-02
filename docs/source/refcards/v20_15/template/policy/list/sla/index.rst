========================
template.policy.list.sla
========================


Operation: GET /dataservice/template/policy/list/sla
----------------------------------------------------


Get policy lists

.. code:: python

    def get_policy_lists_31() -> List[Any]: ...


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
        client.template.policy.list.sla.get_policy_lists_31()


Operation: POST /dataservice/template/policy/list/sla
-----------------------------------------------------


Create policy list

.. code:: python

    def create_policy_list_34(payload: Optional[Any] = None) -> Any: ...


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
        client.template.policy.list.sla.create_policy_list_34()


Operation: DELETE /dataservice/template/policy/list/sla
-------------------------------------------------------


Delete policy lists with specific info tag

.. code:: python

    def delete_policy_lists_with_info_tag_34(
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
        client.template.policy.list.sla.delete_policy_lists_with_info_tag_34()


Operation: GET /dataservice/template/policy/list/sla/{id}
---------------------------------------------------------


Get a specific policy list based on the id

.. code:: python

    def get_lists_by_id_34(id: str) -> Any: ...


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
        client.template.policy.list.sla.get_lists_by_id_34()


Operation: PUT /dataservice/template/policy/list/sla/{id}
---------------------------------------------------------


Edit policy list entries for a specific type of policy list

.. code:: python

    def edit_policy_list_34(
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
        client.template.policy.list.sla.edit_policy_list_34()


Operation: DELETE /dataservice/template/policy/list/sla/{id}
------------------------------------------------------------


Delete policy list entry for a specific type of policy list

.. code:: python

    def delete_policy_list_34(id: str) -> None: ...


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
        client.template.policy.list.sla.delete_policy_list_34()


.. toctree::
    :maxdepth: 1

    filtered
    preview

