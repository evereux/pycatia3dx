"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class ManufacturingComputePmaParameters(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ManufacturingComputePMAParameters
                | 
                | Interface to compute and get PMA Parameters: - MfgMinimumCornerRadius -
                | MfgMinimumChannelWidth - MfgMaximumChannelWidth - Depth - MfgBottomFilletRadius
                | - BottomColor
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def compute_parameters(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub ComputeParameters()
                |     This function computes the PMA parameters and stores for 2DMA
                |     feature
                | 
                |     Returns:
                |         S_OK or E_FAIL

        :return: None
        """
        return self.com_object.ComputeParameters()

    def get_parameter_double_value(self, i_name: str) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetParameterDoubleValue(CATBSTR iName) As double
                |     Get double parameter
                | 
                |     Parameters:
                | 
                |         return
                |             double value 
                | 
                |     Returns:
                |         S_OK or E_FAIL

        :param str i_name:
        :return: float
        """
        return self.com_object.GetParameterDoubleValue(i_name)

    def get_parameter_string_value(self, i_name: str) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetParameterStringValue(CATBSTR iName) As CATBSTR
                |     Get string parameter
                | 
                |     Parameters:
                | 
                |         return
                |             string value 
                | 
                |     Returns:
                |         S_OK or E_FAIL

        :param str i_name:
        :return: str
        """
        return self.com_object.GetParameterStringValue(i_name)

    def __repr__(self):
        return f'ManufacturingComputePmaParameters(name="{ self.name }")'
