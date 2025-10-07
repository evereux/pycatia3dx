"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.annotation.drawing_text import DrawingText
from pycatia3dx.drafting.drawing_component import DrawingComponent
from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.tps.tps_parallel_on_screen import TPSParallelOnScreen
from pycatia3dx.types.general import CATVariant


class Noa(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     Noa
                | 
                | Interface for the TPS Noa object.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def flag_text(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property FlagText() As CATBSTR
                |     Retrieves or sets Flag Text.
                | 
                |     Parameters:
                | 
                |         oText
                |             Returned text for NOA hidden text.

        :return: str
        """

        return self.com_object.FlagText

    @flag_text.setter
    def flag_text(self, value: str):
        """
        :param str value:
        """

        self.com_object.FlagText = value

    @property
    def text(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Text() As CATBSTR
                |     Retrieves or sets Text Representation.
                | 
                |     Parameters:
                | 
                |         oText
                |             Returned text for graphical representation.

        :return: str
        """

        return self.com_object.Text

    @text.setter
    def text(self, value: str):
        """
        :param str value:
        """

        self.com_object.Text = value

    def add_url(self, i_url: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub AddURL(CATBSTR iUrl)
                |     Sets an URL.
                | 
                |     Parameters:
                | 
                |         iUrl
                |             URL to Set

        :param str i_url:
        :return: None
        """
        return self.com_object.AddURL(i_url)

    def get2d_annot(self) -> DrawingText:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Get2dAnnot() As DrawingText
                |     Retrieves Drafting text.

        :return: DrawingText
        """
        return DrawingText(self.com_object.Get2dAnnot())

    def get_ditto(self) -> DrawingComponent:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetDitto() As DrawingComponent
                |     Gets the ditto as a DrawingComponent of the Noa entity.

        :return: DrawingComponent
        """
        return DrawingComponent(self.com_object.GetDitto())

    def get_modifiable_text(self, i_index: CATVariant) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetModifiableText(CATVariant iIndex) As AnyObject
                |     Gets by index a modifiable Text included in the ditto which represents this
                |     NOA.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             Index of the modifiable text. 
                |         oText
                |             returns a CATIADrawingText

        :param CATVariant i_index:
        :return: AnyObject
        """
        return AnyObject(self.com_object.GetModifiableText(i_index))

    def get_modifiable_texts_count(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetModifiableTextsCount() As long
                |     Gets the number of modifiable texts included in the ditto which represents
                |     this NOA.
                | 
                |     Parameters:
                | 
                |         oCount
                |             returns the number of modifiable text included into the ditto which
                |             represents this NOA.

        :return: int
        """
        return self.com_object.GetModifiableTextsCount()

    def get_nbr_url2(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetNbrURL2() As long
                |     Gets the number of URL.
                | 
                |     Parameters:
                | 
                |         oNumberOfURL
                |             returns param oNumberOfURL.

        :return: int
        """
        return self.com_object.GetNbrURL2()

    def modify_url(self, i_url: str, i_index: CATVariant) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub ModifyURL(CATBSTR iUrl,CATVariant iIndex)
                |     Modifies an URL.
                | 
                |     Parameters:
                | 
                |         iUrl
                |             URL to Set. 
                |         iIndex
                |             index of the URL to modify.

        :param str i_url:
        :param CATVariant i_index:
        :return: None
        """
        return self.com_object.ModifyURL(i_url, i_index)

    def remove_url(self, i_index: CATVariant) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub RemoveURL(CATVariant iIndex)
                |     Removes an URL.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             position of the URL to remove.

        :param CATVariant i_index:
        :return: None
        """
        return self.com_object.RemoveURL(i_index)

    def tps_parallel_on_screen(self) -> TPSParallelOnScreen:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func TPSParallelOnScreen() As TPSParallelOnScreen
                |     Gets the annotation on TPSParallelOnScreen interface.

        :return: TPSParallelOnScreen
        """
        return TPSParallelOnScreen(self.com_object.TPSParallelOnScreen())

    def url(self, i_index: CATVariant) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func URL(CATVariant iIndex) As CATBSTR
                |     Retrieves url.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             Index of url. 
                |         oUrl
                |             url 

        :param CATVariant i_index:
        :return: str
        """
        return self.com_object.URL(i_index)

    def __repr__(self):
        return f'Noa(name="{ self.name }")'
