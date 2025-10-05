"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class DrPatternGroup(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     DrPatternGroup
                | 
                | Interface dedicated to Pattern Group.
                | Role: This interface offers services to manage pattern group
                | feature.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def create_drilling_riveting_pattern(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Func CreateDrillingRivetingPattern() As AnyObject
                |     Creates a drilling riveting pattern in this group.
                | 
                |     Parameters:
                | 
                |         oDrMfgPattern
                |             The newly created pattern.

        :return: AnyObject
        """
        return AnyObject(self.com_object.CreateDrillingRivetingPattern())

    def get_manufacturing_features(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Func GetManufacturingFeatures() As CATSafeArrayVariant
                |     Get the group children (patterns and groups).
                | 
                |     Parameters:
                | 
                |         oList
                |             List of drilling riveting patterns and pattern groups

        :return: tuple
        """
        return self.com_object.GetManufacturingFeatures()

    def __repr__(self):
        return f'DrPatternGroup(name="{ self.name }")'
