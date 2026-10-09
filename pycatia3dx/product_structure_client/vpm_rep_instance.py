"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.plm_modeller_base.plm_entity import PLMEntity
from pycatia3dx.product_structure_client.vpm_rep_reference import VPMRepReference


class VPMRepInstance(PLMEntity):
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
                |                         VPMRepInstance
                | 
                | Represents a PLM Product Representation Instance.
                | A PLM Product Representation Instance is an instance of a PLM Product
                | Representation Reference, and the child of a PLM Product Reference that you
                | retrieve by AnyObject.get_Parent .
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def reference_instance_of(self) -> VPMRepReference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ReferenceInstanceOf() As VPMRepReference (Read Only)
                |     Returns the instantiated PLM Product Representation
                |     Reference.
                |     Role: This method returns the PLM Product Representation Reference used to
                |     instantiate the current PLM Product Representation
                |     Instance.
                | 
                |     Example:
                | 
                |            This example shows you how to get the PLM Product Representation
                |            Reference used to  
                |           instantiate the current PLM Product Representation
                |           Instance.
                |
                |            Dim  oProdRepRef  As VPMRepReference
                |            Dim  oProdRepInst As VPMRepInstance
                |            Set  oProdRepRef = oProdRepInst.ReferenceInstanceOf
                |
                |            This second example shows you how to get the PLM Product Reference
                |            owning the current instance.
                |
                |            Dim  oProdRepInst        As VPMRepInstance
                |            .....
                |            Dim  oProdRefAsParent     As VPMReference
                |            Set oProdRefAsParent = oProdRepInst.Parent

        :return: VPMRepReference
        """

        return VPMRepReference(self.com_object.ReferenceInstanceOf)

    def __repr__(self):
        return f'VPMRepInstance(name="{self.name}")'
