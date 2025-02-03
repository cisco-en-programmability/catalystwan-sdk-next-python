================================
v1.policy_group.device.variables
================================


Operation: GET /dataservice/v1/policy-group/{policyGroupId}/device/variables
----------------------------------------------------------------------------


Get device variables

.. code:: python

    def get_policy_group_device_variables(
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
        client.v1.policy_group.device.variables.get_policy_group_device_variables()


Operation: PUT /dataservice/v1/policy-group/{policyGroupId}/device/variables
----------------------------------------------------------------------------


assign values to device variables

.. code:: python

    def create_policy_group_device_variables(
        policy_group_id: str,
        payload: Optional[
            CreatePolicyGroupDeviceVariablesPutRequest
        ] = None,
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
        client.v1.policy_group.device.variables.create_policy_group_device_variables()


Operation: POST /dataservice/v1/policy-group/{policyGroupId}/device/variables
-----------------------------------------------------------------------------


Fetch device variables

.. code:: python

    def fetch_policy_group_device_variables(
        policy_group_id: str,
        payload: Optional[
            FetchPolicyGroupDeviceVariablesPostRequest
        ] = None,
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
        client.v1.policy_group.device.variables.fetch_policy_group_device_variables()


.. toctree::
    :maxdepth: 1

    schema
    models

