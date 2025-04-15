======================================
template.policy.definition.rewriterule
======================================


Operation: POST /dataservice/template/policy/definition/rewriterule
-------------------------------------------------------------------


Create policy definition

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
        client.template.policy.definition.rewriterule.post()


Operation: PUT /dataservice/template/policy/definition/rewriterule/{id}
-----------------------------------------------------------------------


Edit a policy definitions

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
        client.template.policy.definition.rewriterule.put()


Operation: DELETE /dataservice/template/policy/definition/rewriterule/{id}
--------------------------------------------------------------------------


Delete policy definition

.. code:: python

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
        client.template.policy.definition.rewriterule.delete()


Operation: GET /dataservice/template/policy/definition/rewriterule
------------------------------------------------------------------


.. code:: python

    @overload
    def get() -> Any: ...


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
        client.template.policy.definition.rewriterule.get()


Operation: GET /dataservice/template/policy/definition/rewriterule/{id}
-----------------------------------------------------------------------


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
        client.template.policy.definition.rewriterule.get()


.. toctree::
    :maxdepth: 1

    bulk
    multiple
    preview

