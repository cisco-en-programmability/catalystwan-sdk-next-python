========================================
template.policy.definition.securitygroup
========================================


Operation: GET /dataservice/template/policy/definition/securitygroup
--------------------------------------------------------------------


Get policy definitions

.. code:: python

    def get_definitions_21() -> Any: ...


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
        client.template.policy.definition.securitygroup.get_definitions_21()


Operation: POST /dataservice/template/policy/definition/securitygroup
---------------------------------------------------------------------


Create policy definition

.. code:: python

    def create_policy_definition_21(
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
        client.template.policy.definition.securitygroup.create_policy_definition_21()


Operation: GET /dataservice/template/policy/definition/securitygroup/{id}
-------------------------------------------------------------------------


Get a specific policy definitions

.. code:: python

    def get_policy_definition_21(id: str) -> Any: ...


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
        client.template.policy.definition.securitygroup.get_policy_definition_21()


Operation: PUT /dataservice/template/policy/definition/securitygroup/{id}
-------------------------------------------------------------------------


Edit a policy definitions

.. code:: python

    def edit_policy_definition_21(
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
        client.template.policy.definition.securitygroup.edit_policy_definition_21()


Operation: DELETE /dataservice/template/policy/definition/securitygroup/{id}
----------------------------------------------------------------------------


Delete policy definition

.. code:: python

    def delete_policy_definition_21(id: str) -> None: ...


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
        client.template.policy.definition.securitygroup.delete_policy_definition_21()


.. toctree::
    :maxdepth: 1

    bulk
    multiple
    preview

