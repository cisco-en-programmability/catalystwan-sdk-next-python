======
device
======


Operation: GET /dataservice/device
----------------------------------


List all devices

.. code:: python

    def get(
        site_id: Optional[str] = None,
        include_tenantv_smart: Optional[bool] = None,
    ) -> List[DeviceData]: ...


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
        client.device.get()


.. toctree::
    :maxdepth: 1

    aaa/index
    acl/index
    action/index
    app_hosting/index
    app_route/index
    app/index
    appqoe/index
    arp
    autonomousversion/index
    bfd/index
    bgp/index
    block_sync
    bridge/index
    bytenants
    cedgecflowd/index
    cellular/index
    cellular_eiolte/index
    cflowd/index
    cfm/index
    cloudx/index
    compliance/index
    config/index
    configuration/index
    control/index
    counters/index
    crashlog/index
    csp/index
    cts_pac
    devicestatus/index
    dhcp/index
    dhcpv6/index
    dot1x/index
    downloaded_images
    dpi/index
    dre/index
    dual_static_route_tracker
    eigrp/index
    enable_sdavc
    endpoint_tracker
    endpoint_tracker_group
    environment_data/index
    featurelist/index
    file_based/index
    geofence/index
    hardware/index
    hardwarehealth/index
    history/index
    igmp/index
    interface/index
    ip/index
    ipsec/index
    ipv6/index
    keyvalue
    lacp/index
    license/index
    logging
    models/index
    monitor
    multicast/index
    ndv6/index
    nms/index
    ntp/index
    omp/index
    ondemand/index
    orchestrator/index
    ospf/index
    pim/index
    pki/index
    policer
    policy/index
    powerconsumption/index
    ppp/index
    pppoe/index
    qfp/index
    queues
    reachable/index
    reboothistory/index
    redundancy_group/index
    role_based_counters
    role_based_ipv6_counters
    role_based_ipv6_permissions
    role_based_permissions
    role_based_sgt_map
    sdwan_global_drop_statistics
    sdwan_stats
    security/index
    sfp/index
    sig/index
    smu/index
    software/index
    sse/index
    sslproxy/index
    static_route_tracker
    stats
    status
    sxp_connections
    sync_status
    syncall/index
    system/index
    tcpopt/index
    tcpproxy/index
    tier
    tloc/index
    tlocutil/index
    tools/index
    transport/index
    tunnel/index
    ucse/index
    umbrella/index
    unclaimed/index
    unconfigured/index
    unreachable
    users/index
    utd/index
    vdsl_service/index
    vedgeinventory/index
    virtual_application/index
    vm/index
    vmanage/index
    voice/index
    voiceisdninfo/index
    voicet1e1controllerinfo/index
    vpn
    vrrp
    wireless/index
    wlan/index
    models

