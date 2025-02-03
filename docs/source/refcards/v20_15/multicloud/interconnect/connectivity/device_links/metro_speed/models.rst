======
Models
======


.. code:: python

    from typing import List, Any, Optional, Literal, Dict, Union

    InterconnectTypeParam = Literal["EQUINIX", "MEGAPORT"]


    class InlineResponse20012:
        # Device-Link metro speed
        dl_metro_bandwidth: Optional[int]


    class InterconnectDeviceLinkDeviceList:
        # Interface used on the Interconnect Gateway to connect to the Device-Link.
        device_interface_id: Optional[str]
        # IP assigned to the Interconnect Gateway interface to connect to the Device-Link.
        device_intf_ip_address: Optional[str]
        # Name of the Interconnect Gateway in the Device-Link.
        device_name: Optional[str]
        # Uuid of Interconnect Gateway in the Device-Link.
        device_uuid: Optional[str]
        # IP assigned to the loopback interface of the Interconnect Gateway to form SDWAN tunnel.
        egw_loop_back_cidr: Optional[str]


    class InterconnectDeviceLink:
        """
        Interconnect Device-Link Object
        """

        # Device-Link Bandwidth Input.
        bandwidth: str
        # Name of the Interconnect Device-Link.
        device_link_name: str
        edge_account_id: str
        edge_type: str
        # Uuid of the Interconnect Device-Link
        device_link_uuid: Optional[str]
        # Subnet pool for Interconnect Gateway interfaces in the Device-Link.
        device_linksubnet: Optional[str]
        device_list: Optional[List[InterconnectDeviceLinkDeviceList]]
        # Device-Link Bandwidth at a given Metro.
        dl_metro_bandwidth: Optional[str]
        edge_account_name: Optional[str]
        # Device-Link Bandwidth.
        link_bandwidth: Optional[str]
        resource_state: Optional[str]
        resource_state_message: Optional[str]
        resource_state_update_ts: Optional[str]
        # Subnet pool for Interconnect Gateway interfaces in the Device-Link.
        subnet: Optional[str]
        # Version of the payload.
        version: Optional[str]


