"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.dnb_igp_olp_use.olp_choreography_event import OLPChoreographyEvent


class OLPEventText(OLPChoreographyEvent):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     DNBIgpOlpUseItf.OlpChoreographyEvent
                |                         OlpEventText
                | 
                | Represents a text choreography event added to a motion instruction in a
                | task.
                | 
                | This can be used to add text popups to accompany motion instructions and
                | set/get properties
                | such as WindowName, WindowText and Duration of the text event.
                | This interface can only be used by a translator within the Robotics Off-line
                | Programming (OLP) Download or Upload command.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def duration(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Duration() As double
                |     Get/Set the duration of the text event. Default value is 0 (infinite)

        :return: float
        """

        return self.com_object.Duration

    @duration.setter
    def duration(self, value: float):
        """
        :param float value:
        """

        self.com_object.Duration = value

    @property
    def window_name(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property WindowName() As CATBSTR
                |     Get/Set the title of the Text Window used for Choreography Events

        :return: str
        """

        return self.com_object.WindowName

    @window_name.setter
    def window_name(self, value: str):
        """
        :param str value:
        """

        self.com_object.WindowName = value

    @property
    def window_text(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property WindowText() As CATBSTR
                |     Get/Set the text of the Text Window used for Choreography Events

        :return: str
        """

        return self.com_object.WindowText

    @window_text.setter
    def window_text(self, value: str):
        """
        :param str value:
        """

        self.com_object.WindowText = value

    def __repr__(self):
        return f'OLPEventText(name="{ self.name }")'
