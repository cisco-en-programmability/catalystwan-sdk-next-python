============================
statistics.download.filelist
============================


Operation: POST /dataservice/statistics/download/{processType}/filelist
-----------------------------------------------------------------------


Downloading list of stats file

.. code:: python

    def download_list(
        process_type: str,
        payload: Optional[DownloadListPostRequest] = None,
    ) -> None: ...


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
        client.statistics.download.filelist.download_list()


.. toctree::
    :maxdepth: 1

    models

