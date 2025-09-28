"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class DrawingPicture(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     DrawingPicture
                | 
                | Represents a drawing picture in a drawing view.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def display_at_true_depth(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property DisplayAtTrueDepth() As boolean
                |     Checks if the picture has its "Display at true depth" property valued to
                |     True or False. Sets the "Display at true depth" property value to True or
                |     False. Role: The modification of this property to true does not necessarily
                |     means that the picture will be "Displayed at true depth". The value is ignored
                |     if the picture is created in a main view, a backgound view, in a 2D component
                |     reference, in drafting. However it can be usefull to modify its value in case
                |     of copy and paste in a 2DLayout view, in a 2D component reference for an
                |     instanciation in a 2DLayout view.
                |     Precondition: Only available for raster pictures.
                | 
                |     Returns:
                | 
                |         Legal values:
                | 
                |         S_OK
                |             Method correctly executed. 
                |         E_FAIL
                |             Method execution failed. 
                |             Precondition is not met. 
                | 
                |         Example:
                |             This example sets the display at true depth of the MyPicture
                |             picture to True
                | 
                |              MyPicture.DisplayAtTrueDepth = True

        :return: bool
        """

        return self.com_object.DisplayAtTrueDepth

    @display_at_true_depth.setter
    def display_at_true_depth(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.DisplayAtTrueDepth = value

    @property
    def picture_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property PictureType() As CatPictureType (Read Only)
                |     Gets the type of a picture.
                | 
                |     Returns:
                | 
                |         Legal values:
                | 
                |         S_OK
                |             Method correctly executed. 
                |         E_FAIL
                |             Method execution failed. 
                |             It is impossible to retrieve the type of the picture.
                |             
                | 
                |     See also:
                |         CatPictureType

        :return: int
        """

        return self.com_object.PictureType

    @property
    def crop_bottom(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property cropBottom() As double
                |     Returns or sets the cropBottom of the drawing picture. The cropBottom is
                |     the size of the margin on the bottom of the picture. The cropBottom, like any
                |     length, is measured in millimeters.
                | 
                |     Example:
                |         This example sets the cropBottom of the MyPicture drawing picture to 10
                |         mm
                | 
                |          MyPicture.cropBottom = 10.

        :return: float
        """

        return self.com_object.cropBottom

    @crop_bottom.setter
    def crop_bottom(self, value: float):
        """
        :param float value:
        """

        self.com_object.cropBottom = value

    @property
    def crop_left(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property cropLeft() As double
                |     Returns or sets the cropLeft of the drawing picture. The cropLeft is the
                |     size of the margin on the left of the picture. The cropLeft, like any length,
                |     is measured in millimeters.
                | 
                |     Example:
                |         This example sets the cropLeft of the MyPicture drawing picture to 10
                |         mm
                | 
                |          MyPicture.cropLeft = 10.

        :return: float
        """

        return self.com_object.cropLeft

    @crop_left.setter
    def crop_left(self, value: float):
        """
        :param float value:
        """

        self.com_object.cropLeft = value

    @property
    def crop_right(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property cropRight() As double
                |     Returns or sets the cropRight of the drawing picture. The cropRight is the
                |     size of the margin on the right of the picture. The cropRight, like any length,
                |     is measured in millimeters.
                | 
                |     Example:
                |         This example sets the cropRight of the MyPicture drawing picture to 10
                |         mm
                | 
                |          MyPicture.cropRight = 10.

        :return: float
        """

        return self.com_object.cropRight

    @crop_right.setter
    def crop_right(self, value: float):
        """
        :param float value:
        """

        self.com_object.cropRight = value

    @property
    def crop_top(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property cropTop() As double
                |     Returns or sets the cropTop of the drawing picture. The cropTop is the size
                |     of the margin on the top of the picture. The cropTop, like any length, is
                |     measured in millimeters.
                | 
                |     Example:
                |         This example sets the cropTop of the MyPicture drawing picture to 10
                |         mm
                | 
                |          MyPicture.cropTop = 10.

        :return: float
        """

        return self.com_object.cropTop

    @crop_top.setter
    def crop_top(self, value: float):
        """
        :param float value:
        """

        self.com_object.cropTop = value

    @property
    def format(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property format() As CatPictureFormat
                |     Sets the picture format.
                | 
                |     Parameters:
                | 
                |         iPictureFormat
                |             Compression format. 
                | 
                |     Returns:
                | 
                |         Legal values:
                | 
                |         S_OK
                |             Method correctly executed. 
                |         E_FAIL
                |             Method execution failed. 
                |             Reasons of the failure are not given. 
                |         E_IMPL
                |             No implementation available for this method. 
                | 
                |     See also:
                |         CatPictureFormat

        :return: int
        """

        return self.com_object.format

    @format.setter
    def format(self, value: int):
        """
        :param int value:
        """

        self.com_object.format = value

    @property
    def height(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property height() As double
                |     Returns or sets the height of the drawing picture. The height, like any
                |     length, is measured in millimeters.
                | 
                |     Example:
                |         This example gets the height of the MyPicture drawing
                |         picture
                | 
                |          Height = MyPicture.height

        :return: float
        """

        return self.com_object.height

    @height.setter
    def height(self, value: float):
        """
        :param float value:
        """

        self.com_object.height = value

    @property
    def ratio_lock(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ratioLock() As boolean
                |     Returns or sets the ratioLock of the drawing picture. The ratioLock is a
                |     boolean value If ratioLock is True it means that the size must not be changed
                |     by command in a interactive session.But it does not avoid size modifications
                |     thru VBscript exec (height and width still available for
                |     modification).
                | 
                |     Example:
                |         This example sets the ratioLock of the MyPicture drawing picture to
                |         True
                | 
                |          MyPicture.ratioLock = True

        :return: bool
        """

        return self.com_object.ratioLock

    @ratio_lock.setter
    def ratio_lock(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.ratioLock = value

    @property
    def width(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property width() As double
                |     Returns or sets the width of the drawing picture. The width, like any
                |     length, is measured in millimeters.
                | 
                |     Example:
                |         This example gets the width of the MyPicture drawing
                |         picture
                | 
                |          Width = MyPicture.width

        :return: float
        """

        return self.com_object.width

    @width.setter
    def width(self, value: float):
        """
        :param float value:
        """

        self.com_object.width = value

    @property
    def x(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property x() As double
                |     Returns or sets the x coordinate of the drawing picture position. It is
                |     expressed with respect to the view coordinate system. This coordinate, like any
                |     length, is measured in millimeters.
                | 
                |     Example:
                |         This example sets the x coordinate of the position of the MyPicture
                |         drawing picture to 5 inches. You need first to convert the 5 inches into
                |         millimeters.
                | 
                |          NewXCoordinate = 5*25.4
                |          MyPicture.x =  NewXCoordinate

        :return: float
        """

        return self.com_object.x

    @x.setter
    def x(self, value: float):
        """
        :param float value:
        """

        self.com_object.x = value

    @property
    def y(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property y() As double
                |     Returns or sets the y coordinate of the drawing picture position. It is
                |     expressed with respect to the view coordinate system. This coordinate, like any
                |     length, is measured in millimeters.
                | 
                |     Example:
                |         This example sets the y coordinate of the position of the MyPicture
                |         drawing picture to 5 inches. You need first to convert the 5 inches into
                |         millimeters.
                | 
                |          NewYCoordinate = 5*25.4
                |          MyPicture.y =  NewYCoordinate

        :return: float
        """

        return self.com_object.y

    @y.setter
    def y(self, value: float):
        """
        :param float value:
        """

        self.com_object.y = value

    def get_original_height(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Func GetOriginalHeight() As double
                |     Gets the original height of the drawing picture. The height, like any
                |     length, is measured in millimeters.
                | 
                |     Example:
                |         This example gets the original height of the MyPicture drawing
                |         picture
                | 
                |          Height = MyPicture.GetOriginalHeight()

        :return: float
        """
        return self.com_object.GetOriginalHeight()

    def get_original_width(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Func GetOriginalWidth() As double
                |     Gets the original width of the drawing picture. The width, like any length,
                |     is measured in millimeters.
                | 
                |     Example:
                |         This example gets the original width of the MyPicture drawing
                |         picture
                | 
                |          Width = MyPicture.GetOriginalWidth()

        :return: float
        """
        return self.com_object.GetOriginalWidth()

    def __repr__(self):
        return f'DrawingPicture(name="{ self.name }")'
