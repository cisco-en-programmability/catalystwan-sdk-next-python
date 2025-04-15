=============================
wani.policy_activation_status
=============================


Operation: GET /dataservice/wani/{policyType}/{policyId}/policyActivationStatus
-------------------------------------------------------------------------------


Get if specified policy is apart of a activated centralized policy, if it is the response also gives the centralized policy id, the users original defined centralized policy id, and if current policy is apart of a active wani policy.

.. code:: python

    def get(policy_type: str, policy_id: str) -> ActivationStatusRes: ...


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
        client.wani.policy_activation_status.get()


.. toctree::
    :maxdepth: 1

    models

