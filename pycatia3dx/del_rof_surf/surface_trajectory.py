"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class SurfaceTrajectory(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SurfaceTrajectory

    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def points_count(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property PointsCount() As short (Read Only)
                |     Gets the number of points in the trajectory
                | 
                |     Parameters:
                | 
                |         oCount
                |             Retrieves the number of points in the trajectory. 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure.

        :return: int
        """

        return self.com_object.PointsCount

    @property
    def sag(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Sag() As double
                |     Sets and retrieves the Sag value.
                | 
                |     Parameters:
                | 
                |         oSag
                |             The sag value. 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure.

        :return: float
        """

        return self.com_object.Sag

    @sag.setter
    def sag(self, value: float):
        """
        :param float value:
        """

        self.com_object.Sag = value

    @property
    def stroke_count(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property StrokeCount() As short (Read Only)
                |     Gets the number of strokes in the trajectory
                | 
                |     Parameters:
                | 
                |         oStrokes
                |             Retrieves the number of strokes in the trajectory.
                |             
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure.

        :return: int
        """

        return self.com_object.StrokeCount

    def get_approach_distance(self, i_app_retract: int, o_app_distance: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetApproachDistance(APPROACH_RETRACT iAppRetract,double
                | oAppDistance)
                |     Retrieves the approach distance.
                | 
                |     Parameters:
                | 
                |         iAppRetract
                |             Either UndefinedAppRet, First, Last, Retract, Approach, or
                |             ApproachRetract 
                |         oAppDistance
                |             The returned distance 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure.

        :param int i_app_retract:
        :param float o_app_distance:
        :return: None
        """
        return self.com_object.GetApproachDistance(i_app_retract, o_app_distance)

    def get_approach_transformations(self, o_transformations: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetApproachTransformations(CATSafeArrayVariant
                | oTransformations)
                |     Retrieves a list of the approach transformations
                | 
                |     Parameters:
                | 
                |         oTransformations
                |             List of approach transformations 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure.

        :param tuple o_transformations:
        :return: None
        """
        return self.com_object.GetApproachTransformations(o_transformations)

    def get_global_position(self, o_global_pos: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetGlobalPosition(CATSafeArrayVariant oGlobalPos)
                |     Retrieves the global position
                | 
                |     Parameters:
                | 
                |         oGlobalPos
                |             The global position 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure.

        :param tuple o_global_pos:
        :return: None
        """
        return self.com_object.GetGlobalPosition(o_global_pos)

    def get_retract_transformations(self, o_transformations: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetRetractTransformations(CATSafeArrayVariant
                | oTransformations)
                |     Retrieves a list of the retract transformations
                | 
                |     Parameters:
                | 
                |         oTransformations
                |             List of retract transformations 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure.

        :param tuple o_transformations:
        :return: None
        """
        return self.com_object.GetRetractTransformations(o_transformations)

    def get_sweep_direction(self, o_sweep_direction: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetSweepDirection(CATSafeArrayVariant oSweepDirection)
                |     Retrieves the Sweep Direction
                | 
                |     Parameters:
                | 
                |         oGlobalPos
                |             List of global positions 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure.

        :param tuple o_sweep_direction:
        :return: None
        """
        return self.com_object.GetSweepDirection(o_sweep_direction)

    def refresh_traj(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub RefreshTraj()
                |     Refreshes the trajectory.
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure.

        :return: None
        """
        return self.com_object.RefreshTraj()

    def resize_stroke(self, stroke_index: int, stroke_side: int, i_distance: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub ResizeStroke(short StrokeIndex,STROKE_SIDE StrokeSide,double
                | iDistance)
                |     Resizes a given stroke based on the index.
                | 
                |     Parameters:
                | 
                |         StrokeIndex
                |             The index of the stroke to modify. 
                |         StrokeSide
                |             The side of the stroke to modify. 
                |         iDistance
                |             The distance of the resized stroke. 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure.

        :param int stroke_index:
        :param int stroke_side:
        :param float i_distance:
        :return: None
        """
        return self.com_object.ResizeStroke(stroke_index, stroke_side, i_distance)

    def resize_trajectory(self, stroke_side: int, extent: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub ResizeTrajectory(STROKE_SIDE StrokeSide,double extent)
                |     Resizes a given stroke based on the index.
                | 
                |     Parameters:
                | 
                |         StrokeSide
                |             The side of the trajectory to modify. 
                |         extent
                |             The distance of the resized trajectory. 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure.

        :param int stroke_side:
        :param float extent:
        :return: None
        """
        return self.com_object.ResizeTrajectory(stroke_side, extent)

    def set_approach_distance(self, app_retract: int, i_distance: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetApproachDistance(APPROACH_RETRACT AppRetract,double
                | iDistance)
                |     Sets the approach distance.
                | 
                |     Parameters:
                | 
                |         AppRetract
                |             Either UndefinedAppRet, First, Last, Retract, Approach, or
                |             ApproachRetract 
                |         iDistance
                |             The distance to set the approach 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure.

        :param int app_retract:
        :param float i_distance:
        :return: None
        """
        return self.com_object.SetApproachDistance(app_retract, i_distance)

    def set_approach_transformations(self, i_transformations: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetApproachTransformations(CATSafeArrayVariant
                | iTransformations)
                |     Sets the approach transformations
                | 
                |     Parameters:
                | 
                |         iTransformations
                |             List of transformations 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure.

        :param tuple i_transformations:
        :return: None
        """
        return self.com_object.SetApproachTransformations(i_transformations)

    def set_global_position(self, i_global_pos: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetGlobalPosition(CATSafeArrayVariant iGlobalPos)
                |     Sets the global position
                | 
                |     Parameters:
                | 
                |         iGlobalPos
                |             The global position 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure.

        :param tuple i_global_pos:
        :return: None
        """
        return self.com_object.SetGlobalPosition(i_global_pos)

    def set_retract_transformations(self, i_transformations: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetRetractTransformations(CATSafeArrayVariant
                | iTransformations)
                |     Sets the retract transformations
                | 
                |     Parameters:
                | 
                |         iTransformations
                |             List of transformations 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure.

        :param tuple i_transformations:
        :return: None
        """
        return self.com_object.SetRetractTransformations(i_transformations)

    def set_sweep_direction(self, i_sweep_direction: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetSweepDirection(CATSafeArrayVariant iSweepDirection)
                |     Sets the Sweep Direction
                | 
                |     Parameters:
                | 
                |         iGlobalPos
                |             List of global positions 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure. 

        :param tuple i_sweep_direction:
        :return: None
        """
        return self.com_object.SetSweepDirection(i_sweep_direction)

    def __repr__(self):
        return f'SurfaceTrajectory(name="{ self.name }")'
