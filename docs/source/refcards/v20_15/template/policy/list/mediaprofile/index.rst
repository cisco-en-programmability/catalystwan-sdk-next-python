=================================
template.policy.list.mediaprofile
=================================


Operation: GET /dataservice/template/policy/list/mediaprofile
-------------------------------------------------------------


Get policy lists

.. code:: python

    def get_policy_lists() -> List[Any]: ...


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
        client.template.policy.list.mediaprofile.get_policy_lists()


Operation: POST /dataservice/template/policy/list/mediaprofile
--------------------------------------------------------------


Create policy list

.. code:: python

    def create_policy_list(payload: Optional[Any] = None) -> Any: ...


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
        client.template.policy.list.mediaprofile.create_policy_list()


Operation: DELETE /dataservice/template/policy/list/mediaprofile
----------------------------------------------------------------


Delete policy lists with specific info tag

.. code:: python

    def delete_policy_lists_with_info_tag(
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
        client.template.policy.list.mediaprofile.delete_policy_lists_with_info_tag()


Operation: GET /dataservice/template/policy/list/mediaprofile/{id}
------------------------------------------------------------------


Get a specific policy list based on the id

.. code:: python

    def get_lists_by_id(id: str) -> Any: ...


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
        client.template.policy.list.mediaprofile.get_lists_by_id()


Operation: PUT /dataservice/template/policy/list/mediaprofile/{id}
------------------------------------------------------------------


Edit policy list entries for a specific type of policy list

.. code:: python

    def edit_policy_list(
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
        client.template.policy.list.mediaprofile.edit_policy_list()


Operation: DELETE /dataservice/template/policy/list/mediaprofile/{id}
---------------------------------------------------------------------


Delete policy list entry for a specific type of policy list

.. code:: python

    def delete_policy_list(id: str) -> None: ...


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
        client.template.policy.list.mediaprofile.delete_policy_list()


.. toctree::
    :maxdepth: 1

    filtered
    preview

