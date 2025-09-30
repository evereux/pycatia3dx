"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.plm_validation.marker import Marker


class MarkerText(Marker):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     PLMValidationIDLItf.Marker
                |                         MarkerText
                | 
                | Allows management of Marker Text information.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def text(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Text() As CATBSTR
                |     Returns or sets the text for a text marker.
                | 
                |     Example:
                | 
                |          This example retrieves the text
                |
                |          Dim text As String
                |          text = oMarkerText.Text

        :return: str
        """

        return self.com_object.Text

    @text.setter
    def text(self, value: str):
        """
        :param str value:
        """

        self.com_object.Text = value

    @property
    def text_font(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property TextFont() As CATBSTR
                |     Returns or sets the text's font for a marker.
                | 
                |     Example:
                | 
                |          This example retrieves text font
                |
                |          Dim font As String
                |          font = oMarkerText.TextFont

        :return: str
        """

        return self.com_object.TextFont

    @text_font.setter
    def text_font(self, value: str):
        """
        :param str value:
        """

        self.com_object.TextFont = value

    @property
    def text_size(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property TextSize() As double
                |     Returns or sets the text's size for a marker.
                | 
                |     Example:
                | 
                |          This example retrieves the text size
                |
                |          Dim size As Double
                |          size = oMarkerText.TextSize

        :return: float
        """

        return self.com_object.TextSize

    @text_size.setter
    def text_size(self, value: float):
        """
        :param float value:
        """

        self.com_object.TextSize = value

    def __repr__(self):
        return f'MarkerText(name="{ self.name }")'
