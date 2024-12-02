===========================
wani.list_activation_status
===========================


Operation: GET /dataservice/wani/{listType}/{listId}/listActivationStatus
-------------------------------------------------------------------------


Get if specified list is apart of a activated centralized policy, if it is the response also gives the centralized policy id, the users original defined centralized policy id, and if current list is apart of a active wani policy.

.. code:: python

    def get_list_activation_status(
        list_type: str, list_id: str
    ) -> ActivationStatusRes: ...


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
        client.wani.list_activation_status.get_list_activation_status()


.. toctree::
    :maxdepth: 1

    models

