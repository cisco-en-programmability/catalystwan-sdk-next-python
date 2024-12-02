=====================================
template.policy.definition.fxsdidport
=====================================


Operation: GET /dataservice/template/policy/definition/fxsdidport
-----------------------------------------------------------------


Get policy definitions

.. code:: python

    def get_definitions_28() -> Any: ...


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
        client.template.policy.definition.fxsdidport.get_definitions_28()


Operation: POST /dataservice/template/policy/definition/fxsdidport
------------------------------------------------------------------


Create policy definition

.. code:: python

    def create_policy_definition_28(
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
        client.template.policy.definition.fxsdidport.create_policy_definition_28()


Operation: GET /dataservice/template/policy/definition/fxsdidport/{id}
----------------------------------------------------------------------


Get a specific policy definitions

.. code:: python

    def get_policy_definition_28(id: str) -> Any: ...


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
        client.template.policy.definition.fxsdidport.get_policy_definition_28()


Operation: PUT /dataservice/template/policy/definition/fxsdidport/{id}
----------------------------------------------------------------------


Edit a policy definitions

.. code:: python

    def edit_policy_definition_28(
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
        client.template.policy.definition.fxsdidport.edit_policy_definition_28()


Operation: DELETE /dataservice/template/policy/definition/fxsdidport/{id}
-------------------------------------------------------------------------


Delete policy definition

.. code:: python

    def delete_policy_definition_28(id: str) -> None: ...


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
        client.template.policy.definition.fxsdidport.delete_policy_definition_28()


.. toctree::
    :maxdepth: 1

    bulk
    multiple
    preview

