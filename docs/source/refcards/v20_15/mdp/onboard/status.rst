==================
mdp.onboard.status
==================


Operation: GET /dataservice/mdp/onboard/status
----------------------------------------------


Get MDP onboarding status

.. code:: python

    def get() -> List[Any]: ...


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
        client.mdp.onboard.status.get()


