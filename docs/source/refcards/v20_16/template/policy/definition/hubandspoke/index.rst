======================================
template.policy.definition.hubandspoke
======================================


Operation: GET /dataservice/template/policy/definition/hubandspoke
------------------------------------------------------------------


Get policy definitions

.. code:: python

    def get_definitions_4() -> Any: ...


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
        client.template.policy.definition.hubandspoke.get_definitions_4()


Operation: POST /dataservice/template/policy/definition/hubandspoke
-------------------------------------------------------------------


Create policy definition

.. code:: python

    def create_policy_definition_4(
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
        client.template.policy.definition.hubandspoke.create_policy_definition_4()


Operation: GET /dataservice/template/policy/definition/hubandspoke/{id}
-----------------------------------------------------------------------


Get a specific policy definitions

.. code:: python

    def get_policy_definition_4(id: str) -> Any: ...


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
        client.template.policy.definition.hubandspoke.get_policy_definition_4()


Operation: PUT /dataservice/template/policy/definition/hubandspoke/{id}
-----------------------------------------------------------------------


Edit a policy definitions

.. code:: python

    def edit_policy_definition_4(
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
        client.template.policy.definition.hubandspoke.edit_policy_definition_4()


Operation: DELETE /dataservice/template/policy/definition/hubandspoke/{id}
--------------------------------------------------------------------------


Delete policy definition

.. code:: python

    def delete_policy_definition_4(id: str) -> None: ...


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
        client.template.policy.definition.hubandspoke.delete_policy_definition_4()


.. toctree::
    :maxdepth: 1

    bulk
    multiple
    preview

