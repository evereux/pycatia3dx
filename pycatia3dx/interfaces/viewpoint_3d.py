"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-13 15:35:27.265802

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class ViewPoint3D(AnyObject):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     Viewpoint3D
                | 
                | Represents the 3D viewpoint.
                | The 3D viewpoint is the object that stores data which defines how your objects
                | are seen to enable their display by a 3D viewer. This data includes namely the
                | eye location, also named the origin, the distance from the eye to the target,
                | that is to the looked at point in the scene, the sight, up, and right
                | directions, defining a 3D axis system with the eye location as origin, the
                | projection type chosen among perspective (conic) and parallel (cylindric), and
                | the zoom factor. The right direction is not exposed in a property, and is
                | automatically computed from the sight and up directions.
                | 
                | See also:
                |     CatProjectionMode
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def field_of_view(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Property FieldOfView() As double
                |     Returns or sets the field of view associated with the viewpoint. The field
                |     of view is half of the vertical angle of the viewpoint, expressed in degrees.
                |     This property exists with the perspective (conic) projection type
                |     only.
                | 
                |     Example:
                |         This example retrieves in HalfAngle the field of view associated with
                |         the NiceViewpoint viewpoint.
                | 
                |          HalfAngle = NiceViewpoint.FieldOfView

        :return: float
        """

        return self.com_object.FieldOfView

    @field_of_view.setter
    def field_of_view(self, value: float):
        """
        :param float value:
        """

        self.com_object.FieldOfView = value

    @property
    def focus_distance(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Property FocusDistance() As double
                |     Returns or sets the focus distance of the viewpoint. The focus distance
                |     determines the target position, that is the point at which the eye located at
                |     the origin and looking towards the sight direction is looking at. It is
                |     expressed in model units.
                | 
                |     Example:
                |         This example sets the focus distance of the NiceViewpoint viewpoint to
                |         10.
                | 
                |          NiceViewpoint.FocusDistance = 10

        :return: float
        """

        return self.com_object.FocusDistance

    @focus_distance.setter
    def focus_distance(self, value: float):
        """
        :param float value:
        """

        self.com_object.FocusDistance = value

    @property
    def projection_mode(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Property ProjectionMode() As CatProjectionMode
                |     Returns or sets the projection mode.
                | 
                |     Example:
                |         This example sets the projection mode for the My3DViewer 3D viewer to
                |         catProjectionConic.
                | 
                |          My3DViewer.Viewpoint3D.NavigationStyle = catProjectionConic

        :return: int
        """

        return self.com_object.ProjectionMode

    @projection_mode.setter
    def projection_mode(self, value: int):
        """
        :param int value:
        """

        self.com_object.ProjectionMode = value

    @property
    def zoom(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Property Zoom() As double
                |     Returns or sets the zoom factor associated with the viewpoint. This
                |     property exists with the parallel (cylindric) projection type
                |     only.
                | 
                |     Example:
                |         This example retrieves in ZoomFactor the zoom factor associated with
                |         the NiceViewpoint viewpoint, tests if it is greater than 2, and if so, sets it
                |         to one and applies it.
                | 
                |          ZoomFactor = NiceViewpoint.Zoom
                |          If ZoomFactor > 2 Then
                |           ZoomFactor = 1
                |           NiceViewpoint.Zoom(ZoomFactor)
                |          End If

        :return: float
        """

        return self.com_object.Zoom

    @zoom.setter
    def zoom(self, value: float):
        """
        :param float value:
        """

        self.com_object.Zoom = value

    def get_origin(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Sub GetOrigin(CATSafeArrayVariant origin)
                |     Retrieves the coordinates of the origin of the viewpoint. These coordinates
                |     are returned as an array of 3 Variants (double type).
                | 
                |     Example:
                |         This example retrieves the origin of the NiceViewpoint viewpoint in the
                |         origin variable.
                | 
                |          Dim origin(2)
                |          NiceViewpoint.GetOrigin origin

        :return: tuple
        """
        # todo: check this method, does it require system service?
        return self.com_object.GetOrigin()
        # # # # Autogenerated comment:
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise, completely remove all this.
        # # vba_function_name = 'get_origin'
        # # vba_code = """
        # # Public Function get_origin(viewpoint3_d)
        # #     Dim origin (2)
        # #     viewpoint3_d.GetOrigin origin
        # #     get_origin = origin
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_sight_direction(self, o_sight: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Sub GetSightDirection(CATSafeArrayVariant oSight)
                |     Gets the components of the sight direction of the viewpoint. The sight
                |     direction is the line passes both by the origin of the viewpoint and by the
                |     target.
                | 
                |     Example:
                |         This example gets the sight direction of the
                |         NiceViewpoint
                | 
                |          Dim sight(2)
                |          NiceViewpoint.GetSightDirection sight

        :param tuple o_sight:
        :return: None
        """
        return self.com_object.GetSightDirection(o_sight)

    def get_up_direction(self, o_up: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Sub GetUpDirection(CATSafeArrayVariant oUp)
                |     Gets the components of the up direction of the viewpoint.
                | 
                |     Example:
                |         This example gets the up direction of the
                |         NiceViewpoint.
                | 
                |          Dim up(2)
                |          NiceViewpoint.GetUpDirection up

        :param tuple o_up:
        :return: None
        """
        return self.com_object.GetUpDirection(o_up)

    def put_origin(self, origin: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Sub PutOrigin(CATSafeArrayVariant origin)
                |     Sets the coordinates of the origin of the viewpoint. These coordinates are
                |     set as an array of 3 Variants (double type).
                | 
                |     Example:
                |         This example sets the origin of the NiceViewpoint viewpoint. to the
                |         point with coordinates (10, 25, 15).
                | 
                |          NiceViewpoint.PutOrigin Array(10, 25, 15)

        :param tuple origin:
        :return: None
        """
        return self.com_object.PutOrigin(origin)

    def put_sight_direction(self, o_sight: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Sub PutSightDirection(CATSafeArrayVariant oSight)
                |     Sets the components of the sight direction of the viewpoint. The sight
                |     direction is the line passes both by the origin of the viewpoint and by the
                |     target.
                | 
                |     Example:
                |         This example sets the sight direction of the NiceViewpoint viewpoint to
                |         the direction with components (1.414, 1.414, 0).
                | 
                |          NiceViewpoint.PutSightDirection Array(1.414, 1.414,
                |          0)

        :param tuple o_sight:
        :return: None
        """
        return self.com_object.PutSightDirection(o_sight)

    def put_up_direction(self, o_up: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Sub PutUpDirection(CATSafeArrayVariant oUp)
                |     Sets the components of the up direction of the viewpoint.
                | 
                |     Example:
                |         This example sets the up direction of the NiceViewpoint viewpoint to
                |         the direction with components (0, 0, 1).
                | 
                |          NiceViewpoint.PutUpDirection Array(0, 0, 1)

        :param tuple o_up:
        :return: None
        """
        return self.com_object.PutUpDirection(o_up)

    def __repr__(self):
        return f'Viewpoint3D(name="{self.name}")'
