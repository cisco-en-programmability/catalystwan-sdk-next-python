================================
template.policy.definition.aclv6
================================


Operation: GET /dataservice/template/policy/definition/aclv6
------------------------------------------------------------


Get policy definitions

.. code:: python

    def get_definitions_9() -> Any: ...


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
        client.template.policy.definition.aclv6.get_definitions_9()


Operation: POST /dataservice/template/policy/definition/aclv6
-------------------------------------------------------------


Create policy definition

.. code:: python

    def create_policy_definition_9(
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
        client.template.policy.definition.aclv6.create_policy_definition_9()


Operation: GET /dataservice/template/policy/definition/aclv6/{id}
-----------------------------------------------------------------


Get a specific policy definitions

.. code:: python

    def get_policy_definition_9(id: str) -> Any: ...


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
        client.template.policy.definition.aclv6.get_policy_definition_9()


Operation: PUT /dataservice/template/policy/definition/aclv6/{id}
-----------------------------------------------------------------


Edit a policy definitions

.. code:: python

    def edit_policy_definition_9(
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
        client.template.policy.definition.aclv6.edit_policy_definition_9()


Operation: DELETE /dataservice/template/policy/definition/aclv6/{id}
--------------------------------------------------------------------


Delete policy definition

.. code:: python

    def delete_policy_definition_9(id: str) -> None: ...


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
        client.template.policy.definition.aclv6.delete_policy_definition_9()


.. toctree::
    :maxdepth: 1

    bulk
    multiple
    preview

