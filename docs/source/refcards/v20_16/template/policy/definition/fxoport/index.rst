==================================
template.policy.definition.fxoport
==================================


Operation: GET /dataservice/template/policy/definition/fxoport
--------------------------------------------------------------


Get policy definitions

.. code:: python

    def get_definitions_26() -> Any: ...


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
        client.template.policy.definition.fxoport.get_definitions_26()


Operation: POST /dataservice/template/policy/definition/fxoport
---------------------------------------------------------------


Create policy definition

.. code:: python

    def create_policy_definition_26(
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
        client.template.policy.definition.fxoport.create_policy_definition_26()


Operation: GET /dataservice/template/policy/definition/fxoport/{id}
-------------------------------------------------------------------


Get a specific policy definitions

.. code:: python

    def get_policy_definition_26(id: str) -> Any: ...


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
        client.template.policy.definition.fxoport.get_policy_definition_26()


Operation: PUT /dataservice/template/policy/definition/fxoport/{id}
-------------------------------------------------------------------


Edit a policy definitions

.. code:: python

    def edit_policy_definition_26(
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
        client.template.policy.definition.fxoport.edit_policy_definition_26()


Operation: DELETE /dataservice/template/policy/definition/fxoport/{id}
----------------------------------------------------------------------


Delete policy definition

.. code:: python

    def delete_policy_definition_26(id: str) -> None: ...


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
        client.template.policy.definition.fxoport.delete_policy_definition_26()


.. toctree::
    :maxdepth: 1

    bulk
    multiple
    preview

