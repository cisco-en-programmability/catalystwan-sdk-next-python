==========
sdavc.task
==========


Operation: POST /dataservice/sdavc/task/{taskId}
------------------------------------------------


Activate container

.. code:: python

    def post(task_id: str, payload: Any) -> None: ...


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
        client.sdavc.task.post()


