====================================
template.policy.list.supervisorydisc
====================================


Operation: GET /dataservice/template/policy/list/supervisorydisc
----------------------------------------------------------------


Get policy lists

.. code:: python

    def get_policy_lists_32() -> List[Any]: ...


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
        client.template.policy.list.supervisorydisc.get_policy_lists_32()


Operation: POST /dataservice/template/policy/list/supervisorydisc
-----------------------------------------------------------------


Create policy list

.. code:: python

    def create_policy_list_35(payload: Optional[Any] = None) -> Any: ...


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
        client.template.policy.list.supervisorydisc.create_policy_list_35()


Operation: DELETE /dataservice/template/policy/list/supervisorydisc
-------------------------------------------------------------------


Delete policy lists with specific info tag

.. code:: python

    def delete_policy_lists_with_info_tag_35(
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
        client.template.policy.list.supervisorydisc.delete_policy_lists_with_info_tag_35()


Operation: GET /dataservice/template/policy/list/supervisorydisc/{id}
---------------------------------------------------------------------


Get a specific policy list based on the id

.. code:: python

    def get_lists_by_id_35(id: str) -> Any: ...


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
        client.template.policy.list.supervisorydisc.get_lists_by_id_35()


Operation: PUT /dataservice/template/policy/list/supervisorydisc/{id}
---------------------------------------------------------------------


Edit policy list entries for a specific type of policy list

.. code:: python

    def edit_policy_list_35(
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
        client.template.policy.list.supervisorydisc.edit_policy_list_35()


Operation: DELETE /dataservice/template/policy/list/supervisorydisc/{id}
------------------------------------------------------------------------


Delete policy list entry for a specific type of policy list

.. code:: python

    def delete_policy_list_35(id: str) -> None: ...


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
        client.template.policy.list.supervisorydisc.delete_policy_list_35()


.. toctree::
    :maxdepth: 1

    filtered
    preview

