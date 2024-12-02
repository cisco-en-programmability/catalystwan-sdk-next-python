===============================
template.policy.definition.mesh
===============================


Operation: GET /dataservice/template/policy/definition/mesh
-----------------------------------------------------------


Get policy definitions

.. code:: python

    def get_definitions_5() -> Any: ...


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
        client.template.policy.definition.mesh.get_definitions_5()


Operation: POST /dataservice/template/policy/definition/mesh
------------------------------------------------------------


Create policy definition

.. code:: python

    def create_policy_definition_5(
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
        client.template.policy.definition.mesh.create_policy_definition_5()


Operation: GET /dataservice/template/policy/definition/mesh/{id}
----------------------------------------------------------------


Get a specific policy definitions

.. code:: python

    def get_policy_definition_5(id: str) -> Any: ...


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
        client.template.policy.definition.mesh.get_policy_definition_5()


Operation: PUT /dataservice/template/policy/definition/mesh/{id}
----------------------------------------------------------------


Edit a policy definitions

.. code:: python

    def edit_policy_definition_5(
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
        client.template.policy.definition.mesh.edit_policy_definition_5()


Operation: DELETE /dataservice/template/policy/definition/mesh/{id}
-------------------------------------------------------------------


Delete policy definition

.. code:: python

    def delete_policy_definition_5(id: str) -> None: ...


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
        client.template.policy.definition.mesh.delete_policy_definition_5()


.. toctree::
    :maxdepth: 1

    bulk
    multiple
    preview

