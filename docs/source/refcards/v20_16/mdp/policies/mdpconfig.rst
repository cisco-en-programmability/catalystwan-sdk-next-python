======================
mdp.policies.mdpconfig
======================


Operation: PUT /dataservice/mdp/policies/mdpconfig
--------------------------------------------------


Add internal policy from vmanage

.. code:: python

    def put(payload: Any) -> Any: ...


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
        client.mdp.policies.mdpconfig.put()


Operation: GET /dataservice/mdp/policies/mdpconfig/{deviceId}
-------------------------------------------------------------


Retrieve MDP ConfigObject

.. code:: python

    def get(device_id: str) -> List[Any]: ...


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
        client.mdp.policies.mdpconfig.get()


