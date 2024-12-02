===============================================
template.policy.definition.deviceaccesspolicyv6
===============================================


Operation: GET /dataservice/template/policy/definition/deviceaccesspolicyv6
---------------------------------------------------------------------------


Get policy definitions

.. code:: python

    def get_definitions_17() -> Any: ...


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
        client.template.policy.definition.deviceaccesspolicyv6.get_definitions_17()


Operation: POST /dataservice/template/policy/definition/deviceaccesspolicyv6
----------------------------------------------------------------------------


Create policy definition

.. code:: python

    def create_policy_definition_17(
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
        client.template.policy.definition.deviceaccesspolicyv6.create_policy_definition_17()


Operation: GET /dataservice/template/policy/definition/deviceaccesspolicyv6/{id}
--------------------------------------------------------------------------------


Get a specific policy definitions

.. code:: python

    def get_policy_definition_17(id: str) -> Any: ...


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
        client.template.policy.definition.deviceaccesspolicyv6.get_policy_definition_17()


Operation: PUT /dataservice/template/policy/definition/deviceaccesspolicyv6/{id}
--------------------------------------------------------------------------------


Edit a policy definitions

.. code:: python

    def edit_policy_definition_17(
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
        client.template.policy.definition.deviceaccesspolicyv6.edit_policy_definition_17()


Operation: DELETE /dataservice/template/policy/definition/deviceaccesspolicyv6/{id}
-----------------------------------------------------------------------------------


Delete policy definition

.. code:: python

    def delete_policy_definition_17(id: str) -> None: ...


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
        client.template.policy.definition.deviceaccesspolicyv6.delete_policy_definition_17()


.. toctree::
    :maxdepth: 1

    bulk
    multiple
    preview

