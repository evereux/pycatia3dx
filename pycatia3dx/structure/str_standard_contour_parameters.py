"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.collection import Collection
from pycatia3dx.structure.str_parameter import StrParameter
from pycatia3dx.types.general import CATVariant


class StrStandardContourParameters(Collection):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     StrStandardContourParameters
                | 
                | Object for Standard Contour Parameters.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def item(self, i_index: CATVariant) -> StrParameter:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Item(CATVariant iIndex) As StrParameter
                |     Returns a standard contour parameter
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the standard contour parameter
                |             
                | 
                |     Example:
                | 
                | 
                |              This example retrieves  the first StandardContourParameter from
                |              the list.
                |              
                | 
                |               Dim ObjStrStandardContourParameters As
                |               StrStandardContourParameters
                |               Set ObjStrStandardContourParameters = ObjStrOpeningsMgr.GetStandardContourParms(ContourName)
                |               Set ObjStrParameter = ObjStrStandardContourParameters.Item(1)

        :param CATVariant i_index:
        :return: StrParameter
        """
        return StrParameter(self.com_object.Item(i_index))

    def __repr__(self):
        return f'StrStandardContourParameters(name="{self.name}")'
