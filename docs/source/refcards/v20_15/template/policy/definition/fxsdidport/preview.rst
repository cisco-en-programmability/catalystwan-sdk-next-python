=============================================
template.policy.definition.fxsdidport.preview
=============================================


Operation: POST /dataservice/template/policy/definition/fxsdidport/preview
--------------------------------------------------------------------------


Preview policy definition

.. code:: python

    def preview_policy_definition_28(
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
        client.template.policy.definition.fxsdidport.preview.preview_policy_definition_28()


Operation: GET /dataservice/template/policy/definition/fxsdidport/preview/{id}
------------------------------------------------------------------------------


Preview policy definition

.. code:: python

    def preview_policy_definition_by_id_28(id: str) -> Any: ...


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
        client.template.policy.definition.fxsdidport.preview.preview_policy_definition_by_id_28()


