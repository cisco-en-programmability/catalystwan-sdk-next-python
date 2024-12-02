=================================
template.policy.definition.qosmap
=================================


Operation: GET /dataservice/template/policy/definition/qosmap
-------------------------------------------------------------


Get policy definitions

.. code:: python

    def get_definitions_1() -> Any: ...


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
        client.template.policy.definition.qosmap.get_definitions_1()


Operation: POST /dataservice/template/policy/definition/qosmap
--------------------------------------------------------------


Create policy definition

.. code:: python

    def create_policy_definition_1(
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
        client.template.policy.definition.qosmap.create_policy_definition_1()


Operation: GET /dataservice/template/policy/definition/qosmap/{id}
------------------------------------------------------------------


Get a specific policy definitions

.. code:: python

    def get_policy_definition_1(id: str) -> Any: ...


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
        client.template.policy.definition.qosmap.get_policy_definition_1()


Operation: PUT /dataservice/template/policy/definition/qosmap/{id}
------------------------------------------------------------------


Edit a policy definitions

.. code:: python

    def edit_policy_definition_1(
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
        client.template.policy.definition.qosmap.edit_policy_definition_1()


Operation: DELETE /dataservice/template/policy/definition/qosmap/{id}
---------------------------------------------------------------------


Delete policy definition

.. code:: python

    def delete_policy_definition_1(id: str) -> None: ...


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
        client.template.policy.definition.qosmap.delete_policy_definition_1()


.. toctree::
    :maxdepth: 1

    bulk
    multiple
    preview

