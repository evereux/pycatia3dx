"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-13 15:35:27.265802

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class Printer(AnyObject):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     Printer
                | 
                | Represents a printer handled by the printing subsystem.
                | This object is read only and gives access to some properties of the
                | printer.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def device_name(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Property DeviceName() As CATBSTR (Read Only)
                |     Returns the printer device name.
                | 
                |     Example:
                |         This example displays the device name of the myPrinter
                |         printer.
                | 
                |          MsgBox myPrinter.DeviceName

        :return: str
        """

        return self.com_object.DeviceName

    @property
    def orientation(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Property Orientation() As CatPaperOrientation (Read Only)
                |     Returns or sets the default paper orientation.
                | 
                |     Example:
                |         This example retrieves in DefaultPaperOrientation the default paper
                |         orientation of the myPrinter printer.
                | 
                |          Dim DefaultPaperOrientation As CatPaperOrientation
                |          DefaultPaperOrientation = myPrinter.Orientation

        :return: int
        """

        return self.com_object.Orientation

    @property
    def paper_height(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Property PaperHeight() As float (Read Only)
                |     Returns the default paper height.
                | 
                |     Example:
                |         This example retrieves in Height the default paper height of the
                |         myPrinter printer.
                | 
                |          Dim Height
                |          Height = myPrinter.PaperHeight

        :return: float
        """

        return self.com_object.PaperHeight

    @property
    def paper_size(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Property PaperSize() As CatPaperSize (Read Only)
                |     Returns the default paper size.
                | 
                |     Example:
                |         This example retrieves in DefaultPaperSize the default paper size of
                |         the myPrinter printer.
                | 
                |          Dim DefaultPaperSize As CatPaperSize
                |          DefaultPaperSize = myPrinter.PaperSize

        :return: CatPaperSize
        """

        return self.com_object.PaperSize

    @property
    def paper_width(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Property PaperWidth() As float (Read Only)
                |     Returns the default paper width.
                | 
                |     Example:
                |         This example retrieves in Width the default paper width of the
                |         myPrinter printer.
                | 
                |          Dim Width As float
                |          Width = myPrinter.PaperWidth

        :return: float
        """

        return self.com_object.PaperWidth

    def __repr__(self):
        return f'Printer(name="{self.name}")'
