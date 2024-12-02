======================================
template.policy.definition.zonebasedfw
======================================


Operation: GET /dataservice/template/policy/definition/zonebasedfw
------------------------------------------------------------------


Get policy definitions

.. code:: python

    def get_definitions_7() -> Any: ...


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
        client.template.policy.definition.zonebasedfw.get_definitions_7()


Operation: POST /dataservice/template/policy/definition/zonebasedfw
-------------------------------------------------------------------


Create policy definition

.. code:: python

    def create_policy_definition_7(
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
        client.template.policy.definition.zonebasedfw.create_policy_definition_7()


Operation: GET /dataservice/template/policy/definition/zonebasedfw/{id}
-----------------------------------------------------------------------


Get a specific policy definitions

.. code:: python

    def get_policy_definition_7(id: str) -> Any: ...


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
        client.template.policy.definition.zonebasedfw.get_policy_definition_7()


Operation: PUT /dataservice/template/policy/definition/zonebasedfw/{id}
-----------------------------------------------------------------------


Edit a policy definitions

.. code:: python

    def edit_policy_definition_7(
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
        client.template.policy.definition.zonebasedfw.edit_policy_definition_7()


Operation: DELETE /dataservice/template/policy/definition/zonebasedfw/{id}
--------------------------------------------------------------------------


Delete policy definition

.. code:: python

    def delete_policy_definition_7(id: str) -> None: ...


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
        client.template.policy.definition.zonebasedfw.delete_policy_definition_7()


.. toctree::
    :maxdepth: 1

    bulk
    multiple
    preview

