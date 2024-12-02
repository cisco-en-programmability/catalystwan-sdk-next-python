============
mdp.policies
============


Operation: GET /dataservice/mdp/policies/{nmsId}
------------------------------------------------


Retrieve MDP policies

.. code:: python

    def retrieve_mdp_policies(nms_id: str) -> List[Any]: ...


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
        client.mdp.policies.retrieve_mdp_policies()


Operation: PUT /dataservice/mdp/policies/{nmsId}
------------------------------------------------


update policy status

.. code:: python

    def update_policy_status(
        nms_id: str, payload: Optional[Any] = None
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
        client.mdp.policies.update_policy_status()


.. toctree::
    :maxdepth: 1

    mdpconfig

