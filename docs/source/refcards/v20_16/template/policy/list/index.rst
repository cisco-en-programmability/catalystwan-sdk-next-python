====================
template.policy.list
====================


Operation: GET /dataservice/template/policy/list
------------------------------------------------


Get all policy lists

.. code:: python

    def get_all_policy_lists() -> List[Any]: ...


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
        client.template.policy.list.get_all_policy_lists()


.. toctree::
    :maxdepth: 1

    app/index
    appprobe/index
    aspath/index
    class_/index
    color/index
    community/index
    dataipv6prefix/index
    dataprefix/index
    dataprefixall/index
    dataprefixfqdn/index
    expandedcommunity/index
    extcommunity/index
    faxprotocol/index
    fqdn/index
    geolocation/index
    identity/index
    ipprefixall/index
    ipssignature/index
    ipv6prefix/index
    localapp/index
    localdomain/index
    mediaprofile/index
    mirror/index
    modempassthrough/index
    policer/index
    port/index
    preferredcolorgroup/index
    prefix/index
    protocolname/index
    region/index
    scalablegrouptag/index
    site/index
    sla/index
    supervisorydisc/index
    tgapikey/index
    tloc/index
    translationprofile/index
    translationrules/index
    trunkgroup/index
    umbrelladata/index
    urlblacklist/index
    urlwhitelist/index
    vpn/index
    webex/index
    zone/index

