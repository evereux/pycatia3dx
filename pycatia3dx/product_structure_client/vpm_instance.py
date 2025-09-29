"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.mode.position import Position
from pycatia3dx.plm_modeller_base.plm_entity import PLMEntity
from pycatia3dx.product_structure_client.vpm_reference import VPMReference


class VPMInstance(PLMEntity):
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
                |                         VPMInstance
                | 
                | Represents the PLM Product Instance.
                | A PLM Product Instance is an instance of a PLM Product Reference, and the child
                | of another one that you retrieve by AnyObject.get_Parent .
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def position(self) -> Position:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Position() As Position (Read Only)
                |     Returns the PLM Product Instance position.
                | 
                |     Example:
                | 
                |             This example shows you how to get the PLM Product instance
                |             position.
                |            
                | 
                |          
                |             Dim  oProdInstance        As VPMInstance
                |            .....
                |             Dim  oProdInstPosition  As Position
                |            Set oProdInstPosition = oProdInstance.Position

        :return: Position
        """

        return Position(self.com_object.Position)

    @property
    def reference_instance_of(self) -> VPMReference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ReferenceInstanceOf() As VPMReference (Read Only)
                |     Returns the instantiated PLM Product Reference.
                |     Role: This method returns the PLM Product Reference used to instantiate the
                |     current PLM Product Instance.
                | 
                |     Example:
                | 
                |             This first example shows you how to get the PLM Product Reference
                |             used to instantiate the current instance.
                |
                |            Dim  oProdInstance        As VPMInstance
                |            ...
                |            Dim  oProdRefAsReference  As VPMReference
                |            Set  oProdRefAsReference = oProdInstance.ReferenceInstanceOf
                |
                |             This second example shows you how to get the PLM Product Reference
                |             owning the current instance.
                |
                |            Dim  oProdInstance        As VPMInstance
                |            .....
                |            Dim  oProdRefAsParent     As VPMReference
                |            Set oProdRefAsParent = oProdInstance.Parent

        :return: VPMReference
        """

        return VPMReference(self.com_object.ReferenceInstanceOf)

    def __repr__(self):
        return f'VpmInstance(name="{self.name}")'
