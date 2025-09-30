"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class ManufacturingActivitySyntax(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ManufacturingActivitySyntax
                | 
                | Interface dedicated to activity object managing PP words.
                | Role: This interface offers services to manage PP words of
                | activity.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def get_nc_instruction(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetNCInstruction() As CATBSTR
                |     Retrieves the NC instruction.
                | 
                |     Returns:
                |         S_OK when the method succeeds, and E_FAIL otherwise 
                |     Parameters:
                | 
                |         oPPWORDs
                |             The PP words instruction

        :return: str
        """
        return self.com_object.GetNCInstruction()

    def get_ppword_syntax(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetPPWORDSyntax() As CATBSTR
                |     Retrieves the PP words syntax.
                | 
                |     Returns:
                |         S_OK when the method succeeds, and E_FAIL otherwise 
                |     Parameters:
                | 
                |         oMode
                |             The PP words syntax

        :return: str
        """
        return self.com_object.GetPPWORDSyntax()

    def reset_ppword_syntax(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub ResetPPWORDSyntax()
                |     Resets the PP words syntax.
                | 
                |     Returns:
                |         S_OK when the method succeeds, and E_FAIL otherwise

        :return: None
        """
        return self.com_object.ResetPPWORDSyntax()

    def set_ppword_syntax(self, i_ppwor_ds: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetPPWORDSyntax(CATBSTR iPPWORDs)
                |     Sets the PP words syntax.
                | 
                |     Returns:
                |         S_OK when the method succeeds, and E_FAIL otherwise 
                |     Parameters:
                | 
                |         iPPWORDs
                |             The user PP words syntax to set

        :param str i_ppwor_ds:
        :return: None
        """
        return self.com_object.SetPPWORDSyntax(i_ppwor_ds)

    def __repr__(self):
        return f'ManufacturingActivitySyntax(name="{ self.name }")'
