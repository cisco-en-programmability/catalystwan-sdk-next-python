=======================================
template.policy.list.translationprofile
=======================================


Operation: POST /dataservice/template/policy/list/translationprofile
--------------------------------------------------------------------


Create policy list

.. code:: python

    def post(payload: Any) -> Any: ...


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
        client.template.policy.list.translationprofile.post()


Operation: PUT /dataservice/template/policy/list/translationprofile/{id}
------------------------------------------------------------------------


Edit policy list entries for a specific type of policy list

.. code:: python

    def put(id: str, payload: Any) -> Any: ...


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
        client.template.policy.list.translationprofile.put()


Operation: GET /dataservice/template/policy/list/translationprofile
-------------------------------------------------------------------


.. code:: python

    @overload
    def get() -> List[Any]: ...


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
        client.template.policy.list.translationprofile.get()


Operation: GET /dataservice/template/policy/list/translationprofile/{id}
------------------------------------------------------------------------


.. code:: python

    @overload
    def get(id: str) -> Any: ...


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
        client.template.policy.list.translationprofile.get()


Operation: DELETE /dataservice/template/policy/list/translationprofile
----------------------------------------------------------------------


.. code:: python

    @overload
    def delete(info_tag: Optional[str] = None) -> List[Any]: ...


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
        client.template.policy.list.translationprofile.delete()


Operation: DELETE /dataservice/template/policy/list/translationprofile/{id}
---------------------------------------------------------------------------


.. code:: python

    @overload
    def delete(id: str) -> None: ...


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
        client.template.policy.list.translationprofile.delete()


.. toctree::
    :maxdepth: 1

    filtered
    preview

