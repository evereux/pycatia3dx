"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.structure.str_objects import StrObjects
from pycatia3dx.structure.str_references import StrReferences


class StrBreak(AnyObject):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     StrBreak
                | 
                | Object to manage Structure Break of a SuperPlate or Profile.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def splitting_elements(self) -> StrReferences:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SplittingElements() As StrReferences (Read Only)
                |     Returns the list of SplittingElements.
                | 
                |     Example:
                | 
                | 
                |              This example retrieves SplittingElements of the panel or
                |              profile.
                |              
                | 
                |              Set ListOfSplittingElements = ObjStrBreak.SplittingElements

        :return: StrReferences
        """

        return StrReferences(self.com_object.SplittingElements)

    def break_(self, i_list_of_splitting_elements: StrReferences) -> StrObjects:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Break(StrReferences iListOfSplittingElements) As
                | StrObjects
                |     Returns the list of newly created SuperPlates or Profiles after Breaking a
                |     SuperPlate or a Profile with splitting elements
                | 
                |     Parameters:
                | 
                |         iListOfSplittingElements
                |             The list of features splitting this SuperPlate / Profile
                |             
                | 
                |     Example:
                | 
                | 
                |              This example Breaks a panel into two panels.
                |              
                | 
                |               'Create reference of splitting element
                |               Dim SplittingElemRef As Reference
                |               Set SplittingElemRef = ObjPart.CreateReferenceFromObject(SplittingPanel)
                |               'Add splitting elements to the list
                |               Dim ListOfSplitRef As StrReferences
                |               Set ListOfSplitRef = ObjStrBreak.SplittingElements
                |               ListOfSplitRef.Add SplittingElemRef
                |               'Break the Panel
                |               Set ListOfResults = ObjStrBreak.Break(ListOfSplitRef)

        :param StrReferences i_list_of_splitting_elements:
        :return: StrObjects
        """
        return StrObjects(self.com_object.Break(i_list_of_splitting_elements.com_object))

    def __repr__(self):
        return f'StrBreak(name="{self.name}")'
