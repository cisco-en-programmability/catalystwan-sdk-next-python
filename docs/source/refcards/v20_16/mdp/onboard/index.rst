===========
mdp.onboard
===========


Operation: POST /dataservice/mdp/onboard
----------------------------------------


Start MDP onboarding operation

.. code:: python

    def onboard_mdp(payload: Optional[Any] = None) -> Any: ...


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
        client.mdp.onboard.onboard_mdp()


Operation: PUT /dataservice/mdp/onboard/{nmsId}
-----------------------------------------------


update MDP onboarding document

.. code:: python

    def update_onboarding_payload(
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
        client.mdp.onboard.update_onboarding_payload()


Operation: DELETE /dataservice/mdp/onboard/{nmsId}
--------------------------------------------------


offboard the mdp application

.. code:: python

    def offboard(nms_id: str) -> None: ...


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
        client.mdp.onboard.offboard()


.. toctree::
    :maxdepth: 1

    status

