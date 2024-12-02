======================
template.policy.vsmart
======================


Operation: GET /dataservice/template/policy/vsmart
--------------------------------------------------


Get all template vsmart policy list

.. code:: python

    def generate_v_smart_policy_template_list() -> List[Any]: ...


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
        client.template.policy.vsmart.generate_v_smart_policy_template_list()


Operation: POST /dataservice/template/policy/vsmart
---------------------------------------------------


Create template for given policy

.. code:: python

    def create_v_smart_template(payload: Optional[Any] = None) -> Any: ...


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
        client.template.policy.vsmart.create_v_smart_template()


Operation: PUT /dataservice/template/policy/vsmart/{policyId}
-------------------------------------------------------------


Edit template for given policy id

.. code:: python

    def edit_v_smart_template(
        policy_id: str, payload: Optional[Any] = None
    ) -> List[Any]: ...


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
        client.template.policy.vsmart.edit_v_smart_template()


Operation: DELETE /dataservice/template/policy/vsmart/{policyId}
----------------------------------------------------------------


Delete template for a given policy id

.. code:: python

    def delete_v_smart_template(policy_id: str) -> None: ...


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
        client.template.policy.vsmart.delete_v_smart_template()


.. toctree::
    :maxdepth: 1

    activate/index
    central
    connectivity/index
    deactivate
    definition
    qosmos_nbar_migration_warning

