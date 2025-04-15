========================
template.policy.security
========================


Operation: POST /dataservice/template/policy/security
-----------------------------------------------------


Create Template

.. code:: python

    def post(payload: Any) -> None: ...


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
        client.template.policy.security.post()


Operation: PUT /dataservice/template/policy/security/{policyId}
---------------------------------------------------------------


Edit Template

.. code:: python

    def put(policy_id: str, payload: Any) -> Any: ...


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
        client.template.policy.security.put()


Operation: DELETE /dataservice/template/policy/security/{policyId}
------------------------------------------------------------------


Delete Template

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
        client.template.policy.security.delete()


Operation: GET /dataservice/template/policy/security
----------------------------------------------------


.. code:: python

    @overload
    def get(mode: Optional[str] = None) -> List[Any]: ...


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
        client.template.policy.security.get()


Operation: GET /dataservice/template/policy/security/{deviceModel}
------------------------------------------------------------------


.. code:: python

    @overload
    def get(device_model: DeviceModel) -> Any: ...


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
        client.template.policy.security.get()


.. toctree::
    :maxdepth: 1

    definition
    devices
    staging
    summary
    models

