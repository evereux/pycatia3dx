"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class DrPatternGroupFactory(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     DrPatternGroupFactory
                | 
                | Interface implemented by pattern group and manufacturing product used to create
                | pattern groups.
                | Role: This interface allows creation of pattern groups.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def create_pattern_group(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Func CreatePatternGroup() As AnyObject
                |     Creates a pattern group.
                | 
                |     Parameters:
                | 
                |         oDrPatternGroup
                |             The newly created pattern group. 

        :return: AnyObject
        """
        return AnyObject(self.com_object.CreatePatternGroup())

    def __repr__(self):
        return f'DrPatternGroupFactory(name="{ self.name }")'
