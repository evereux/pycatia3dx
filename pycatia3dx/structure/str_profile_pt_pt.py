"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.mode.reference import Reference
from pycatia3dx.system.any_object import AnyObject


class StrProfilePtPt(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     StrProfilePtPt
                | 
                | Object to manage member created with 2 points Role: To manage member created
                | with 2 points.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def end_point(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property EndPoint() As Reference
                |     Returns or Sets the Profile's End point.
                | 
                |     Example:
                | 
                | 
                |              This example gets the end point of the Profile  
                |              
                | 
                |              Set RefEtartPoint = ObjStrProfilePtPt.EndPoint

        :return: Reference
        """

        return Reference(self.com_object.EndPoint)

    @end_point.setter
    def end_point(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.EndPoint = value

    @property
    def start_point(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property StartPoint() As Reference
                |     Returns or Sets the Profile's Start point.
                | 
                |     Example:
                | 
                | 
                |              This example sets the start point of the Profile 
                |              
                | 
                |              Dim ObjStrProfilePtPt As StrProfilePtPt
                |              Set ObjStrProfilePtPt = ObjSfdMember.StrProfilePtPt
                |              ObjStrProfilePtPt.StartPoint = RefStartPoint

        :return: Reference
        """

        return Reference(self.com_object.StartPoint)

    @start_point.setter
    def start_point(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.StartPoint = value

    def __repr__(self):
        return f'StrProfilePtPt(name="{ self.name }")'
