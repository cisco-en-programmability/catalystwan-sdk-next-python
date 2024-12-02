=============================================
template.policy.definition.vpnmembershipgroup
=============================================


Operation: GET /dataservice/template/policy/definition/vpnmembershipgroup
-------------------------------------------------------------------------


Get policy definitions

.. code:: python

    def get_definitions_6() -> Any: ...


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
        client.template.policy.definition.vpnmembershipgroup.get_definitions_6()


Operation: POST /dataservice/template/policy/definition/vpnmembershipgroup
--------------------------------------------------------------------------


Create policy definition

.. code:: python

    def create_policy_definition_6(
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
        client.template.policy.definition.vpnmembershipgroup.create_policy_definition_6()


Operation: GET /dataservice/template/policy/definition/vpnmembershipgroup/{id}
------------------------------------------------------------------------------


Get a specific policy definitions

.. code:: python

    def get_policy_definition_6(id: str) -> Any: ...


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
        client.template.policy.definition.vpnmembershipgroup.get_policy_definition_6()


Operation: PUT /dataservice/template/policy/definition/vpnmembershipgroup/{id}
------------------------------------------------------------------------------


Edit a policy definitions

.. code:: python

    def edit_policy_definition_6(
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
        client.template.policy.definition.vpnmembershipgroup.edit_policy_definition_6()


Operation: DELETE /dataservice/template/policy/definition/vpnmembershipgroup/{id}
---------------------------------------------------------------------------------


Delete policy definition

.. code:: python

    def delete_policy_definition_6(id: str) -> None: ...


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
        client.template.policy.definition.vpnmembershipgroup.delete_policy_definition_6()


.. toctree::
    :maxdepth: 1

    bulk
    multiple
    preview

