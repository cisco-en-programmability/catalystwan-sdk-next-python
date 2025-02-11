======================================
template.policy.definition.rewriterule
======================================


Operation: GET /dataservice/template/policy/definition/rewriterule
------------------------------------------------------------------


Get policy definitions

.. code:: python

    def get_definitions_19() -> Any: ...


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
        client.template.policy.definition.rewriterule.get_definitions_19()


Operation: POST /dataservice/template/policy/definition/rewriterule
-------------------------------------------------------------------


Create policy definition

.. code:: python

    def create_policy_definition_19(
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
        client.template.policy.definition.rewriterule.create_policy_definition_19()


Operation: GET /dataservice/template/policy/definition/rewriterule/{id}
-----------------------------------------------------------------------


Get a specific policy definitions

.. code:: python

    def get_policy_definition_19(id: str) -> Any: ...


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
        client.template.policy.definition.rewriterule.get_policy_definition_19()


Operation: PUT /dataservice/template/policy/definition/rewriterule/{id}
-----------------------------------------------------------------------


Edit a policy definitions

.. code:: python

    def edit_policy_definition_19(
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
        client.template.policy.definition.rewriterule.edit_policy_definition_19()


Operation: DELETE /dataservice/template/policy/definition/rewriterule/{id}
--------------------------------------------------------------------------


Delete policy definition

.. code:: python

    def delete_policy_definition_19(id: str) -> None: ...


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
        client.template.policy.definition.rewriterule.delete_policy_definition_19()


.. toctree::
    :maxdepth: 1

    bulk
    multiple
    preview

