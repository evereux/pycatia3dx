"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.todo_machining_use.manufacturing_output_generator import ManufacturingOutputGenerator


class ManufacturingAptGenerator(ManufacturingOutputGenerator):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                    MachiningUseItf.ManufacturingOutputGenerator
                |                         ManufacturingAPTGenerator
                | 
                | Generator of APT output machining code.
                | 
                | See also:
                |     DELMIAManufacturingOutputGenerator
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def __repr__(self):
        return f'ManufacturingAptGenerator(name="{ self.name }")'
