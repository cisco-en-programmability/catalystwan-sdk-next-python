=========================
template.policy.list.site
=========================


Operation: GET /dataservice/template/policy/list/site
-----------------------------------------------------


Get policy lists

.. code:: python

    def get_policy_lists_30() -> List[Any]: ...


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
        client.template.policy.list.site.get_policy_lists_30()


Operation: POST /dataservice/template/policy/list/site
------------------------------------------------------


Create policy list

.. code:: python

    def create_policy_list_33(payload: Optional[Any] = None) -> Any: ...


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
        client.template.policy.list.site.create_policy_list_33()


Operation: DELETE /dataservice/template/policy/list/site
--------------------------------------------------------


Delete policy lists with specific info tag

.. code:: python

    def delete_policy_lists_with_info_tag_33(
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
        client.template.policy.list.site.delete_policy_lists_with_info_tag_33()


Operation: GET /dataservice/template/policy/list/site/{id}
----------------------------------------------------------


Get a specific policy list based on the id

.. code:: python

    def get_lists_by_id_33(id: str) -> Any: ...


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
        client.template.policy.list.site.get_lists_by_id_33()


Operation: PUT /dataservice/template/policy/list/site/{id}
----------------------------------------------------------


Edit policy list entries for a specific type of policy list

.. code:: python

    def edit_policy_list_33(
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
        client.template.policy.list.site.edit_policy_list_33()


Operation: DELETE /dataservice/template/policy/list/site/{id}
-------------------------------------------------------------


Delete policy list entry for a specific type of policy list

.. code:: python

    def delete_policy_list_33(id: str) -> None: ...


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
        client.template.policy.list.site.delete_policy_list_33()


.. toctree::
    :maxdepth: 1

    defaultsite
    filtered
    preview

