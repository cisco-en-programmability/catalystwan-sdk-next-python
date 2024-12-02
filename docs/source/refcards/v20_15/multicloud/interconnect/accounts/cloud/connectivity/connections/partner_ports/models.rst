======
Models
======


.. code:: python

    from typing import Literal, Optional, List, Union, Dict, Any

    ConnectType = Literal[
        "AWS", "AWSHC", "INTERCONNECT_ATTACHMENT", "PRIMARY", "SECONDARY"
    ]

    CloudType = Literal[
        "AWS", "AWS_GOVCLOUD", "AZURE", "AZURE_GOVCLOUD", "GCP"
    ]

    EdgeType = Literal["EQUINIX", "MEGAPORT"]


    class InterconnectPartnerPortsDetails:
        """
        Megaport specific partner port fields.
        """

        authorization_key: Optional[str]
        # Megaport companyId for the region.
        company_uid: Optional[str]
        connect_type: Optional[ConnectType]
        # Megaport id for the region.
        product_uid: Optional[str]
        # Bandwidth speeds supported at the region.
        speed: Optional[str]
        # Cross connect (VXC) id connected to the region
        vxc_id: Optional[str]
        # Cross Connect enabled Megaport region.
        vxc_permitted: Optional[bool]


    class InterconnectPartnerPorts:
        """
        Interconnect partner port information
        """

        # Megaport specific partner port fields.
        att_partner_port: Optional[InterconnectPartnerPortsDetails]
        cloud_type: Optional[CloudType]
        edge_type: Optional[EdgeType]
        # Megaport specific partner port fields.
        eq_partner_port: Optional[InterconnectPartnerPortsDetails]
        location_id: Optional[str]
        # Megaport specific partner port fields.
        mp_partner_port: Optional[InterconnectPartnerPortsDetails]
        name: Optional[str]


    class InlineResponse2006:
        edge_partner_ports_list: Optional[List[InterconnectPartnerPorts]]


