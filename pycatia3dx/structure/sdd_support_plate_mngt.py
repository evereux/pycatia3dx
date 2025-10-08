"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.structure.sdd_plate import SddPlate
from pycatia3dx.structure.sdd_plates import SddPlates


class SddSupportPlateMngt(AnyObject):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SddSupportPlateMngt
                | 
                | Object managing the Plates on which this Stiffener/StiffenerOnFreeEdge is
                | attached to.
                | Role: Manages the plates on which this Stiffener/StiffenerOnFreeEdge is
                | attached to.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def other_support_plates(self) -> SddPlates:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property OtherSupportPlates() As SddPlates
                |     Returns or Sets the other support Plates on which this is attached
                |     to.
                | 
                |     Example:
                | 
                | 
                |              This example retrieves in OtherSupportPlates.
                |              
                | 
                |              Dim ObjSddSupportPlateMngt As SddSupportPlateMngt
                |              Set ObjSddSupportPlateMngt = ObjSddStiffener.SddSupportPlateMngt
                |              ObjSddPlates = ObjSddSupportPlateMngt.OtherSupportPlates

        :return: SddPlates
        """

        return SddPlates(self.com_object.OtherSupportPlates)

    @other_support_plates.setter
    def other_support_plates(self, value: SddPlates):
        """
        :param SddPlates value:
        """

        self.com_object.OtherSupportPlates = value

    @property
    def reference_support_plate(self) -> SddPlate:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ReferenceSupportPlate() As SddPlate (Read Only)
                |     Returns the Source ReferencePlate on which this is attached to. This plate
                |     is used for: This plate is set by StrProfileSurfSurf.FirstSurface or
                |     StrProfileCrv.Reference.

        :return: SddPlate
        """

        return SddPlate(self.com_object.ReferenceSupportPlate)

    def add_other_support_plate(self, i_sdd_plate: SddPlate) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub AddOtherSupportPlate(SddPlate iSddPlate)
                |     Adds a support Plate.
                |     Role: Allows adding a support Plate.
                | 
                |     Parameters:
                | 
                |         iSddPlate
                |             SddPlate.

        :param SddPlate i_sdd_plate:
        :return: None
        """
        return self.com_object.AddOtherSupportPlate(i_sdd_plate.com_object)

    def promote_to_reference_plate(self, i_other_support_plate: SddPlate) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub PromoteToReferencePlate(SddPlate iOtherSupportPlate)
                |     Promotes a support Plate to a ReferencePlate and move the previous
                |     ReferencePlate to the list of the other support Plates.
                |     Role: Allows changing the ReferencePlate.
                | 
                |     Parameters:
                | 
                |         iOtherSupportPlate
                |             Support Plate to be promoted to ReferencePlate.

        :param SddPlate i_other_support_plate:
        :return: None
        """
        return self.com_object.PromoteToReferencePlate(i_other_support_plate.com_object)

    def remove_other_support_plate(self, i_sdd_plate: SddPlate) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub RemoveOtherSupportPlate(SddPlate iSddPlate)
                |     Removes a support Plate.
                |     Role: Allows removing a support Plate.
                | 
                |     Parameters:
                | 
                |         iSddPlate
                |             Support Plate to remove. 

        :param SddPlate i_sdd_plate:
        :return: None
        """
        return self.com_object.RemoveOtherSupportPlate(i_sdd_plate.com_object)

    def __repr__(self):
        return f'SddSupportPlateMngt(name="{self.name}")'
