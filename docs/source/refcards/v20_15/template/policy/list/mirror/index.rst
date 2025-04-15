===========================
template.policy.list.mirror
===========================


Operation: POST /dataservice/template/policy/list/mirror
--------------------------------------------------------


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
        client.template.policy.list.mirror.post()


Operation: PUT /dataservice/template/policy/list/mirror/{id}
------------------------------------------------------------


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
        client.template.policy.list.mirror.put()


Operation: GET /dataservice/template/policy/list/mirror
-------------------------------------------------------


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
        client.template.policy.list.mirror.get()


Operation: GET /dataservice/template/policy/list/mirror/{id}
------------------------------------------------------------


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
        client.template.policy.list.mirror.get()


Operation: DELETE /dataservice/template/policy/list/mirror
----------------------------------------------------------


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
        client.template.policy.list.mirror.delete()


Operation: DELETE /dataservice/template/policy/list/mirror/{id}
---------------------------------------------------------------


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
        client.template.policy.list.mirror.delete()


.. toctree::
    :maxdepth: 1

    filtered
    preview

