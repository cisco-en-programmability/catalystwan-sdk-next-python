=====================
template.policy.vedge
=====================


Operation: GET /dataservice/template/policy/vedge
-------------------------------------------------


Get policy details

.. code:: python

    def get() -> Any: ...


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
        client.template.policy.vedge.get()


Operation: PUT /dataservice/template/policy/vedge/{policyId}
------------------------------------------------------------


Edit template

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
        client.template.policy.vedge.put()


Operation: DELETE /dataservice/template/policy/vedge/{policyId}
---------------------------------------------------------------


Delete template

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
        client.template.policy.vedge.delete()


Operation: POST /dataservice/template/policy/vedge
--------------------------------------------------


.. code:: python

    @overload
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
        client.template.policy.vedge.post()


Operation: POST /dataservice/template/policy/vedge/{resourceGroupName}/{policyId}
---------------------------------------------------------------------------------


.. code:: python

    @overload
    def post(policy_id: str, resource_group_name: str) -> None: ...


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
        client.template.policy.vedge.post()


.. toctree::
    :maxdepth: 1

    definition
    devices

