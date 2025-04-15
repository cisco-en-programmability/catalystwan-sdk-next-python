========================
event.enable.fileprocess
========================


Operation: GET /dataservice/event/enable/fileprocess
----------------------------------------------------


Enable events from file.

.. code:: python

    def get() -> GeneralSchema: ...


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
        client.event.enable.fileprocess.get()


.. toctree::
    :maxdepth: 1

    models

