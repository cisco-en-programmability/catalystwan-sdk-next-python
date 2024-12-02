==================================
template.policy.definition.control
==================================


Operation: GET /dataservice/template/policy/definition/control
--------------------------------------------------------------


Get policy definitions

.. code:: python

    def get_definitions_14() -> Any: ...


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
        client.template.policy.definition.control.get_definitions_14()


Operation: POST /dataservice/template/policy/definition/control
---------------------------------------------------------------


Create policy definition

.. code:: python

    def create_policy_definition_14(
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
        client.template.policy.definition.control.create_policy_definition_14()


Operation: GET /dataservice/template/policy/definition/control/{id}
-------------------------------------------------------------------


Get a specific policy definitions

.. code:: python

    def get_policy_definition_14(id: str) -> Any: ...


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
        client.template.policy.definition.control.get_policy_definition_14()


Operation: PUT /dataservice/template/policy/definition/control/{id}
-------------------------------------------------------------------


Edit a policy definitions

.. code:: python

    def edit_policy_definition_14(
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
        client.template.policy.definition.control.edit_policy_definition_14()


Operation: DELETE /dataservice/template/policy/definition/control/{id}
----------------------------------------------------------------------


Delete policy definition

.. code:: python

    def delete_policy_definition_14(id: str) -> None: ...


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
        client.template.policy.definition.control.delete_policy_definition_14()


.. toctree::
    :maxdepth: 1

    bulk
    multiple
    preview

