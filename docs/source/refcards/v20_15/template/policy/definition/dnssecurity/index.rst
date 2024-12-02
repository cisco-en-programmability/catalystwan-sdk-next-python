======================================
template.policy.definition.dnssecurity
======================================


Operation: GET /dataservice/template/policy/definition/dnssecurity
------------------------------------------------------------------


Get policy definitions

.. code:: python

    def get_definitions() -> Any: ...


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
        client.template.policy.definition.dnssecurity.get_definitions()


Operation: POST /dataservice/template/policy/definition/dnssecurity
-------------------------------------------------------------------


Create policy definition

.. code:: python

    def create_policy_definition(
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
        client.template.policy.definition.dnssecurity.create_policy_definition()


Operation: GET /dataservice/template/policy/definition/dnssecurity/{id}
-----------------------------------------------------------------------


Get a specific policy definitions

.. code:: python

    def get_policy_definition(id: str) -> Any: ...


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
        client.template.policy.definition.dnssecurity.get_policy_definition()


Operation: PUT /dataservice/template/policy/definition/dnssecurity/{id}
-----------------------------------------------------------------------


Edit a policy definitions

.. code:: python

    def edit_policy_definition(
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
        client.template.policy.definition.dnssecurity.edit_policy_definition()


Operation: DELETE /dataservice/template/policy/definition/dnssecurity/{id}
--------------------------------------------------------------------------


Delete policy definition

.. code:: python

    def delete_policy_definition(id: str) -> None: ...


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
        client.template.policy.definition.dnssecurity.delete_policy_definition()


.. toctree::
    :maxdepth: 1

    bulk
    multiple
    preview

