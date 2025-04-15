===============
v1.policy_group
===============


Operation: POST /dataservice/v1/policy-group
--------------------------------------------


Create a new Policy Group

.. code:: python

    def post(
        payload: CreatePolicyGroupPostRequest,
    ) -> CreatePolicyGroupPostResponse: ...


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
        client.v1.policy_group.post()


Operation: PUT /dataservice/v1/policy-group/{policyGroupId}
-----------------------------------------------------------


Edit a Policy Group

.. code:: python

    def put(
        policy_group_id: str, payload: EditPolicyGroupPutRequest
    ) -> EditPolicyGroupPutResponse: ...


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
        client.v1.policy_group.put()


Operation: DELETE /dataservice/v1/policy-group/{policyGroupId}
--------------------------------------------------------------


Delete Policy Group

.. code:: python

    def delete(
        policy_group_id: str, delete_profiles: Optional[bool] = None
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
        client.v1.policy_group.delete()


Operation: GET /dataservice/v1/policy-group
-------------------------------------------


.. code:: python

    @overload
    def get(solution: Optional[str] = None) -> List[PolicyGroup]: ...


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
        client.v1.policy_group.get()


Operation: GET /dataservice/v1/policy-group/{policyGroupId}
-----------------------------------------------------------


.. code:: python

    @overload
    def get(policy_group_id: str) -> PolicyGroup: ...


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
        client.v1.policy_group.get()


.. toctree::
    :maxdepth: 1

    device/index
    models

