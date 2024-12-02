===================================
software.compliance.ip.origin.check
===================================


Operation: POST /dataservice/software/compliance/ip/origin/check
----------------------------------------------------------------


Block IP based on list

.. code:: python

    def check_given_ip_list(
        payload: Optional[Any] = None,
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
        client.software.compliance.ip.origin.check.check_given_ip_list()


