===========
mdp.onboard
===========


Operation: POST /dataservice/mdp/onboard
----------------------------------------


Start MDP onboarding operation

.. code:: python

    def post(payload: Any) -> Any: ...


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
        client.mdp.onboard.post()


Operation: PUT /dataservice/mdp/onboard/{nmsId}
-----------------------------------------------


update MDP onboarding document

.. code:: python

    def put(nms_id: str, payload: Any) -> Any: ...


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
        client.mdp.onboard.put()


Operation: DELETE /dataservice/mdp/onboard/{nmsId}
--------------------------------------------------


offboard the mdp application

.. code:: python

    def delete(nms_id: str) -> None: ...


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
        client.mdp.onboard.delete()


.. toctree::
    :maxdepth: 1

    status

