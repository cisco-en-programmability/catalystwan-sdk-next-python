=======================================
template.policy.definition.urlfiltering
=======================================


Operation: GET /dataservice/template/policy/definition/urlfiltering
-------------------------------------------------------------------


Get policy definitions

.. code:: python

    def get_definitions_23() -> Any: ...


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
        client.template.policy.definition.urlfiltering.get_definitions_23()


Operation: POST /dataservice/template/policy/definition/urlfiltering
--------------------------------------------------------------------


Create policy definition

.. code:: python

    def create_policy_definition_23(
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
        client.template.policy.definition.urlfiltering.create_policy_definition_23()


Operation: GET /dataservice/template/policy/definition/urlfiltering/{id}
------------------------------------------------------------------------


Get a specific policy definitions

.. code:: python

    def get_policy_definition_23(id: str) -> Any: ...


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
        client.template.policy.definition.urlfiltering.get_policy_definition_23()


Operation: PUT /dataservice/template/policy/definition/urlfiltering/{id}
------------------------------------------------------------------------


Edit a policy definitions

.. code:: python

    def edit_policy_definition_23(
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
        client.template.policy.definition.urlfiltering.edit_policy_definition_23()


Operation: DELETE /dataservice/template/policy/definition/urlfiltering/{id}
---------------------------------------------------------------------------


Delete policy definition

.. code:: python

    def delete_policy_definition_23(id: str) -> None: ...


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
        client.template.policy.definition.urlfiltering.delete_policy_definition_23()


.. toctree::
    :maxdepth: 1

    bulk
    multiple
    preview

