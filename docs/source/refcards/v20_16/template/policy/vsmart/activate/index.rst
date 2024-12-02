===============================
template.policy.vsmart.activate
===============================


Operation: POST /dataservice/template/policy/vsmart/activate/{policyId}
-----------------------------------------------------------------------


Activate vsmart policy for a given policy id

.. code:: python

    def activate_policy(
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
        client.template.policy.vsmart.activate.activate_policy()


.. toctree::
    :maxdepth: 1

    central

