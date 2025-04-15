===============================
stream.device.nwpi.tasks.create
===============================


Operation: POST /dataservice/stream/device/nwpi/tasks/create
------------------------------------------------------------


Task Action - Create

.. code:: python

    def post(payload: Any) -> TasksCreateResponsePayload: ...


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
        client.stream.device.nwpi.tasks.create.post()


.. toctree::
    :maxdepth: 1

    models

