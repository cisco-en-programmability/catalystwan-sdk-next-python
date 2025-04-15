============
mdp.policies
============


Operation: GET /dataservice/mdp/policies/{nmsId}
------------------------------------------------


Retrieve MDP policies

.. code:: python

    def get(nms_id: str) -> List[Any]: ...


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
        client.mdp.policies.get()


Operation: PUT /dataservice/mdp/policies/{nmsId}
------------------------------------------------


update policy status

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
        client.mdp.policies.put()


.. toctree::
    :maxdepth: 1

    mdpconfig

