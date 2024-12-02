===================================
template.policy.definition.approute
===================================


Operation: GET /dataservice/template/policy/definition/approute
---------------------------------------------------------------


Get policy definitions

.. code:: python

    def get_definitions_12() -> Any: ...


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
        client.template.policy.definition.approute.get_definitions_12()


Operation: POST /dataservice/template/policy/definition/approute
----------------------------------------------------------------


Create policy definition

.. code:: python

    def create_policy_definition_12(
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
        client.template.policy.definition.approute.create_policy_definition_12()


Operation: GET /dataservice/template/policy/definition/approute/{id}
--------------------------------------------------------------------


Get a specific policy definitions

.. code:: python

    def get_policy_definition_12(id: str) -> Any: ...


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
        client.template.policy.definition.approute.get_policy_definition_12()


Operation: PUT /dataservice/template/policy/definition/approute/{id}
--------------------------------------------------------------------


Edit a policy definitions

.. code:: python

    def edit_policy_definition_12(
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
        client.template.policy.definition.approute.edit_policy_definition_12()


Operation: DELETE /dataservice/template/policy/definition/approute/{id}
-----------------------------------------------------------------------


Delete policy definition

.. code:: python

    def delete_policy_definition_12(id: str) -> None: ...


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
        client.template.policy.definition.approute.delete_policy_definition_12()


.. toctree::
    :maxdepth: 1

    bulk
    multiple
    preview

