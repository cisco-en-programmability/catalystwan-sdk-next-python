=============================================
template.policy.definition.deviceaccesspolicy
=============================================


Operation: GET /dataservice/template/policy/definition/deviceaccesspolicy
-------------------------------------------------------------------------


Get policy definitions

.. code:: python

    def get_definitions_16() -> Any: ...


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
        client.template.policy.definition.deviceaccesspolicy.get_definitions_16()


Operation: POST /dataservice/template/policy/definition/deviceaccesspolicy
--------------------------------------------------------------------------


Create policy definition

.. code:: python

    def create_policy_definition_16(
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
        client.template.policy.definition.deviceaccesspolicy.create_policy_definition_16()


Operation: GET /dataservice/template/policy/definition/deviceaccesspolicy/{id}
------------------------------------------------------------------------------


Get a specific policy definitions

.. code:: python

    def get_policy_definition_16(id: str) -> Any: ...


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
        client.template.policy.definition.deviceaccesspolicy.get_policy_definition_16()


Operation: PUT /dataservice/template/policy/definition/deviceaccesspolicy/{id}
------------------------------------------------------------------------------


Edit a policy definitions

.. code:: python

    def edit_policy_definition_16(
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
        client.template.policy.definition.deviceaccesspolicy.edit_policy_definition_16()


Operation: DELETE /dataservice/template/policy/definition/deviceaccesspolicy/{id}
---------------------------------------------------------------------------------


Delete policy definition

.. code:: python

    def delete_policy_definition_16(id: str) -> None: ...


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
        client.template.policy.definition.deviceaccesspolicy.delete_policy_definition_16()


.. toctree::
    :maxdepth: 1

    bulk
    multiple
    preview

