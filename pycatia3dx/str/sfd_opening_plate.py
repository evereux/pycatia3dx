"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class SfdOpeningPlate(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SfdOpeningPlate
                | 
                | Object to filter a Structure Functional Modeler Opening for
                | Plate.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def move_to_opening_p_pr_set(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub MoveToOpeningPPrSet()
                |     Moves the PlateOpening to the OpeningPPrSet. So this Opening will now
                |     interrupt the stiffeners.
                | 
                |     Example:
                | 
                | 
                |              This example moves this opening to
                |              OpeningPlateProfileSet.
                |              
                | 
                |              Dim ObjSfdOpeningPlate As SfdOpeningPlate
                |              Set ObjSfdOpeningPlate = ObjStrOpening.GetItem("SfdOpeningPlate")
                |              ObjSfdOpeningPlate.MoveToOpeningPPrSet

        :return: None
        """
        return self.com_object.MoveToOpeningPPrSet()

    def move_to_opening_p_set(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub MoveToOpeningPSet()
                |     Moves the PlateOpening to the OpeningPSet. So this Opening will not
                |     interrupt the stiffeners.
                | 
                |     Example:
                | 
                | 
                |              This example moves this opening to
                |              OpeningPlateSet.
                |              
                | 
                |              ObjSfdOpeningPlate.MoveToOpeningPSet

        :return: None
        """
        return self.com_object.MoveToOpeningPSet()

    def __repr__(self):
        return f'SfdOpeningPlate(name="{ self.name }")'
