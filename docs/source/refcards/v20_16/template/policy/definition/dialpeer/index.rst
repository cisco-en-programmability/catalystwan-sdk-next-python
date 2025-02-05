===================================
template.policy.definition.dialpeer
===================================


Operation: GET /dataservice/template/policy/definition/dialpeer
---------------------------------------------------------------


Get policy definitions

.. code:: python

    def get_definitions_25() -> Any: ...


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
        client.template.policy.definition.dialpeer.get_definitions_25()


Operation: POST /dataservice/template/policy/definition/dialpeer
----------------------------------------------------------------


Create policy definition

.. code:: python

    def create_policy_definition_25(
        payload: Optional[Any] = None,
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
        client.template.policy.definition.dialpeer.create_policy_definition_25()


Operation: GET /dataservice/template/policy/definition/dialpeer/{id}
--------------------------------------------------------------------


Get a specific policy definitions

.. code:: python

    def get_policy_definition_25(id: str) -> Any: ...


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
        client.template.policy.definition.dialpeer.get_policy_definition_25()


Operation: PUT /dataservice/template/policy/definition/dialpeer/{id}
--------------------------------------------------------------------


Edit a policy definitions

.. code:: python

    def edit_policy_definition_25(
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
        client.template.policy.definition.dialpeer.edit_policy_definition_25()


Operation: DELETE /dataservice/template/policy/definition/dialpeer/{id}
-----------------------------------------------------------------------


Delete policy definition

.. code:: python

    def delete_policy_definition_25(id: str) -> None: ...


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
        client.template.policy.definition.dialpeer.delete_policy_definition_25()


.. toctree::
    :maxdepth: 1

    bulk
    multiple
    preview

