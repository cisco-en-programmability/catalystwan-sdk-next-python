==============================
template.policy.definition.acl
==============================


Operation: GET /dataservice/template/policy/definition/acl
----------------------------------------------------------


Get policy definitions

.. code:: python

    def get_definitions_8() -> Any: ...


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
        client.template.policy.definition.acl.get_definitions_8()


Operation: POST /dataservice/template/policy/definition/acl
-----------------------------------------------------------


Create policy definition

.. code:: python

    def create_policy_definition_8(
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
        client.template.policy.definition.acl.create_policy_definition_8()


Operation: GET /dataservice/template/policy/definition/acl/{id}
---------------------------------------------------------------


Get a specific policy definitions

.. code:: python

    def get_policy_definition_8(id: str) -> Any: ...


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
        client.template.policy.definition.acl.get_policy_definition_8()


Operation: PUT /dataservice/template/policy/definition/acl/{id}
---------------------------------------------------------------


Edit a policy definitions

.. code:: python

    def edit_policy_definition_8(
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
        client.template.policy.definition.acl.edit_policy_definition_8()


Operation: DELETE /dataservice/template/policy/definition/acl/{id}
------------------------------------------------------------------


Delete policy definition

.. code:: python

    def delete_policy_definition_8(id: str) -> None: ...


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
        client.template.policy.definition.acl.delete_policy_definition_8()


.. toctree::
    :maxdepth: 1

    bulk
    multiple
    preview

