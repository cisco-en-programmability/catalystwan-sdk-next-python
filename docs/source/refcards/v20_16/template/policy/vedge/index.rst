=====================
template.policy.vedge
=====================


Operation: GET /dataservice/template/policy/vedge
-------------------------------------------------


Get policy details

.. code:: python

    def generate_policy_template_list() -> Any: ...


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
        client.template.policy.vedge.generate_policy_template_list()


Operation: POST /dataservice/template/policy/vedge
--------------------------------------------------


Create template

.. code:: python

    def create_v_edge_template(payload: Optional[Any] = None) -> Any: ...


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
        client.template.policy.vedge.create_v_edge_template()


Operation: PUT /dataservice/template/policy/vedge/{policyId}
------------------------------------------------------------


Edit template

.. code:: python

    def edit_v_edge_template(
        policy_id: str, payload: Optional[Any] = None
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
        client.template.policy.vedge.edit_v_edge_template()


Operation: DELETE /dataservice/template/policy/vedge/{policyId}
---------------------------------------------------------------


Delete template

.. code:: python

    def delete_v_edge_template(policy_id: str) -> None: ...


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
        client.template.policy.vedge.delete_v_edge_template()


Operation: POST /dataservice/template/policy/vedge/{resourceGroupName}/{policyId}
---------------------------------------------------------------------------------


Change policy resource group

.. code:: python

    def change_policy_resource_group(
        policy_id: str, resource_group_name: str
    ) -> None: ...


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
        client.template.policy.vedge.change_policy_resource_group()


.. toctree::
    :maxdepth: 1

    definition
    devices

