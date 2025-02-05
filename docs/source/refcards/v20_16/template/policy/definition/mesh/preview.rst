=======================================
template.policy.definition.mesh.preview
=======================================


Operation: POST /dataservice/template/policy/definition/mesh/preview
--------------------------------------------------------------------


Preview policy definition

.. code:: python

    def preview_policy_definition_5(
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
        client.template.policy.definition.mesh.preview.preview_policy_definition_5()


Operation: GET /dataservice/template/policy/definition/mesh/preview/{id}
------------------------------------------------------------------------


Preview policy definition

.. code:: python

    def preview_policy_definition_by_id_5(id: str) -> Any: ...


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
        client.template.policy.definition.mesh.preview.preview_policy_definition_by_id_5()


