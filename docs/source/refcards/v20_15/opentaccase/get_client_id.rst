=========================
opentaccase.get_client_id
=========================


Operation: GET /dataservice/opentaccase/getClientID
---------------------------------------------------


Deprecated!!!

Gets vManage Client ID

.. code:: python

    def get_client_id() -> List[Any]: ...


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
        client.opentaccase.get_client_id.get_client_id()


