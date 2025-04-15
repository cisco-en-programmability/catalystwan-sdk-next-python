===============
onboard.details
===============


Operation: POST /dataservice/onboard/details
--------------------------------------------


Add Manual Onboard Device details

.. code:: python

    def post(payload: DeviceDetailsData) -> None: ...


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
        client.onboard.details.post()


.. toctree::
    :maxdepth: 1

    models

