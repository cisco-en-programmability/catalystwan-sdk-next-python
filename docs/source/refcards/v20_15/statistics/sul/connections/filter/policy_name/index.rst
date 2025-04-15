=============================================
statistics.sul.connections.filter.policy_name
=============================================


Operation: GET /dataservice/statistics/sul/connections/filter/policy_name/{policyType}
--------------------------------------------------------------------------------------


Get filter Policy Name list

.. code:: python

    def get(policy_type: PolicyTypeParam, query: str) -> List[Any]: ...


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
        client.statistics.sul.connections.filter.policy_name.get()


.. toctree::
    :maxdepth: 1

    models

