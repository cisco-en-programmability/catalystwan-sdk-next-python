==================
notifications.rule
==================


Operation: PUT /dataservice/notifications/rule
----------------------------------------------


Update notification rule

.. code:: python

    def update_notification_rule(
        rule_id: str, payload: Optional[Any] = None
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
        client.notifications.rule.update_notification_rule()


Operation: POST /dataservice/notifications/rule
-----------------------------------------------


Add notification rule

.. code:: python

    def create_notification_rule(
        payload: Optional[Any] = None,
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
        client.notifications.rule.create_notification_rule()


