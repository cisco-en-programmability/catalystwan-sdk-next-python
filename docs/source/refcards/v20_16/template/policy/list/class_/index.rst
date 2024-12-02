===========================
template.policy.list.class_
===========================


Operation: GET /dataservice/template/policy/list/class
------------------------------------------------------


Get policy lists

.. code:: python

    def get_policy_lists_13() -> List[Any]: ...


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
        client.template.policy.list.class_.get_policy_lists_13()


Operation: POST /dataservice/template/policy/list/class
-------------------------------------------------------


Create policy list

.. code:: python

    def create_policy_list_14(payload: Optional[Any] = None) -> Any: ...


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
        client.template.policy.list.class_.create_policy_list_14()


Operation: DELETE /dataservice/template/policy/list/class
---------------------------------------------------------


Delete policy lists with specific info tag

.. code:: python

    def delete_policy_lists_with_info_tag_14(
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
        client.template.policy.list.class_.delete_policy_lists_with_info_tag_14()


Operation: GET /dataservice/template/policy/list/class/{id}
-----------------------------------------------------------


Get a specific policy list based on the id

.. code:: python

    def get_lists_by_id_14(id: str) -> Any: ...


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
        client.template.policy.list.class_.get_lists_by_id_14()


Operation: PUT /dataservice/template/policy/list/class/{id}
-----------------------------------------------------------


Edit policy list entries for a specific type of policy list

.. code:: python

    def edit_policy_list_14(
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
        client.template.policy.list.class_.edit_policy_list_14()


Operation: DELETE /dataservice/template/policy/list/class/{id}
--------------------------------------------------------------


Delete policy list entry for a specific type of policy list

.. code:: python

    def delete_policy_list_14(id: str) -> None: ...


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
        client.template.policy.list.class_.delete_policy_list_14()


.. toctree::
    :maxdepth: 1

    filtered
    preview

