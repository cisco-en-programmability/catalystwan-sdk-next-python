====================================================
template.policy.definition.advancedinspectionprofile
====================================================


Operation: GET /dataservice/template/policy/definition/advancedinspectionprofile
--------------------------------------------------------------------------------


Get policy definitions

.. code:: python

    def get_definitions_10() -> Any: ...


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
        client.template.policy.definition.advancedinspectionprofile.get_definitions_10()


Operation: POST /dataservice/template/policy/definition/advancedinspectionprofile
---------------------------------------------------------------------------------


Create policy definition

.. code:: python

    def create_policy_definition_10(
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
        client.template.policy.definition.advancedinspectionprofile.create_policy_definition_10()


Operation: GET /dataservice/template/policy/definition/advancedinspectionprofile/{id}
-------------------------------------------------------------------------------------


Get a specific policy definitions

.. code:: python

    def get_policy_definition_10(id: str) -> Any: ...


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
        client.template.policy.definition.advancedinspectionprofile.get_policy_definition_10()


Operation: PUT /dataservice/template/policy/definition/advancedinspectionprofile/{id}
-------------------------------------------------------------------------------------


Edit a policy definitions

.. code:: python

    def edit_policy_definition_10(
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
        client.template.policy.definition.advancedinspectionprofile.edit_policy_definition_10()


Operation: DELETE /dataservice/template/policy/definition/advancedinspectionprofile/{id}
----------------------------------------------------------------------------------------


Delete policy definition

.. code:: python

    def delete_policy_definition_10(id: str) -> None: ...


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
        client.template.policy.definition.advancedinspectionprofile.delete_policy_definition_10()


.. toctree::
    :maxdepth: 1

    bulk
    multiple
    preview

