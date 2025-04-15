======================
template.policy.vsmart
======================


Operation: GET /dataservice/template/policy/vsmart
--------------------------------------------------


Get all template vsmart policy list

.. code:: python

    def get() -> List[Any]: ...


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
        client.template.policy.vsmart.get()


Operation: POST /dataservice/template/policy/vsmart
---------------------------------------------------


Create template for given policy

.. code:: python

    def post(payload: Any) -> Any: ...


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
        client.template.policy.vsmart.post()


Operation: PUT /dataservice/template/policy/vsmart/{policyId}
-------------------------------------------------------------


Edit template for given policy id

.. code:: python

    def put(policy_id: str, payload: Any) -> List[Any]: ...


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
        client.template.policy.vsmart.put()


Operation: DELETE /dataservice/template/policy/vsmart/{policyId}
----------------------------------------------------------------


Delete template for a given policy id

.. code:: python

    def delete(policy_id: str) -> None: ...


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
        client.template.policy.vsmart.delete()


.. toctree::
    :maxdepth: 1

    activate/index
    central
    connectivity/index
    deactivate
    definition
    qosmos_nbar_migration_warning

