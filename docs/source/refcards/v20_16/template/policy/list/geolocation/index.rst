================================
template.policy.list.geolocation
================================


Operation: GET /dataservice/template/policy/list/geolocation
------------------------------------------------------------


Get policy lists

.. code:: python

    def get_policy_lists_15() -> List[Any]: ...


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
        client.template.policy.list.geolocation.get_policy_lists_15()


Operation: POST /dataservice/template/policy/list/geolocation
-------------------------------------------------------------


Create policy list

.. code:: python

    def create_policy_list_17(payload: Optional[Any] = None) -> Any: ...


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
        client.template.policy.list.geolocation.create_policy_list_17()


Operation: DELETE /dataservice/template/policy/list/geolocation
---------------------------------------------------------------


Delete policy lists with specific info tag

.. code:: python

    def delete_policy_lists_with_info_tag_17(
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
        client.template.policy.list.geolocation.delete_policy_lists_with_info_tag_17()


Operation: GET /dataservice/template/policy/list/geolocation/{id}
-----------------------------------------------------------------


Get a specific policy list based on the id

.. code:: python

    def get_lists_by_id_17(id: str) -> Any: ...


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
        client.template.policy.list.geolocation.get_lists_by_id_17()


Operation: PUT /dataservice/template/policy/list/geolocation/{id}
-----------------------------------------------------------------


Edit policy list entries for a specific type of policy list

.. code:: python

    def edit_policy_list_17(
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
        client.template.policy.list.geolocation.edit_policy_list_17()


Operation: DELETE /dataservice/template/policy/list/geolocation/{id}
--------------------------------------------------------------------


Delete policy list entry for a specific type of policy list

.. code:: python

    def delete_policy_list_17(id: str) -> None: ...


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
        client.template.policy.list.geolocation.delete_policy_list_17()


.. toctree::
    :maxdepth: 1

    entries
    filtered
    preview

