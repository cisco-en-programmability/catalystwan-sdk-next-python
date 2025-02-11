=============================
template.policy.list.tgapikey
=============================


Operation: GET /dataservice/template/policy/list/tgapikey
---------------------------------------------------------


Get policy lists

.. code:: python

    def get_policy_lists_33() -> List[Any]: ...


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
        client.template.policy.list.tgapikey.get_policy_lists_33()


Operation: POST /dataservice/template/policy/list/tgapikey
----------------------------------------------------------


Create policy list

.. code:: python

    def create_policy_list_36(payload: Optional[Any] = None) -> Any: ...


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
        client.template.policy.list.tgapikey.create_policy_list_36()


Operation: DELETE /dataservice/template/policy/list/tgapikey
------------------------------------------------------------


Delete policy lists with specific info tag

.. code:: python

    def delete_policy_lists_with_info_tag_36(
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
        client.template.policy.list.tgapikey.delete_policy_lists_with_info_tag_36()


Operation: GET /dataservice/template/policy/list/tgapikey/{id}
--------------------------------------------------------------


Get a specific policy list based on the id

.. code:: python

    def get_lists_by_id_36(id: str) -> Any: ...


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
        client.template.policy.list.tgapikey.get_lists_by_id_36()


Operation: PUT /dataservice/template/policy/list/tgapikey/{id}
--------------------------------------------------------------


Edit policy list entries for a specific type of policy list

.. code:: python

    def edit_policy_list_36(
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
        client.template.policy.list.tgapikey.edit_policy_list_36()


Operation: DELETE /dataservice/template/policy/list/tgapikey/{id}
-----------------------------------------------------------------


Delete policy list entry for a specific type of policy list

.. code:: python

    def delete_policy_list_36(id: str) -> None: ...


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
        client.template.policy.list.tgapikey.delete_policy_list_36()


.. toctree::
    :maxdepth: 1

    filtered
    preview

