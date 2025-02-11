====================================
template.policy.definition.vpnqosmap
====================================


Operation: GET /dataservice/template/policy/definition/vpnqosmap
----------------------------------------------------------------


Get policy definitions

.. code:: python

    def get_definitions_2() -> Any: ...


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
        client.template.policy.definition.vpnqosmap.get_definitions_2()


Operation: POST /dataservice/template/policy/definition/vpnqosmap
-----------------------------------------------------------------


Create policy definition

.. code:: python

    def create_policy_definition_2(
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
        client.template.policy.definition.vpnqosmap.create_policy_definition_2()


Operation: GET /dataservice/template/policy/definition/vpnqosmap/{id}
---------------------------------------------------------------------


Get a specific policy definitions

.. code:: python

    def get_policy_definition_2(id: str) -> Any: ...


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
        client.template.policy.definition.vpnqosmap.get_policy_definition_2()


Operation: PUT /dataservice/template/policy/definition/vpnqosmap/{id}
---------------------------------------------------------------------


Edit a policy definitions

.. code:: python

    def edit_policy_definition_2(
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
        client.template.policy.definition.vpnqosmap.edit_policy_definition_2()


Operation: DELETE /dataservice/template/policy/definition/vpnqosmap/{id}
------------------------------------------------------------------------


Delete policy definition

.. code:: python

    def delete_policy_definition_2(id: str) -> None: ...


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
        client.template.policy.definition.vpnqosmap.delete_policy_definition_2()


.. toctree::
    :maxdepth: 1

    bulk
    multiple
    preview

