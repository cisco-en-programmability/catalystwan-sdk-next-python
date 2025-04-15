=========================
partner.aci.policy.events
=========================


Operation: GET /dataservice/partner/aci/policy/events/{partnerId}
-----------------------------------------------------------------


Get ACI events

.. code:: python

    def get(
        partner_id: str,
        starttime: Optional[int] = None,
        endtime: Optional[int] = None,
    ) -> List[Any]: ...


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
        client.partner.aci.policy.events.get()


