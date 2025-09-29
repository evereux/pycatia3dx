"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.plm_modeller_base.plm_entity import PLMEntity
from pycatia3dx.product_structure_client.vpm_instances import VPMInstances
from pycatia3dx.product_structure_client.vpm_publications import VPMPublications
from pycatia3dx.product_structure_client.vpm_rep_instances import VPMRepInstances


class VPMReference(PLMEntity):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     PLMModelerBaseIDLItf.PLMEntity
                |                         VPMReference
                | 
                | Represents the PLM Product Reference.
                | A PLM Product Reference has children: PLM Product Instances or PLM Product
                | Representation Instances or PLM Product Publications.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def instances(self) -> VPMInstances:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Instances() As VPMInstances (Read Only)
                |     Returns the collection of PLM Product Instances.
                | 
                |     Example:
                | 
                |            This example shows you how to get the PLM Product Instances children
                |            of a PLM Product Reference.
                |            
                | 
                |            Dim  oProdRef  As VPMReference
                |            .....
                |            Dim  cListInstances As VPMInstances
                |            Set  cListInstances = oProdRef.Instances

        :return: VPMInstances
        """

        return VPMInstances(self.com_object.Instances)

    @property
    def publications(self) -> VPMPublications:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Publications() As VPMPublications (Read Only)
                |     Returns the collection of PLM Product Publications.
                | 
                |     Example:
                | 
                |            This example shows you how to get the PLM Product Publications
                |            children of a PLM Product Reference.
                |            
                | 
                |            Dim  oProdRef  As VPMReference
                |            .....
                |            Dim  cListPublications As VPMPublications
                |            Set  cListPublications = oProdRef.Publications

        :return: VPMPublications
        """

        return VPMPublications(self.com_object.Publications)

    @property
    def rep_instances(self) -> VPMRepInstances:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property RepInstances() As VPMRepInstances (Read Only)
                |     Returns the collection of PLM Product Representation
                |     Instances.
                | 
                |     Example:
                | 
                |             This example shows you how to get the PLM Product Representation
                |             Instances children of a PLM Product Reference.
                |            
                | 
                |            Dim  oProdRef  As VPMReference
                |            .....
                |            Dim  cListRepInstances As VPMRepInstances
                |            Set  cListRepInstances = oProdRef.RepInstances

        :return: VPMRepInstances
        """

        return VPMRepInstances(self.com_object.RepInstances)

    def __repr__(self):
        return f'VpmReference(name="{self.name}")'
