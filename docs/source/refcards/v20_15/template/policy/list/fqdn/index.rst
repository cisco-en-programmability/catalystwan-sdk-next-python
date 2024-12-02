=========================
template.policy.list.fqdn
=========================


Operation: GET /dataservice/template/policy/list/fqdn
-----------------------------------------------------


Get policy lists

.. code:: python

    def get_policy_lists_14() -> List[Any]: ...


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
        client.template.policy.list.fqdn.get_policy_lists_14()


Operation: POST /dataservice/template/policy/list/fqdn
------------------------------------------------------


Create policy list

.. code:: python

    def create_policy_list_16(payload: Optional[Any] = None) -> Any: ...


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
        client.template.policy.list.fqdn.create_policy_list_16()


Operation: DELETE /dataservice/template/policy/list/fqdn
--------------------------------------------------------


Delete policy lists with specific info tag

.. code:: python

    def delete_policy_lists_with_info_tag_16(
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
        client.template.policy.list.fqdn.delete_policy_lists_with_info_tag_16()


Operation: GET /dataservice/template/policy/list/fqdn/{id}
----------------------------------------------------------


Get a specific policy list based on the id

.. code:: python

    def get_lists_by_id_16(id: str) -> Any: ...


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
        client.template.policy.list.fqdn.get_lists_by_id_16()


Operation: PUT /dataservice/template/policy/list/fqdn/{id}
----------------------------------------------------------


Edit policy list entries for a specific type of policy list

.. code:: python

    def edit_policy_list_16(
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
        client.template.policy.list.fqdn.edit_policy_list_16()


Operation: DELETE /dataservice/template/policy/list/fqdn/{id}
-------------------------------------------------------------


Delete policy list entry for a specific type of policy list

.. code:: python

    def delete_policy_list_16(id: str) -> None: ...


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
        client.template.policy.list.fqdn.delete_policy_list_16()


.. toctree::
    :maxdepth: 1

    filtered
    preview

