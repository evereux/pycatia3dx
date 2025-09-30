"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.interfaces.service import Service
from pycatia3dx.plm_modeller_base.plm_entity import PLMEntity
from pycatia3dx.types.general import CATVariant


class PLMScriptService(Service):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     InfInterfaces.Service
                |                         PLMScriptService
                | 
                | Interface that offer services to handle scripts that are stored in
                | database.
                | 
                | Example of how to retrieve such an object using
                | Application.GetSessionService:
                | 
                |  Dim aScriptSrv as PLMScriptService
                |  Set aScriptSrv = CATIA.GetSessionService("PLMScriptService")
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def execute_script_v6(self, i_plm_entity: PLMEntity, i_type: int, i_program_name: str, i_function_name: str, i_parameters: tuple) -> CATVariant:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func ExecuteScriptV6(PLMEntity iPLMEntity,CatScriptLibraryType iType,CATBSTR
                | iProgramName,CATBSTR iFunctionName,CATSafeArrayVariant iParameters) As
                | CATVariant
                |     Executes a script from a script library that is stored in
                |     database.
                | 
                |     Parameters:
                | 
                |         iPLMEntity
                |             The library in which the script is contained as a PLM entity.
                |             
                |         iType
                |             The type of the library (macro language) 
                |         iProgramName
                |             The name of the program in the library 
                |         iFunctionName
                |             The name of the function to invoke 
                |         iParameters
                |             An array of parameters for the function 
                |         oResult
                |             The value returned by the function (if any) 
                | 
                |     Example:
                |         This example executes the function CATMain in the program Macro1.catvbs
                |         contained by a PLM entity which PLM_ExternalID is
                |         VBScriptProject1.
                | 
                |          Dim iPLMEntity As PLMEntity
                |          Dim aSearchSrv
                |          Set aSearchSrv = CATIA.GetSessionService("PLMSearch")
                |          '... use aSearchSrv to retrieve the PLM entity which PLM_ExternalID is
                |          VBScriptProject1
                |          Dim params()
                |          aScriptSrv.ExecuteScriptV6iPLMEntity, catScriptLibraryTypeDirectory,
                |          "Macro1.catvbs", "CATMain", params

        :param PLMEntity i_plm_entity:
        :param int i_type:
        :param str i_program_name:
        :param str i_function_name:
        :param tuple i_parameters:
        :return: CATVariant
        """
        return self.com_object.ExecuteScriptV6(i_plm_entity.com_object, i_type, i_program_name, i_function_name, i_parameters)

    def __repr__(self):
        return f'PlmScriptService(name="{ self.name }")'
