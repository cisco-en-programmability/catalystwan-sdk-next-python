=====================================
template.policy.list.translationrules
=====================================


Operation: GET /dataservice/template/policy/list/translationrules
-----------------------------------------------------------------


Get policy lists

.. code:: python

    def get_policy_lists_2() -> List[Any]: ...


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
        client.template.policy.list.translationrules.get_policy_lists_2()


Operation: POST /dataservice/template/policy/list/translationrules
------------------------------------------------------------------


Create policy list

.. code:: python

    def create_policy_list_2(payload: Optional[Any] = None) -> Any: ...


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
        client.template.policy.list.translationrules.create_policy_list_2()


Operation: DELETE /dataservice/template/policy/list/translationrules
--------------------------------------------------------------------


Delete policy lists with specific info tag

.. code:: python

    def delete_policy_lists_with_info_tag_2(
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
        client.template.policy.list.translationrules.delete_policy_lists_with_info_tag_2()


Operation: GET /dataservice/template/policy/list/translationrules/{id}
----------------------------------------------------------------------


Get a specific policy list based on the id

.. code:: python

    def get_lists_by_id_2(id: str) -> Any: ...


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
        client.template.policy.list.translationrules.get_lists_by_id_2()


Operation: PUT /dataservice/template/policy/list/translationrules/{id}
----------------------------------------------------------------------


Edit policy list entries for a specific type of policy list

.. code:: python

    def edit_policy_list_2(
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
        client.template.policy.list.translationrules.edit_policy_list_2()


Operation: DELETE /dataservice/template/policy/list/translationrules/{id}
-------------------------------------------------------------------------


Delete policy list entry for a specific type of policy list

.. code:: python

    def delete_policy_list_2(id: str) -> None: ...


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
        client.template.policy.list.translationrules.delete_policy_list_2()


.. toctree::
    :maxdepth: 1

    filtered
    preview

