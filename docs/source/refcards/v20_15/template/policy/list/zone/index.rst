=========================
template.policy.list.zone
=========================


Operation: GET /dataservice/template/policy/list/zone
-----------------------------------------------------


Get policy lists

.. code:: python

    def get_policy_lists_40() -> List[Any]: ...


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
        client.template.policy.list.zone.get_policy_lists_40()


Operation: POST /dataservice/template/policy/list/zone
------------------------------------------------------


Create policy list

.. code:: python

    def create_policy_list_43(payload: Optional[Any] = None) -> Any: ...


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
        client.template.policy.list.zone.create_policy_list_43()


Operation: DELETE /dataservice/template/policy/list/zone
--------------------------------------------------------


Delete policy lists with specific info tag

.. code:: python

    def delete_policy_lists_with_info_tag_43(
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
        client.template.policy.list.zone.delete_policy_lists_with_info_tag_43()


Operation: GET /dataservice/template/policy/list/zone/{id}
----------------------------------------------------------


Get a specific policy list based on the id

.. code:: python

    def get_lists_by_id_43(id: str) -> Any: ...


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
        client.template.policy.list.zone.get_lists_by_id_43()


Operation: PUT /dataservice/template/policy/list/zone/{id}
----------------------------------------------------------


Edit policy list entries for a specific type of policy list

.. code:: python

    def edit_policy_list_43(
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
        client.template.policy.list.zone.edit_policy_list_43()


Operation: DELETE /dataservice/template/policy/list/zone/{id}
-------------------------------------------------------------


Delete policy list entry for a specific type of policy list

.. code:: python

    def delete_policy_list_43(id: str) -> None: ...


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
        client.template.policy.list.zone.delete_policy_list_43()


.. toctree::
    :maxdepth: 1

    filtered
    preview

