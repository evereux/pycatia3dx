"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.knowledge_interfaces.parameter import Parameter
from pycatia3dx.system.collection import Collection
from pycatia3dx.types.general import CATVariant


class SsmParameters(Collection):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     SsmParameters
                | 
                | Object for collection of Parameters.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def item(self, i_index: CATVariant) -> Parameter:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Item(CATVariant iIndex) As Parameter
                |     Returns a parameter from the collection of parameters
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of the parameter 
                | 
                |     Example:
                | 
                | 
                |              This example retrieves first parameter from list of
                |              Parameters.
                |              
                | 
                |               Dim ObjSsmParameters As SsmParameters
                |               Set ObjSsmParameters = ObjStrDetailFeature.GetParameters
                |               Dim OffsetParameter As Parameter
                |               Set OffsetParameter = ObjSsmParameters.Item(1)

        :param CATVariant i_index:
        :return: Parameter
        """
        return Parameter(self.com_object.Item(i_index))

    def __repr__(self):
        return f'SsmParameters(name="{ self.name }")'
