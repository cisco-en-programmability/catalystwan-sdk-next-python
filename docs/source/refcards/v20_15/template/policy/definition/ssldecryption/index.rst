========================================
template.policy.definition.ssldecryption
========================================


Operation: POST /dataservice/template/policy/definition/ssldecryption
---------------------------------------------------------------------


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
        client.template.policy.definition.ssldecryption.post()


Operation: PUT /dataservice/template/policy/definition/ssldecryption/{id}
-------------------------------------------------------------------------


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
        client.template.policy.definition.ssldecryption.put()


Operation: DELETE /dataservice/template/policy/definition/ssldecryption/{id}
----------------------------------------------------------------------------


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
        client.template.policy.definition.ssldecryption.delete()


Operation: GET /dataservice/template/policy/definition/ssldecryption
--------------------------------------------------------------------


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
        client.template.policy.definition.ssldecryption.get()


Operation: GET /dataservice/template/policy/definition/ssldecryption/{id}
-------------------------------------------------------------------------


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
        client.template.policy.definition.ssldecryption.get()


.. toctree::
    :maxdepth: 1

    bulk
    multiple
    preview

