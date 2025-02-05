==========================
dca.template.policy.vsmart
==========================


Operation: POST /dataservice/dca/template/policy/vsmart
-------------------------------------------------------


Get vSmart template list

.. code:: python

    def get_vsmart_template_list_dca(
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
        client.dca.template.policy.vsmart.get_vsmart_template_list_dca()


