"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.mode.references import References
from pycatia3dx.system.any_object import AnyObject


class StrProfileSubElementMngt(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     StrProfileSubElementMngt
                | 
                | Interface representing the Structure Detail Design Profile Sub
                | Elements.
                | Role: This interface manages the SDD Profile Sub Elements.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def get_edges(self, i_name_1: str, i_name_2: str) -> References:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetEdges(CATBSTR iName_1,CATBSTR iName_2) As References
                |     Returns the CATIAReference objects.
                | 
                |     Example:
                | 
                |          
                |              
                |              This example retrieves in oListOfEdges from
                |              StrProfileSubElementMngt object.
                |              
                | 
                |              Dim oListOfEdges As References
                |              Set oListOfEdges = oObjSddProfileSubElementMngt.GetEdges("Start", "WebInner-")

        :param str i_name_1:
        :param str i_name_2:
        :return: References
        """
        return References(self.com_object.GetEdges(i_name_1, i_name_2))

    def get_faces(self, i_name: str) -> References:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetFaces(CATBSTR iName) As References
                |     Returns the CATIAReference objects.
                | 
                |     Example:
                | 
                |          
                |              
                |              This example retrieves in oListOfFaces from
                |              StrProfileSubElementMngt object.
                |              
                | 
                |              Dim oListOfFaces As References
                |              Set oListOfFaces = oObjSddProfileSubElementMngt.GetFaces("WebInner+")

        :param str i_name:
        :return: References
        """
        return References(self.com_object.GetFaces(i_name))

    def __repr__(self):
        return f'StrProfileSubElementMngt(name="{ self.name }")'
