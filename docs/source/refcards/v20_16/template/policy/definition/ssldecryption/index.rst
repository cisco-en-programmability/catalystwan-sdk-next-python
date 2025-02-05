========================================
template.policy.definition.ssldecryption
========================================


Operation: GET /dataservice/template/policy/definition/ssldecryption
--------------------------------------------------------------------


Get policy definitions

.. code:: python

    def get_definitions_3() -> Any: ...


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
        client.template.policy.definition.ssldecryption.get_definitions_3()


Operation: POST /dataservice/template/policy/definition/ssldecryption
---------------------------------------------------------------------


Create policy definition

.. code:: python

    def create_policy_definition_3(
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
        client.template.policy.definition.ssldecryption.create_policy_definition_3()


Operation: GET /dataservice/template/policy/definition/ssldecryption/{id}
-------------------------------------------------------------------------


Get a specific policy definitions

.. code:: python

    def get_policy_definition_3(id: str) -> Any: ...


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
        client.template.policy.definition.ssldecryption.get_policy_definition_3()


Operation: PUT /dataservice/template/policy/definition/ssldecryption/{id}
-------------------------------------------------------------------------


Edit a policy definitions

.. code:: python

    def edit_policy_definition_3(
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
        client.template.policy.definition.ssldecryption.edit_policy_definition_3()


Operation: DELETE /dataservice/template/policy/definition/ssldecryption/{id}
----------------------------------------------------------------------------


Delete policy definition

.. code:: python

    def delete_policy_definition_3(id: str) -> None: ...


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
        client.template.policy.definition.ssldecryption.delete_policy_definition_3()


.. toctree::
    :maxdepth: 1

    bulk
    multiple
    preview

