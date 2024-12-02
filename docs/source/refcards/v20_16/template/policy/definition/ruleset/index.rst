==================================
template.policy.definition.ruleset
==================================


Operation: GET /dataservice/template/policy/definition/ruleset
--------------------------------------------------------------


Get policy definitions

.. code:: python

    def get_definitions_20() -> Any: ...


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
        client.template.policy.definition.ruleset.get_definitions_20()


Operation: POST /dataservice/template/policy/definition/ruleset
---------------------------------------------------------------


Create policy definition

.. code:: python

    def create_policy_definition_20(
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
        client.template.policy.definition.ruleset.create_policy_definition_20()


Operation: GET /dataservice/template/policy/definition/ruleset/{id}
-------------------------------------------------------------------


Get a specific policy definitions

.. code:: python

    def get_policy_definition_20(id: str) -> Any: ...


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
        client.template.policy.definition.ruleset.get_policy_definition_20()


Operation: PUT /dataservice/template/policy/definition/ruleset/{id}
-------------------------------------------------------------------


Edit a policy definitions

.. code:: python

    def edit_policy_definition_20(
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
        client.template.policy.definition.ruleset.edit_policy_definition_20()


Operation: DELETE /dataservice/template/policy/definition/ruleset/{id}
----------------------------------------------------------------------


Delete policy definition

.. code:: python

    def delete_policy_definition_20(id: str) -> None: ...


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
        client.template.policy.definition.ruleset.delete_policy_definition_20()


.. toctree::
    :maxdepth: 1

    bulk
    multiple
    preview

