============================================
template.policy.definition.vpnqosmap.preview
============================================


Operation: POST /dataservice/template/policy/definition/vpnqosmap/preview
-------------------------------------------------------------------------


Preview policy definition

.. code:: python

    def preview_policy_definition_2(
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
        client.template.policy.definition.vpnqosmap.preview.preview_policy_definition_2()


Operation: GET /dataservice/template/policy/definition/vpnqosmap/preview/{id}
-----------------------------------------------------------------------------


Preview policy definition

.. code:: python

    def preview_policy_definition_by_id_2(id: str) -> Any: ...


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
        client.template.policy.definition.vpnqosmap.preview.preview_policy_definition_by_id_2()


