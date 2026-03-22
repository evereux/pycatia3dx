"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.collection import Collection
from pycatia3dx.sde.ssm_cutting_input import SsmCuttingInput
from pycatia3dx.types.general import CATVariant


class SsmCuttingInputs(Collection):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     SsmCuttingInputs
                | 
                | Role: This interface is collection of CuttingInputs
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=SsmCuttingInput)
        self.com_object = com_object

    def item(self, i_index: CATVariant) -> SsmCuttingInput:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Item(CATVariant iIndex) As SsmCuttingInput
                |     Retrieves a Cutting Input
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of Cutting Input 

        :param CATVariant i_index:
        :return: SsmCuttingInput
        """
        return SsmCuttingInput(self.com_object.Item(i_index))

    def __repr__(self):
        return f'SsmCuttingInputs(name="{self.name}")'
