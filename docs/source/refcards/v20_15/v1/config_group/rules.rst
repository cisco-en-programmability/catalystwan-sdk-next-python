=====================
v1.config_group.rules
=====================


Operation: GET /dataservice/v1/config-group/{configGroupId}/rules
-----------------------------------------------------------------


Get Rule by associated object Id, example : get rules by config group Id

.. code:: python

    def get_rule_association_by_config_group_id(
        config_group_id: str,
    ) -> str: ...


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
        client.v1.config_group.rules.get_rule_association_by_config_group_id()


