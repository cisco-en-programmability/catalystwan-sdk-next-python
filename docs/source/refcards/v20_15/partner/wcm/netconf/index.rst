===================
partner.wcm.netconf
===================


Operation: POST /dataservice/partner/wcm/netconf/{nmsId}
--------------------------------------------------------


Push device configs

.. code:: python

    def push_netconf_configs(
        nms_id: str, payload: WcmNetconfConfigRequest
    ) -> WcmNetconfConfigRes: ...


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
        client.partner.wcm.netconf.push_netconf_configs()


.. toctree::
    :maxdepth: 1

    models

