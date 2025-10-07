"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class SemanticGDTCommonZone(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SemanticGDTCommonZone
                | 
                | Interface for accessing Common Zone, CZ, modifier on a Semantic GDT (ISO
                | Standard only).
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def modifier(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Modifier() As CATBSTR (Read Only)
                |     Retrieves CZ modifier display.
                |     Empty string is returned if modifier not applied. 

        :return: str
        """

        return self.com_object.Modifier

    def __repr__(self):
        return f'SemanticGdtCommonZone(name="{ self.name }")'
