"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.interfaces.service import Service


class DrawingService(Service):

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
                |                         DrawingService
                | 
                | Interface representing the service to retrieve available drawing standards and
                | sheet styles.
                | Application.GetSessionService("CATDrawingService")
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def number_of_standards(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property NumberOfStandards() As long (Read Only)
                |     Returns the number of standards in the environment.

        :return: int
        """

        return self.com_object.NumberOfStandards

    def number_of_sheet_styles(self, i_standard_name: str) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Func NumberOfSheetStyles(CATBSTR iStandardName) As long
                |     Returns the number of sheet style from a given standard.
                | 
                |     Parameters:
                | 
                |         iNumOfStandard
                |             Standard number. 
                | 
                |     Returns:
                |         the number of sheet style for the given standard.

        :param str i_standard_name:
        :return: int
        """
        return self.com_object.NumberOfSheetStyles(i_standard_name)

    def sheet_style_names_list(self, i_standard_name: str, o_list_of_sheet_style_names: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub SheetStyleNamesList(CATBSTR iStandardName,CATSafeArrayVariant
                | oListOfSheetStyleNames)
                |     Returns the list of available Sheet style for a given
                |     standard.
                | 
                |     Parameters:
                | 
                |         oListOfSheetStyleNames
                |             The list of available sheet style names.

        :param str i_standard_name:
        :param tuple o_list_of_sheet_style_names:
        :return: None
        """
        return self.com_object.SheetStyleNamesList(i_standard_name, o_list_of_sheet_style_names)

    def standard_names_list(self, o_list_of_standard_names: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub StandardNamesList(CATSafeArrayVariant
                | oListOfStandardNames)
                |     Returns the list of available standard names.
                | 
                |     Parameters:
                | 
                |         oListOfStandardNames
                |             The list of available standard names.

        :param tuple o_list_of_standard_names:
        :return: None
        """
        return self.com_object.StandardNamesList(o_list_of_standard_names)

    def __repr__(self):
        return f'DrawingService(name="{ self.name }")'
