===================
notifications.rules
===================


Operation: GET /dataservice/notifications/rules
-----------------------------------------------


Get all rules or specific notification rule by its Id

.. code:: python

    def get(
        rule_id: Optional[str] = None, site_id: Optional[str] = None
    ) -> NotificationsRulesResponse: ...


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
        client.notifications.rules.get()


Operation: DELETE /dataservice/notifications/rules
--------------------------------------------------


Delete notification rule

.. code:: python

    def delete(rule_id: str) -> None: ...


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
        client.notifications.rules.delete()


.. toctree::
    :maxdepth: 1

    models

