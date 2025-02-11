==========================================================
device.file_based.data_collection.initiate_file_generation
==========================================================


Operation: POST /dataservice/device/file-based/data-collection/initiate-file-generation
---------------------------------------------------------------------------------------


Request device to prepare realtime collection data in required file format

.. code:: python

    def initiate_file_generation_request_to_device(
        payload: Optional[InitiateFileGenerationRequest] = None,
    ) -> str: ...


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
        client.device.file_based.data_collection.initiate_file_generation.initiate_file_generation_request_to_device()


.. toctree::
    :maxdepth: 1

    models

