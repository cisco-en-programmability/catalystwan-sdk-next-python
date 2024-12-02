===========================================
template.policy.definition.srstphoneprofile
===========================================


Operation: GET /dataservice/template/policy/definition/srstphoneprofile
-----------------------------------------------------------------------


Get policy definitions

.. code:: python

    def get_definitions_30() -> Any: ...


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
        client.template.policy.definition.srstphoneprofile.get_definitions_30()


Operation: POST /dataservice/template/policy/definition/srstphoneprofile
------------------------------------------------------------------------


Create policy definition

.. code:: python

    def create_policy_definition_30(
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
        client.template.policy.definition.srstphoneprofile.create_policy_definition_30()


Operation: GET /dataservice/template/policy/definition/srstphoneprofile/{id}
----------------------------------------------------------------------------


Get a specific policy definitions

.. code:: python

    def get_policy_definition_30(id: str) -> Any: ...


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
        client.template.policy.definition.srstphoneprofile.get_policy_definition_30()


Operation: PUT /dataservice/template/policy/definition/srstphoneprofile/{id}
----------------------------------------------------------------------------


Edit a policy definitions

.. code:: python

    def edit_policy_definition_30(
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
        client.template.policy.definition.srstphoneprofile.edit_policy_definition_30()


Operation: DELETE /dataservice/template/policy/definition/srstphoneprofile/{id}
-------------------------------------------------------------------------------


Delete policy definition

.. code:: python

    def delete_policy_definition_30(id: str) -> None: ...


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
        client.template.policy.definition.srstphoneprofile.delete_policy_definition_30()


.. toctree::
    :maxdepth: 1

    bulk
    multiple
    preview

