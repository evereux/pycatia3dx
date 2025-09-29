"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class VSOMorphingUpdate(AnyObject):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     VSOMorphingUpdate
                | 
                | Interface representing a RSO law or morphing feature.
                | 
                | Role: Components that implement CATIAVSOMorphingUpdate are Virtual to Real
                | Shape Morphind law and morphing features
                | 
                | ClassReference, Class#MethodReference, #InternalMethod...
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def update_input_file(self, i_new_file_path: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub UpdateInputFile(CATBSTR iNewFilePath)

        :param str i_new_file_path:
        :return: None
        """
        return self.com_object.UpdateInputFile(i_new_file_path)

    def __repr__(self):
        return f'VsoMorphingUpdate(name="{self.name}")'
