===============
v1.policy_group
===============


Operation: GET /dataservice/v1/policy-group
-------------------------------------------


Get a Policy Group by Solution

.. code:: python

    def get_policy_group_by_solution(
        solution: Optional[str] = None,
    ) -> List[PolicyGroup]: ...


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
        client.v1.policy_group.get_policy_group_by_solution()


Operation: POST /dataservice/v1/policy-group
--------------------------------------------


Create a new Policy Group

.. code:: python

    def create_policy_group(payload: Optional[str] = None) -> str: ...


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
        client.v1.policy_group.create_policy_group()


Operation: GET /dataservice/v1/policy-group/{policyGroupId}
-----------------------------------------------------------


Get a Policy Group by ID

.. code:: python

    def get_policy_group(policy_group_id: str) -> PolicyGroup: ...


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
        client.v1.policy_group.get_policy_group()


Operation: PUT /dataservice/v1/policy-group/{policyGroupId}
-----------------------------------------------------------


Edit a Policy Group

.. code:: python

    def edit_policy_group(
        policy_group_id: str, payload: Optional[str] = None
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
        client.v1.policy_group.edit_policy_group()


Operation: DELETE /dataservice/v1/policy-group/{policyGroupId}
--------------------------------------------------------------


Delete Policy Group

.. code:: python

    def delete_policy_group(
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
        client.v1.policy_group.delete_policy_group()


.. toctree::
    :maxdepth: 1

    device/index
    models

