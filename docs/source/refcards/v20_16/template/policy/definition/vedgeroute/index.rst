=====================================
template.policy.definition.vedgeroute
=====================================


Operation: GET /dataservice/template/policy/definition/vedgeroute
-----------------------------------------------------------------


Get policy definitions

.. code:: python

    def get_definitions_24() -> Any: ...


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
        client.template.policy.definition.vedgeroute.get_definitions_24()


Operation: POST /dataservice/template/policy/definition/vedgeroute
------------------------------------------------------------------


Create policy definition

.. code:: python

    def create_policy_definition_24(
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
        client.template.policy.definition.vedgeroute.create_policy_definition_24()


Operation: GET /dataservice/template/policy/definition/vedgeroute/{id}
----------------------------------------------------------------------


Get a specific policy definitions

.. code:: python

    def get_policy_definition_24(id: str) -> Any: ...


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
        client.template.policy.definition.vedgeroute.get_policy_definition_24()


Operation: PUT /dataservice/template/policy/definition/vedgeroute/{id}
----------------------------------------------------------------------


Edit a policy definitions

.. code:: python

    def edit_policy_definition_24(
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
        client.template.policy.definition.vedgeroute.edit_policy_definition_24()


Operation: DELETE /dataservice/template/policy/definition/vedgeroute/{id}
-------------------------------------------------------------------------


Delete policy definition

.. code:: python

    def delete_policy_definition_24(id: str) -> None: ...


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
        client.template.policy.definition.vedgeroute.delete_policy_definition_24()


.. toctree::
    :maxdepth: 1

    bulk
    multiple
    preview

