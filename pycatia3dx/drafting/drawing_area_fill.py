"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class DrawingAreaFill(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     DrawingAreaFill
                | 
                | Represents a drawing area fill in a drawing view.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def area_fill_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property AreaFillType() As CatAreaFillType (Read Only)
                |     Returns area fill type.
                | 
                |     Example:
                |         This example sets the anchor position of the MyText drawing text to top
                |         left position.
                | 
                |          MyText.AnchorPosition = TopLeft

        :return: int
        """

        return self.com_object.AreaFillType

    @property
    def display_at_true_depth(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property DisplayAtTrueDepth() As boolean
                |     Checks if the Area Fill has its "Display at true depth" property valued to
                |     True or False. Sets the "Display at true depth" property value to True or
                |     False. Role: The modification of this property to true does not necessarily
                |     means that the Area Fill will be "Displayed at true depth". The value is
                |     ignored if the Area Fill is created in a main view, a backgound view, in a 2D
                |     component reference, in drafting. However it can be usefull to modify its value
                |     in case of copy and paste in a 2DLayout view, in a 2D component reference for
                |     an instanciation in a 2DLayout view.
                | 
                |     Example:
                |         This example sets the display at true depth of the myAreaFill Area Fill
                |         to True
                | 
                |          myAreaFill.DisplayAtTrueDepth = True

        :return: bool
        """

        return self.com_object.DisplayAtTrueDepth

    @display_at_true_depth.setter
    def display_at_true_depth(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.DisplayAtTrueDepth = value

    def get_characteristics(self, o_number_of_contour: int, o_number_of_points: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub GetCharacteristics(long oNumberOfContour,long
                | oNumberOfPoints)
                |     Gets the number of contours and the number of points (external and
                |     internals contours) of a drawing area fill. This method can be used before
                |     calling GetPoints
                | 
                |     Parameters:
                | 
                |         oNumberOfContour
                |             Number of contours 
                |         oNumberOfPoints
                |             Number of points 
                |         Example:
                |             This example gets profil infomation of myAreaFill.
                | 
                |              Dim numberOfContours As Long
                |              Dim numberOfPoints As Long
                |              myAreaFill.GetCharacteristics numberOfContours,
                |              numberOfPoints

        :param int o_number_of_contour:
        :param int o_number_of_points:
        :return: None
        """
        return self.com_object.GetCharacteristics(o_number_of_contour, o_number_of_points)

    def get_points(self, o_number_of_points_per_contour: tuple, o_points_coordinates: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub GetPoints(CATSafeArrayVariant oNumberOfPointsPerContour,CATSafeArrayVariant
                | oPointsCoordinates)
                |     Get points coordinates of external and internal contours of area fill. This
                |     method can be used for isolated or not drawing area fills
                | 
                |     Parameters:
                | 
                |         oNumberOfPointsPerContour
                |             Number of points per contour 
                |         oPointsCoordinates
                |             External and internal points coordinates of drawing area fill
                |             
                |         Example:
                |             This example gets geometrical infomation of
                |             myAreaFill.
                | 
                |              Dim numberOfContours As Long
                |              Dim numberOfPoints As Long
                |              Dim NumberOfPtsPerContour() as Variant
                |              Dim PtsCoordinates() as Variant
                |              myAreaFill.GetCharacteristics numberOfContours,
                |              numberOfPoints
                |              Redim NumberOfPtsPerContour(numberOfContours)
                |              Redim PtsCoordinates(2*numberOfPoints)
                |              myAreaFill.GetPoints NumberOfPtsPerContour,
                |              PtsCoordinates

        :param tuple o_number_of_points_per_contour:
        :param tuple o_points_coordinates:
        :return: None
        """
        return self.com_object.GetPoints(o_number_of_points_per_contour, o_points_coordinates)

    def isolate(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub Isolate()
                |     Isolates a drawing area fill from its geometry. 
                | Example:
                |     This example isolates myAreaFill from its geometry.
                | 
                |      myAreaFill.Isolate

        :return: None
        """
        return self.com_object.Isolate()

    def modify_points(self, i_number_of_points_per_contour: tuple, i_points_coordinates: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub ModifyPoints(CATSafeArrayVariant
                | iNumberOfPointsPerContour,CATSafeArrayVariant
                | iPointsCoordinates)
                |     Set points coordinates of external and internal contours of area fill. This
                |     method can be used for isolated or not drawing area fills. If drawing area fill
                |     points curves, it is turned into a drawing area fill on
                |     points.
                | 
                |     Parameters:
                | 
                |         iNumberOfPointsPerContour
                |             Number of points per contour 
                |         iPointsCoordinates
                |             External and internal points coordinates of drawing area fill
                |             
                |         Example:
                |             This example sets geometrical infomation of
                |             myAreaFill.
                | 
                |              NumberOfPtsPerContour = Array(4, 3)
                |              PtsCoordinates  = Array(10., 10., 50., 10., 50., 50., 10., 50., 20., 20., 40., 20., 30., 40.)
                |              myAreaFill.ModifyPointsNumberOfPtsPerContour,
                |              PtsCoordinates

        :param tuple i_number_of_points_per_contour:
        :param tuple i_points_coordinates:
        :return: None
        """
        return self.com_object.ModifyPoints(i_number_of_points_per_contour, i_points_coordinates)

    def set_pattern(self, i_pattern_name_from_standard: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub SetPattern(CATBSTR iPatternNameFromStandard)
                |     Sets a pattern from its name on an area fill. Pattern name must exist on
                |     document area fill belong to.
                | 
                |     Parameters:
                | 
                |         iPatternNameFromStandard
                |             Pattern name to retrieve from embedded standard 
                |         Example:
                |             This example sets a pattern on myAreaFill. Pattern names can be
                |             retrieved in "Tools/Standards..." command under "Patterns" node of drafting
                |             standards.
                | 
                |              myAreaFill.SetPattern "alu 30"

        :param str i_pattern_name_from_standard:
        :return: None
        """
        return self.com_object.SetPattern(i_pattern_name_from_standard)

    def __repr__(self):
        return f'DrawingAreaFill(name="{ self.name }")'
