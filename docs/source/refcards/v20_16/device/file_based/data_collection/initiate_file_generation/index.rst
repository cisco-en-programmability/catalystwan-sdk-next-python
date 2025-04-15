==========================================================
device.file_based.data_collection.initiate_file_generation
==========================================================


Operation: POST /dataservice/device/file-based/data-collection/initiate-file-generation
---------------------------------------------------------------------------------------


Request device to prepare realtime collection data in required file format

.. code:: python

    def post(payload: InitiateFileGenerationRequest) -> str: ...


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
        client.device.file_based.data_collection.initiate_file_generation.post()


.. toctree::
    :maxdepth: 1

    models

