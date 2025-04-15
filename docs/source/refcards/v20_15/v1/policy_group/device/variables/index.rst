================================
v1.policy_group.device.variables
================================


Operation: GET /dataservice/v1/policy-group/{policyGroupId}/device/variables
----------------------------------------------------------------------------


Get device variables

.. code:: python

    def get(
        policy_group_id: str,
        device_id: Optional[str] = None,
        suggestions: Optional[bool] = None,
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
        client.v1.policy_group.device.variables.get()


Operation: PUT /dataservice/v1/policy-group/{policyGroupId}/device/variables
----------------------------------------------------------------------------


assign values to device variables

.. code:: python

    def put(
        policy_group_id: str,
        payload: CreatePolicyGroupDeviceVariablesPutRequest,
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
        client.v1.policy_group.device.variables.put()


Operation: POST /dataservice/v1/policy-group/{policyGroupId}/device/variables
-----------------------------------------------------------------------------


Fetch device variables

.. code:: python

    def post(
        policy_group_id: str,
        payload: FetchPolicyGroupDeviceVariablesPostRequest,
    ) -> FetchPolicyGroupDeviceVariablesPostResponse: ...


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
        client.v1.policy_group.device.variables.post()


.. toctree::
    :maxdepth: 1

    schema
    models

