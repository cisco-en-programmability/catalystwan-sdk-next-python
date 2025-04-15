========
schedule
========


Operation: GET /dataservice/schedule/{schedulerId}
--------------------------------------------------


Get a schedule record for backup by scheduler id

.. code:: python

    def get(scheduler_id: str) -> Any: ...


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
        client.schedule.get()


Operation: DELETE /dataservice/schedule/{schedulerId}
-----------------------------------------------------


Delete a schedule record for backup in vManage by scheduler id

.. code:: python

    def delete(scheduler_id: str) -> Any: ...


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
        client.schedule.delete()


.. toctree::
    :maxdepth: 1

    create
    list

