========================================
template.policy.definition.aclv6.preview
========================================


Operation: POST /dataservice/template/policy/definition/aclv6/preview
---------------------------------------------------------------------


Preview policy definition

.. code:: python

    def preview_policy_definition_9(
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
        client.template.policy.definition.aclv6.preview.preview_policy_definition_9()


Operation: GET /dataservice/template/policy/definition/aclv6/preview/{id}
-------------------------------------------------------------------------


Preview policy definition

.. code:: python

    def preview_policy_definition_by_id_9(id: str) -> Any: ...


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
        client.template.policy.definition.aclv6.preview.preview_policy_definition_by_id_9()


