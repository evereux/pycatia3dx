"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.mode.references import References
from pycatia3dx.system.any_object import AnyObject


class SddPlateSubElementMngt(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SddPlateSubElementMngt
                | 
                | Interface representing the Structure Detail Design Plate Sub
                | Elements.
                | Role: This interface manages the SDD Plate Sub Elements.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def get_faces(self, i_name: int) -> References:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetFaces(CATStrPlateFaceName iName) As References
                |     Returns the CATIAReference objects.
                | 
                |     Example:
                |
                |              This example retrieves in oListOfFaces from SddPlateSubElementMngt
                |              object.
                |
                |              Dim oListOfFaces As References
                |              Set oListOfFaces = oObjSddPlateSubElementMngt.GetFaces(1)

        :param int i_name:
        :return: References
        """
        return References(self.com_object.GetFaces(i_name))

    def __repr__(self):
        return f'SddPlateSubElementMngt(name="{ self.name }")'
