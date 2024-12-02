==============================================
template.policy.definition.rewriterule.preview
==============================================


Operation: POST /dataservice/template/policy/definition/rewriterule/preview
---------------------------------------------------------------------------


Preview policy definition

.. code:: python

    def preview_policy_definition_19(
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
        client.template.policy.definition.rewriterule.preview.preview_policy_definition_19()


Operation: GET /dataservice/template/policy/definition/rewriterule/preview/{id}
-------------------------------------------------------------------------------


Preview policy definition

.. code:: python

    def preview_policy_definition_by_id_19(id: str) -> Any: ...


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
        client.template.policy.definition.rewriterule.preview.preview_policy_definition_by_id_19()


