======================
mdp.policies.mdpconfig
======================


Operation: PUT /dataservice/mdp/policies/mdpconfig
--------------------------------------------------


Add internal policy from vmanage

.. code:: python

    def add_internal_policy(payload: Optional[Any] = None) -> Any: ...


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
        client.mdp.policies.mdpconfig.add_internal_policy()


Operation: GET /dataservice/mdp/policies/mdpconfig/{deviceId}
-------------------------------------------------------------


Retrieve MDP ConfigObject

.. code:: python

    def retrieve_mdp_config_object(device_id: str) -> List[Any]: ...


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
        client.mdp.policies.mdpconfig.retrieve_mdp_config_object()


