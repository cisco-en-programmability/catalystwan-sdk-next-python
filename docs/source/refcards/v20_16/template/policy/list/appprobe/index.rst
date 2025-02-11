=============================
template.policy.list.appprobe
=============================


Operation: GET /dataservice/template/policy/list/appprobe
---------------------------------------------------------


Get policy lists

.. code:: python

    def get_policy_lists_4() -> List[Any]: ...


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
        client.template.policy.list.appprobe.get_policy_lists_4()


Operation: POST /dataservice/template/policy/list/appprobe
----------------------------------------------------------


Create policy list

.. code:: python

    def create_policy_list_4(payload: Optional[Any] = None) -> Any: ...


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
        client.template.policy.list.appprobe.create_policy_list_4()


Operation: DELETE /dataservice/template/policy/list/appprobe
------------------------------------------------------------


Delete policy lists with specific info tag

.. code:: python

    def delete_policy_lists_with_info_tag_4(
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
        client.template.policy.list.appprobe.delete_policy_lists_with_info_tag_4()


Operation: GET /dataservice/template/policy/list/appprobe/{id}
--------------------------------------------------------------


Get a specific policy list based on the id

.. code:: python

    def get_lists_by_id_4(id: str) -> Any: ...


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
        client.template.policy.list.appprobe.get_lists_by_id_4()


Operation: PUT /dataservice/template/policy/list/appprobe/{id}
--------------------------------------------------------------


Edit policy list entries for a specific type of policy list

.. code:: python

    def edit_policy_list_4(
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
        client.template.policy.list.appprobe.edit_policy_list_4()


Operation: DELETE /dataservice/template/policy/list/appprobe/{id}
-----------------------------------------------------------------


Delete policy list entry for a specific type of policy list

.. code:: python

    def delete_policy_list_4(id: str) -> None: ...


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
        client.template.policy.list.appprobe.delete_policy_list_4()


.. toctree::
    :maxdepth: 1

    filtered
    preview

