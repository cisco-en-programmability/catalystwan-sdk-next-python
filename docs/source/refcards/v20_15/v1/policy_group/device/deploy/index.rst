=============================
v1.policy_group.device.deploy
=============================


Operation: POST /dataservice/v1/policy-group/{policyGroupId}/device/deploy
--------------------------------------------------------------------------


deploy policy group to devices

.. code:: python

    def post(
        policy_group_id: str, payload: DeployPolicyGroupPostRequest
    ) -> DeployPolicyGroupPostResponse: ...


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
        client.v1.policy_group.device.deploy.post()


.. toctree::
    :maxdepth: 1

    models

