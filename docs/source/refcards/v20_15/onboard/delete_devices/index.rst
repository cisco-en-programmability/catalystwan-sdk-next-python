======================
onboard.delete_devices
======================


Operation: POST /dataservice/onboard/delete-devices
---------------------------------------------------


Delete Manual Onboard Device details

.. code:: python

    def post(payload: DeleteDetails) -> List[DeleteResponseInner]: ...


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
        client.onboard.delete_devices.post()


.. toctree::
    :maxdepth: 1

    models

