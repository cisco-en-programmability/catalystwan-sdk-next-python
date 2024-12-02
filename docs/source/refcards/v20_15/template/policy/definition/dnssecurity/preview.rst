==============================================
template.policy.definition.dnssecurity.preview
==============================================


Operation: POST /dataservice/template/policy/definition/dnssecurity/preview
---------------------------------------------------------------------------


Preview policy definition

.. code:: python

    def preview_policy_definition(
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
        client.template.policy.definition.dnssecurity.preview.preview_policy_definition()


Operation: GET /dataservice/template/policy/definition/dnssecurity/preview/{id}
-------------------------------------------------------------------------------


Preview policy definition

.. code:: python

    def preview_policy_definition_by_id(id: str) -> Any: ...


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
        client.template.policy.definition.dnssecurity.preview.preview_policy_definition_by_id()


