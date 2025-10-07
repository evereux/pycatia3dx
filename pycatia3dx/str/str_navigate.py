"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.mode.references import References
from pycatia3dx.system.any_object import AnyObject


class StrNavigate(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     StrNavigate
                | 
                | Object to navigate sfd/sdd objects.
                | Role: Allows navigating sfd/sdd objects.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def get_children(self) -> References:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetChildren() As References
                |     Returns the list of all children of this object.
                | 
                |     Example:
                | 
                | 
                |              This example retrieves the penetrating profile.
                |              
                | 
                |              Set PenetratingProfile = ObjStrNavigate.GetPenetratingProfile

        :return: References
        """
        return References(self.com_object.GetChildren())

    def get_parents(self) -> References:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetParents() As References
                |     Returns list of all parents of this object.
                | 
                |     Example:
                | 
                | 
                |              This example sets the penetrating profile.
                |              
                | 
                |              ObjStrNavigate As StrNavigate
                |              Set ObjStrNavigate = ObjStrNavigates.Add
                |              Dim penetratingElem As Reference
                |              Set penetratingElem = ObjPart.CreateReferenceFromObject(ObjSfdStiffener)
                |              ObjStrNavigate.SetPenetratingProfile
                |              penetratingElem

        :return: References
        """
        return References(self.com_object.GetParents())

    def __repr__(self):
        return f'StrNavigate(name="{ self.name }")'
