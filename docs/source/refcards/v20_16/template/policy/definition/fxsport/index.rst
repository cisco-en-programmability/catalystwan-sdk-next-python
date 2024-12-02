==================================
template.policy.definition.fxsport
==================================


Operation: GET /dataservice/template/policy/definition/fxsport
--------------------------------------------------------------


Get policy definitions

.. code:: python

    def get_definitions_27() -> Any: ...


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
        client.template.policy.definition.fxsport.get_definitions_27()


Operation: POST /dataservice/template/policy/definition/fxsport
---------------------------------------------------------------


Create policy definition

.. code:: python

    def create_policy_definition_27(
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
        client.template.policy.definition.fxsport.create_policy_definition_27()


Operation: GET /dataservice/template/policy/definition/fxsport/{id}
-------------------------------------------------------------------


Get a specific policy definitions

.. code:: python

    def get_policy_definition_27(id: str) -> Any: ...


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
        client.template.policy.definition.fxsport.get_policy_definition_27()


Operation: PUT /dataservice/template/policy/definition/fxsport/{id}
-------------------------------------------------------------------


Edit a policy definitions

.. code:: python

    def edit_policy_definition_27(
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
        client.template.policy.definition.fxsport.edit_policy_definition_27()


Operation: DELETE /dataservice/template/policy/definition/fxsport/{id}
----------------------------------------------------------------------


Delete policy definition

.. code:: python

    def delete_policy_definition_27(id: str) -> None: ...


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
        client.template.policy.definition.fxsport.delete_policy_definition_27()


.. toctree::
    :maxdepth: 1

    bulk
    multiple
    preview

