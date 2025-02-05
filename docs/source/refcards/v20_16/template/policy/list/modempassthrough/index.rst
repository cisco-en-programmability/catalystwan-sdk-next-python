=====================================
template.policy.list.modempassthrough
=====================================


Operation: GET /dataservice/template/policy/list/modempassthrough
-----------------------------------------------------------------


Get policy lists

.. code:: python

    def get_policy_lists_22() -> List[Any]: ...


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
        client.template.policy.list.modempassthrough.get_policy_lists_22()


Operation: POST /dataservice/template/policy/list/modempassthrough
------------------------------------------------------------------


Create policy list

.. code:: python

    def create_policy_list_25(payload: Optional[Any] = None) -> Any: ...


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
        client.template.policy.list.modempassthrough.create_policy_list_25()


Operation: DELETE /dataservice/template/policy/list/modempassthrough
--------------------------------------------------------------------


Delete policy lists with specific info tag

.. code:: python

    def delete_policy_lists_with_info_tag_25(
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
        client.template.policy.list.modempassthrough.delete_policy_lists_with_info_tag_25()


Operation: GET /dataservice/template/policy/list/modempassthrough/{id}
----------------------------------------------------------------------


Get a specific policy list based on the id

.. code:: python

    def get_lists_by_id_25(id: str) -> Any: ...


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
        client.template.policy.list.modempassthrough.get_lists_by_id_25()


Operation: PUT /dataservice/template/policy/list/modempassthrough/{id}
----------------------------------------------------------------------


Edit policy list entries for a specific type of policy list

.. code:: python

    def edit_policy_list_25(
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
        client.template.policy.list.modempassthrough.edit_policy_list_25()


Operation: DELETE /dataservice/template/policy/list/modempassthrough/{id}
-------------------------------------------------------------------------


Delete policy list entry for a specific type of policy list

.. code:: python

    def delete_policy_list_25(id: str) -> None: ...


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
        client.template.policy.list.modempassthrough.delete_policy_list_25()


.. toctree::
    :maxdepth: 1

    filtered
    preview

