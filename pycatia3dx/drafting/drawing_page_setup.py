"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.interfaces.page_setup import PageSetup


class DrawingPageSetup(PageSetup):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     InfInterfaces.PageSetup
                |                         DrawingPageSetup
                | 
                | Represents the page setup for the drawing representations.
                | 
                | The page setup is the object that stores data which defines how your
                | representations and images are actually printed on paper. This data includes
                | namely the paper size, the orientation, the bottom, top, right, and left
                | margins, the zoom factor, the banner, the printing quality, the choice of the
                | best orientation, and the choice to fit either the drawing sheet format or the
                | printer format.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def choose_best_orientation(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ChooseBestOrientation() As boolean
                |     Activates or deactivates the choice of the best
                |     orientation.
                | 
                |     Example:
                |         This example requests the best orientation to be chosen for
                |         MySheet.
                | 
                |          MySheet.DrawingPageSetUp.ChooseBestOrientation = TRUE

        :return: bool
        """

        return self.com_object.ChooseBestOrientation

    @choose_best_orientation.setter
    def choose_best_orientation(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.ChooseBestOrientation = value

    @property
    def fit_to_printer_format(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property FitToPrinterFormat() As boolean
                |     Fits the format of the print to the printer format.
                | 
                |     Example:
                |         This example turns this calculation on.
                | 
                |          MySheet.DrawingPageSetUp.FitToPrinterFormat = TRUE

        :return: bool
        """

        return self.com_object.FitToPrinterFormat

    @fit_to_printer_format.setter
    def fit_to_printer_format(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.FitToPrinterFormat = value

    @property
    def fit_to_sheet_format(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property FitToSheetFormat() As boolean
                |     Fits the format of the print to the sheet format.
                | 
                |     Example:
                |         This example turns this calculation on.
                | 
                |          MySheet.DrawingPageSetUp.FitToSheetFormat = TRUE

        :return: bool
        """

        return self.com_object.FitToSheetFormat

    @fit_to_sheet_format.setter
    def fit_to_sheet_format(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.FitToSheetFormat = value

    def __repr__(self):
        return f'DrawingPageSetup(name="{ self.name }")'
