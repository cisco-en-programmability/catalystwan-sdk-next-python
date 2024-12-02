========================================
template.policy.definition.sslutdprofile
========================================


Operation: GET /dataservice/template/policy/definition/sslutdprofile
--------------------------------------------------------------------


Get policy definitions

.. code:: python

    def get_definitions_22() -> Any: ...


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
        client.template.policy.definition.sslutdprofile.get_definitions_22()


Operation: POST /dataservice/template/policy/definition/sslutdprofile
---------------------------------------------------------------------


Create policy definition

.. code:: python

    def create_policy_definition_22(
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
        client.template.policy.definition.sslutdprofile.create_policy_definition_22()


Operation: GET /dataservice/template/policy/definition/sslutdprofile/{id}
-------------------------------------------------------------------------


Get a specific policy definitions

.. code:: python

    def get_policy_definition_22(id: str) -> Any: ...


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
        client.template.policy.definition.sslutdprofile.get_policy_definition_22()


Operation: PUT /dataservice/template/policy/definition/sslutdprofile/{id}
-------------------------------------------------------------------------


Edit a policy definitions

.. code:: python

    def edit_policy_definition_22(
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
        client.template.policy.definition.sslutdprofile.edit_policy_definition_22()


Operation: DELETE /dataservice/template/policy/definition/sslutdprofile/{id}
----------------------------------------------------------------------------


Delete policy definition

.. code:: python

    def delete_policy_definition_22(id: str) -> None: ...


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
        client.template.policy.definition.sslutdprofile.delete_policy_definition_22()


.. toctree::
    :maxdepth: 1

    bulk
    multiple
    preview

