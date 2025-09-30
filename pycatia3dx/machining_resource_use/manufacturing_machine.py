"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class ManufacturingMachine(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ManufacturingMachine
                | 
                | Interface dedicated to Machine objects management.
                | Role: This interface offers services to manage mainly the Machine
                | object.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def get_post_processor_file(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetPostProcessorFile() As CATBSTR
                |     Retrieves the post processor file associated to the
                |     Machine.
                | 
                |     Parameters:
                | 
                |         oFilePath
                |             The path to the PP Library file associated to the Machine.
                |             
                | 
                |     Returns:
                |         Return code.
                |         Legal values:
                | 
                |             S_OK: the file is defined
                |             E_FAIL: otherwise

        :return: str
        """
        return self.com_object.GetPostProcessorFile()

    def __repr__(self):
        return f'ManufacturingMachine(name="{ self.name }")'
