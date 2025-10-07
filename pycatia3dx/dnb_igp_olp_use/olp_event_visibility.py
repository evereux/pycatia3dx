"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.dnb_igp_olp_use.olp_choreography_event import OLPChoreographyEvent


class OLPEventVisibility(OLPChoreographyEvent):

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
                |                         OlpEventVisibility
                | 
                | Represents a visibility (hide/show) choreography event added to a motion
                | instruction in a task.
                | 
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
                |     Get/Set the duration of the event. Default value is 0 (infinite)

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
    def show(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Show() As boolean
                |     Get/Set whether this event hides or shows the product(s). If TRUE they are
                |     shown, if FALSE, they are hidden.

        :return: bool
        """

        return self.com_object.Show

    @show.setter
    def show(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.Show = value

    def add_product_by_name(self, i_name: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub AddProductByName(CATBSTR iName)
                |     Adds a product to the Visibility activity by name.
                |     The current editor is searched for product that contain this name. If the
                |     name is not found a warning is posted, but the function succeeds. If multiple
                |     matches are found, they are all added, but a warning is
                |     issued.
                | 
                |     Parameters:
                | 
                |         iName
                |             The name of the product to hide or show.

        :param str i_name:
        :return: None
        """
        return self.com_object.AddProductByName(i_name)

    def get_product_names(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetProductNames() As CATSafeArrayVariant
                |     Get all the product names being hidden or shown.

        :return: tuple
        """
        return self.com_object.GetProductNames()

    def remove_product_by_name(self, i_name: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub RemoveProductByName(CATBSTR iName)
                |     Remove a product from the list.

        :param str i_name:
        :return: None
        """
        return self.com_object.RemoveProductByName(i_name)

    def __repr__(self):
        return f'OLPEventVisibility(name="{ self.name }")'
