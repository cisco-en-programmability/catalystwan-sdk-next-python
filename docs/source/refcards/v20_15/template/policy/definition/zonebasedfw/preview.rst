==============================================
template.policy.definition.zonebasedfw.preview
==============================================


Operation: POST /dataservice/template/policy/definition/zonebasedfw/preview
---------------------------------------------------------------------------


Preview policy definition

.. code:: python

    def preview_policy_definition_7(
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
        client.template.policy.definition.zonebasedfw.preview.preview_policy_definition_7()


Operation: GET /dataservice/template/policy/definition/zonebasedfw/preview/{id}
-------------------------------------------------------------------------------


Preview policy definition

.. code:: python

    def preview_policy_definition_by_id_7(id: str) -> Any: ...


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
        client.template.policy.definition.zonebasedfw.preview.preview_policy_definition_by_id_7()


