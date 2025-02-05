=======================================
template.policy.list.translationprofile
=======================================


Operation: GET /dataservice/template/policy/list/translationprofile
-------------------------------------------------------------------


Get policy lists

.. code:: python

    def get_policy_lists_1() -> List[Any]: ...


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
        client.template.policy.list.translationprofile.get_policy_lists_1()


Operation: POST /dataservice/template/policy/list/translationprofile
--------------------------------------------------------------------


Create policy list

.. code:: python

    def create_policy_list_1(payload: Optional[Any] = None) -> Any: ...


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
        client.template.policy.list.translationprofile.create_policy_list_1()


Operation: DELETE /dataservice/template/policy/list/translationprofile
----------------------------------------------------------------------


Delete policy lists with specific info tag

.. code:: python

    def delete_policy_lists_with_info_tag_1(
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
        client.template.policy.list.translationprofile.delete_policy_lists_with_info_tag_1()


Operation: GET /dataservice/template/policy/list/translationprofile/{id}
------------------------------------------------------------------------


Get a specific policy list based on the id

.. code:: python

    def get_lists_by_id_1(id: str) -> Any: ...


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
        client.template.policy.list.translationprofile.get_lists_by_id_1()


Operation: PUT /dataservice/template/policy/list/translationprofile/{id}
------------------------------------------------------------------------


Edit policy list entries for a specific type of policy list

.. code:: python

    def edit_policy_list_1(
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
        client.template.policy.list.translationprofile.edit_policy_list_1()


Operation: DELETE /dataservice/template/policy/list/translationprofile/{id}
---------------------------------------------------------------------------


Delete policy list entry for a specific type of policy list

.. code:: python

    def delete_policy_list_1(id: str) -> None: ...


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
        client.template.policy.list.translationprofile.delete_policy_list_1()


.. toctree::
    :maxdepth: 1

    filtered
    preview

