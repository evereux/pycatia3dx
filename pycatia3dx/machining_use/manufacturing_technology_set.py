"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.knowledge_interfaces.parameter import Parameter
from pycatia3dx.system.any_object import AnyObject


class ManufacturingTechnologySet(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ManufacturingTechnologySet
                | 
                | Interface representing Machine Technology Set.
                | Role: This interface offers services to manage Machine Technology
                | Set.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def get_parameter_names(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetParameterNames() As CATSafeArrayVariant
                |     Retrieves the Technonology Paramter Names defined on the
                |     Machine.
                | 
                |     Parameters:
                | 
                |         oListParamNames
                |             Techno Parameter Names defined on the Machine. 
                | 
                |     Returns:
                |         Return code.
                |         Legal values:
                | 
                |             S_OK: the List is defined
                |             E_FAIL: otherwise

        :return: tuple
        """
        return self.com_object.GetParameterNames()

    def get_techno_parameter_value(self, i_attribute: str) -> Parameter:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetTechnoParameterValue(CATBSTR iAttribute) As Parameter
                |     Retrieves value of a CATICkeParm TechnoParameter.
                | 
                |     Parameters:
                | 
                |         iAttribute
                |             The name of the Technonology Paramter 
                |         oValue
                |             The CKE value 
                | 
                |     See also:
                |         CATICkeParm

        :param str i_attribute:
        :return: Parameter
        """
        return Parameter(self.com_object.GetTechnoParameterValue(i_attribute))

    def __repr__(self):
        return f'ManufacturingTechnologySet(name="{ self.name }")'
