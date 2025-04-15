=========================
serverlongpoll.event.poll
=========================


Operation: GET /dataservice/serverlongpoll/event/poll/{partnerId}
-----------------------------------------------------------------


Retrieve registration change information

.. code:: python

    def get(
        partner_id: str,
        event_id: Optional[str] = None,
        event_names: Optional[List[EventName]] = None,
        wait_time: Optional[int] = 0,
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
        client.serverlongpoll.event.poll.get()


.. toctree::
    :maxdepth: 1

    models

