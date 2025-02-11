===========================================
template.policy.definition.dialpeer.preview
===========================================


Operation: POST /dataservice/template/policy/definition/dialpeer/preview
------------------------------------------------------------------------


Preview policy definition

.. code:: python

    def preview_policy_definition_25(
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
        client.template.policy.definition.dialpeer.preview.preview_policy_definition_25()


Operation: GET /dataservice/template/policy/definition/dialpeer/preview/{id}
----------------------------------------------------------------------------


Preview policy definition

.. code:: python

    def preview_policy_definition_by_id_25(id: str) -> Any: ...


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
        client.template.policy.definition.dialpeer.preview.preview_policy_definition_by_id_25()


