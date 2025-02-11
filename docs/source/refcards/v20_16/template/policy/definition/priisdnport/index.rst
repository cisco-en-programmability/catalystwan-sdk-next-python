======================================
template.policy.definition.priisdnport
======================================


Operation: GET /dataservice/template/policy/definition/priisdnport
------------------------------------------------------------------


Get policy definitions

.. code:: python

    def get_definitions_29() -> Any: ...


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
        client.template.policy.definition.priisdnport.get_definitions_29()


Operation: POST /dataservice/template/policy/definition/priisdnport
-------------------------------------------------------------------


Create policy definition

.. code:: python

    def create_policy_definition_29(
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
        client.template.policy.definition.priisdnport.create_policy_definition_29()


Operation: GET /dataservice/template/policy/definition/priisdnport/{id}
-----------------------------------------------------------------------


Get a specific policy definitions

.. code:: python

    def get_policy_definition_29(id: str) -> Any: ...


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
        client.template.policy.definition.priisdnport.get_policy_definition_29()


Operation: PUT /dataservice/template/policy/definition/priisdnport/{id}
-----------------------------------------------------------------------


Edit a policy definitions

.. code:: python

    def edit_policy_definition_29(
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
        client.template.policy.definition.priisdnport.edit_policy_definition_29()


Operation: DELETE /dataservice/template/policy/definition/priisdnport/{id}
--------------------------------------------------------------------------


Delete policy definition

.. code:: python

    def delete_policy_definition_29(id: str) -> None: ...


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
        client.template.policy.definition.priisdnport.delete_policy_definition_29()


.. toctree::
    :maxdepth: 1

    bulk
    multiple
    preview

