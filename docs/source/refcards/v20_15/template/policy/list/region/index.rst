===========================
template.policy.list.region
===========================


Operation: GET /dataservice/template/policy/list/region
-------------------------------------------------------


Get policy lists

.. code:: python

    def get_policy_lists_28() -> List[Any]: ...


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
        client.template.policy.list.region.get_policy_lists_28()


Operation: POST /dataservice/template/policy/list/region
--------------------------------------------------------


Create policy list

.. code:: python

    def create_policy_list_31(payload: Optional[Any] = None) -> Any: ...


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
        client.template.policy.list.region.create_policy_list_31()


Operation: DELETE /dataservice/template/policy/list/region
----------------------------------------------------------


Delete policy lists with specific info tag

.. code:: python

    def delete_policy_lists_with_info_tag_31(
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
        client.template.policy.list.region.delete_policy_lists_with_info_tag_31()


Operation: GET /dataservice/template/policy/list/region/{id}
------------------------------------------------------------


Get a specific policy list based on the id

.. code:: python

    def get_lists_by_id_31(id: str) -> Any: ...


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
        client.template.policy.list.region.get_lists_by_id_31()


Operation: PUT /dataservice/template/policy/list/region/{id}
------------------------------------------------------------


Edit policy list entries for a specific type of policy list

.. code:: python

    def edit_policy_list_31(
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
        client.template.policy.list.region.edit_policy_list_31()


Operation: DELETE /dataservice/template/policy/list/region/{id}
---------------------------------------------------------------


Delete policy list entry for a specific type of policy list

.. code:: python

    def delete_policy_list_31(id: str) -> None: ...


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
        client.template.policy.list.region.delete_policy_list_31()


.. toctree::
    :maxdepth: 1

    filtered
    preview

