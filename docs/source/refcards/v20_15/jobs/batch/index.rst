==========
jobs.batch
==========


Operation: POST /dataservice/jobs/batch
---------------------------------------


Batch processing multiple REST API calls

.. code:: python

    def batch_execute(payload: Optional[BatchFlow] = None) -> str: ...


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
        client.jobs.batch.batch_execute()


.. toctree::
    :maxdepth: 1

    models

