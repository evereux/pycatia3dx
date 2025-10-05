"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.sma_mpa_structural_mode.sim_composite_grid_elem_ref import SimCompositeGridElemRef


class SimCompositeGridElemRefGroup(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimCompositeGridElemRefGroup
                | 
                | Represents the Composite Cells Elements Reference group
                | object.
                | Given a SimCompositeGrid object, you can retrieve a SimCompositeCellsElemRefGroup as below: ... Refer SMAIAMpaCompositeGrid.idl to create/retrieve SimCompositeGrid. ... Dim myCompositeRefElemGroup As SimCompositeCellsElemRefGroup Set myCompositeRefElemGroup = myCompositeGrid.AddNewRefGroup or Dim listElemsGrp listElemsGrp = myCompositeGrid.GetElementRefGroups ...Loop for listSize = UBound(listElemsGrp) - LBound(listElemsGrp) + 1 if needed.. myCompositeRefElemGroup = listElemsGrp(0)
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def add_new_elem_ref(self) -> SimCompositeGridElemRef:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func AddNewElemRef() As SimCompositeGridElemRef
                |     Creates a new reference element inside the group.
                | 
                |     Returns:
                |         New reference element of the group.

        :return: SimCompositeGridElemRef
        """
        return SimCompositeGridElemRef(self.com_object.AddNewElemRef())

    def get_element_refs(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetElementRefs() As CATSafeArrayVariant
                |     Retreives all reference elements in the group.
                | 
                |     Returns:
                |         List of all reference elements in the group. 

        :return: tuple
        """
        return self.com_object.GetElementRefs()

    def __repr__(self):
        return f'SimCompositeGridElemRefGroup(name="{ self.name }")'
