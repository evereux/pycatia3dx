"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.plm_modeller_base.plm_entity import PLMEntity
from pycatia3dx.product_structure_client.parent_vpm_rep_instances import ParentVPMRepInstances
from pycatia3dx.product_structure_client.vpm_reference import VPMReference


class VPMRepReference(PLMEntity):
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
                |                         VPMRepReference
                | 
                | Represents the PLM Product Representation Reference.
                | A PLM Product Representation Reference contains geometrical or technological
                | data.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def father(self) -> VPMReference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Father() As VPMReference (Read Only)
                |     Returns the parent PLM Product Reference.
                |     Role: This method only works for a once instantiable PLM Product
                |     Representation Reference. It returns the PLM Product Reference containing the
                |     unique instance of the current PLM Product Representation
                |     Reference.
                | 
                |     Example:
                | 
                |             This first example shows you how to get the PLM Product Reference
                |             containing the unique instance of the 
                |             current PLM Product Representation Reference.
                |            
                | 
                |          
                |            Dim  oProdRepRef As VPMRepReference
                |            .....
                |            Dim  oProdRefAsParent  As VPMReference
                |            Set oProdRefAsParent = oProdRepRef.Father

        :return: VPMReference
        """

        return VPMReference(self.com_object.Father)

    @property
    def parent_rep_instances(self) -> ParentVPMRepInstances:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ParentRepInstances() As ParentVPMRepInstances (Read
                | Only)
                |     Returns the set of Parent PLM Representation Instances of a Representation
                |     Reference.
                | 
                |     Example:
                | 
                |            This example shows you how to get the PLM Product Representation
                |            Instances parent of a PLM Representation Reference.
                |            
                | 
                |              Dim  oProdRepRef  As VPMRepReference
                |              .....
                |              Dim  cListRepInstances As ParentVPMRepInstances
                |              Set  cListRepInstances = oProdRepRef.ParentRepInstances

        :return: ParentVPMRepInstances
        """

        return ParentVPMRepInstances(self.com_object.ParentRepInstances)

    def __repr__(self):
        return f'VpmRepReference(name="{self.name}")'
