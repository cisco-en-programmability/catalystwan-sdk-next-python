==========================
security.policy.ips.device
==========================


Operation: POST /dataservice/security/policy/ips/device
-------------------------------------------------------


Get ips alert devices list

.. code:: python

    def get_post_ips_alert_by_query(
        payload: Optional[Any] = None,
    ) -> List[DeviceLists]: ...


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
        client.security.policy.ips.device.get_post_ips_alert_by_query()


.. toctree::
    :maxdepth: 1

    models

