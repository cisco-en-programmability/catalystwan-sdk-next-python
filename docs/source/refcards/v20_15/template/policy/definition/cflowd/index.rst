=================================
template.policy.definition.cflowd
=================================


Operation: GET /dataservice/template/policy/definition/cflowd
-------------------------------------------------------------


Get policy definitions

.. code:: python

    def get_definitions_13() -> Any: ...


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
        client.template.policy.definition.cflowd.get_definitions_13()


Operation: POST /dataservice/template/policy/definition/cflowd
--------------------------------------------------------------


Create policy definition

.. code:: python

    def create_policy_definition_13(
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
        client.template.policy.definition.cflowd.create_policy_definition_13()


Operation: GET /dataservice/template/policy/definition/cflowd/{id}
------------------------------------------------------------------


Get a specific policy definitions

.. code:: python

    def get_policy_definition_13(id: str) -> Any: ...


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
        client.template.policy.definition.cflowd.get_policy_definition_13()


Operation: PUT /dataservice/template/policy/definition/cflowd/{id}
------------------------------------------------------------------


Edit a policy definitions

.. code:: python

    def edit_policy_definition_13(
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
        client.template.policy.definition.cflowd.edit_policy_definition_13()


Operation: DELETE /dataservice/template/policy/definition/cflowd/{id}
---------------------------------------------------------------------


Delete policy definition

.. code:: python

    def delete_policy_definition_13(id: str) -> None: ...


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
        client.template.policy.definition.cflowd.delete_policy_definition_13()


.. toctree::
    :maxdepth: 1

    bulk
    multiple
    preview

