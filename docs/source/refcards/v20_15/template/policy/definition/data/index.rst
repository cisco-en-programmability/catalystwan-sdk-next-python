===============================
template.policy.definition.data
===============================


Operation: GET /dataservice/template/policy/definition/data
-----------------------------------------------------------


Get policy definitions

.. code:: python

    def get_definitions_15() -> Any: ...


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
        client.template.policy.definition.data.get_definitions_15()


Operation: POST /dataservice/template/policy/definition/data
------------------------------------------------------------


Create policy definition

.. code:: python

    def create_policy_definition_15(
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
        client.template.policy.definition.data.create_policy_definition_15()


Operation: GET /dataservice/template/policy/definition/data/{id}
----------------------------------------------------------------


Get a specific policy definitions

.. code:: python

    def get_policy_definition_15(id: str) -> Any: ...


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
        client.template.policy.definition.data.get_policy_definition_15()


Operation: PUT /dataservice/template/policy/definition/data/{id}
----------------------------------------------------------------


Edit a policy definitions

.. code:: python

    def edit_policy_definition_15(
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
        client.template.policy.definition.data.edit_policy_definition_15()


Operation: DELETE /dataservice/template/policy/definition/data/{id}
-------------------------------------------------------------------


Delete policy definition

.. code:: python

    def delete_policy_definition_15(id: str) -> None: ...


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
        client.template.policy.definition.data.delete_policy_definition_15()


.. toctree::
    :maxdepth: 1

    bulk
    multiple
    preview

