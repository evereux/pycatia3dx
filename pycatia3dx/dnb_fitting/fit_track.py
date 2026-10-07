"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.dnb_fitting.fit_track_t_points import FitTrackTPoints
from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.types.general import CATVariant


class FitTrack(AnyObject):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     FitTrack
                | 
                | Represents the FitTrack.
                | 
                | Role: A FitTrack is an object that represents the trajectory in which an object
                | can be moved. The FitTrack object can be used to model the trajectory with
                | various properties and to add the objects to move. Once the Track properties
                | are set/modified, it is mandatory to call Refresh on the Track to update the
                | Track with properties.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def interpolater(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Interpolater(DNBInterpolater iInterpolater)
                |     Returns or sets the Track Interpolater Type.
                | 
                |     Example:
                | 
                |             This example first sets the track interpolation as Linear and then
                |             returns in trackInterpolater the Fitting Track interpolation
                |             type.
                |           
                | 
                |           Dim trackInterpolater As DNBInterpolater
                |           trackInterpolater = FitLINEAR
                |           myTrack.Interpolater = trackInterpolater
                |           trackInterpolater = myTrack.Interpolater

        :return: int
        """

        return self.com_object.Interpolater

    @interpolater.setter
    def interpolater(self, value: int):
        """
        :param int value:
        """

        self.com_object.Interpolater = value

    @property
    def mode(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Mode(DNBTrackMode iMode)
                |     Returns or sets the Track move Mode.
                | 
                |     Example:
                | 
                |             This example first sets the track mode as Time and then returns in
                |             trackMode the Fitting Track move mode.
                |           
                | 
                |           Dim trackMode As DNBTrackMode
                |           trackMode = FitTIME
                |           myTrack.Mode = trackMode
                |           trackMode = myTrack.Mode

        :return: int
        """

        return self.com_object.Mode

    @mode.setter
    def mode(self, value: int):
        """
        :param int value:
        """

        self.com_object.Mode = value

    @property
    def speed(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Speed(double iSpeed)
                |     Returns or sets the Track Speed.
                | 
                |     Example:
                | 
                |             This example first sets the track speed to 0.01 and then returns in
                |             trackSpeed the Fitting Track's speed.
                |           
                | 
                |           Dim trackSpeed As double
                |           trackSpeed = 0.01
                |           myTrack.Speed = trackSpeed
                |           trackSpeed = myTrack.Speed

        :return: float
        """

        return self.com_object.Speed

    @speed.setter
    def speed(self, value: float):
        """
        :param float value:
        """

        self.com_object.Speed = value

    @property
    def t_points(self) -> FitTrackTPoints:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property TPoints() As FitTrackTPoints (Read Only)
                |     Retrieves the collection object FitTrackTPoints.
                | 
                |     Example:
                | 
                |             This example retrieves the object FitTrackTPoints.
                |             
                | 
                |             Dim myTPoints As FitTrackTPoints 
                |             Set myTPoints = myTrack.TPoints

        :return: FitTrackTPoints
        """

        return FitTrackTPoints(self.com_object.TPoints)

    @property
    def total_time(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property TotalTime(double iTime)
                |     Returns or sets the Track Total Time.
                | 
                |     Example:
                | 
                |             This example first sets the track time to 10 and then returns in
                |             trackTime the Fitting Track's time.
                |           
                | 
                |           Dim trackTime As double
                |           trackTime = 10
                |           myTrack.TotalTime = trackTime
                |           trackTime = myTrack.TotalTime

        :return: float
        """

        return self.com_object.TotalTime

    @total_time.setter
    def total_time(self, value: float):
        """
        :param float value:
        """

        self.com_object.TotalTime = value

    def add_moving_object(self, i_moving_object: AnyObject, i_part_pos: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub AddMovingObject(CATBaseDispatch iMovingObject,CATSafeArrayVariant
                | iPartPos)
                |     Adds the object as moving object to the Track.
                |     Role: Adds a given object and moving object to this Track.
                | 
                |     Parameters:
                | 
                |         iMovingObject
                |             The moving object that is to be added as moving object for this
                |             Track. iMovingObject has to be an Occurrence correctly computed int he context
                |             of the Track. 
                |         iPartPos
                |             The Relative Position of the Added moving object with Anchor
                |             Position. 
                | 
                |     Example:
                | 
                |             This example adds the object as moved by myTrack
                |             Track.
                |             
                | 
                |             Dim movingObjOccurrence As CATBaseDispatch 
                |             Dim PartPos (11) As Double
                |             PartPos( 0) = 1.0
                |             PartPos( 1) = 0.0
                |             PartPos( 2) = 0.0
                |             PartPos( 3) = 0.0
                |             PartPos( 4) = 1.0
                |             PartPos( 5) = 0.0
                |             PartPos( 6) = 0.0
                |             PartPos( 7) = 0.0
                |             PartPos( 8) = 1.0
                |             PartPos( 9) = 100.0
                |             PartPos(10) = 100.0
                |             PartPos(11) = 100.0
                |             myTrack.AddMovingObject movingObjOccurrence,
                |             PartPos

        :param AnyObject i_moving_object:
        :param tuple i_part_pos:
        :return: None
        """
        return self.com_object.AddMovingObject(i_moving_object.com_object, i_part_pos)

    def get_anchor_position(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2026-02-08 14:05:01.675948))
                | Sub GetAnchorPosition(CATSafeArrayVariant iComponents)
                |     Retrieves the Anchor Position of the Track.
                |     Role: Retrieves the Anchor Position of the Track with respect to the
                |     absolute coordinate system.
                |
                |     Parameters:
                |
                |         iComponents
                |             The position of the Anchor Position with respect to the absolute
                |             coordinate system.
                |
                |                 iComponents( 0) is the X component of the
                |                 X-axis
                |                 iComponents( 1) is the Y component of the
                |                 X-axis
                |                 iComponents( 2) is the Z component of the
                |                 X-axis
                |                 iComponents( 3) is the X component of the
                |                 Y-axis
                |                 iComponents( 4) is the Y component of the
                |                 Y-axis
                |                 iComponents( 5) is the Z component of the
                |                 Y-axis
                |                 iComponents( 6) is the X component of the
                |                 Z-axis
                |                 iComponents( 7) is the Y component of the
                |                 Z-axis
                |                 iComponents( 8) is the Z component of the
                |                 Z-axis
                |                 iComponents( 9) is the X component of the
                |                 origin
                |                 iComponents(10) is the Y component of the
                |                 origin
                |                 iComponents(11) is the Z component of the origin
                |
                |
                |     Example:
                |
                |             This example gets the Anchor Position in anchorPos of myTrack
                |             Track.
                |
                |
                |             Dim anchorPos(11) As Double
                |             myTrack.GetAnchorPosition anchorPos

        :return: tuple
        """
        return self.com_object.GetAnchorPosition()
        # todo: check this method, does it require system service?
        # Autogenerated comment:
        # some methods require a system service call as the methods expects a vb array object
        # passed to it and there is no way to do this directly with python. In those cases the following code
        # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # vba_function_name = 'get_anchor_position'
        # vba_code = """
        # Public Function get_anchor_position(fit_track)
        #     Dim iComponents (2)
        #     fit_track.GetAnchorPosition iComponents
        #     get_anchor_position = iComponents
        # End Function
        # """

        # system_service = SystemService(self.application.SystemService)
        # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_moving_objects(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2026-02-08 14:05:01.675948))
                | Sub GetMovingObjects(CATSafeArrayVariant iMovingObjects)
                |     Retrieves the objects moved by the Track.
                |
                |     Parameters:
                |
                |         iMovingObjects
                |             The moving objects of this Track. The objects returned are the
                |             Occurrences of Objects.
                |
                |     Example:
                |
                |             This example gets the objects moved by myTrack
                |             Track.
                |
                |
                |             ReDim MovingObjects(nbMovingObjects)
                |             myTrack.GetMovingObjects  MovingObjects

        :return: tuple
        """
        return self.com_object.GetMovingObjects()
        # todo: check this method, does it require system service?
        # Autogenerated comment:
        # some methods require a system service call as the methods expects a vb array object
        # passed to it and there is no way to do this directly with python. In those cases the following code
        # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # vba_function_name = 'get_moving_objects'
        # vba_code = """
        # Public Function get_moving_objects(fit_track)
        #     Dim iMovingObjects (2)
        #     fit_track.GetMovingObjects iMovingObjects
        #     get_moving_objects = iMovingObjects
        # End Function
        # """

        # system_service = SystemService(self.application.SystemService)
        # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_number_moving_objects(self, i_num_objects: CATVariant) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetNumberMovingObjects(CATVariant iNumObjects)
                |     Retrieves the number of objects moved by the Track.
                | 
                |     Parameters:
                | 
                |         iNumTPoints
                |             The number of moving objects of this Track. 
                | 
                |     Example:
                | 
                |             This example gets the number of objects moved by myTrack
                |             Track.
                |             
                | 
                |             Dim nbMovingObjects
                |             myTrack.GetNumberMovingObjects nbMovingObjects

        :param CATVariant i_num_objects:
        :return: None
        """
        return self.com_object.GetNumberMovingObjects(i_num_objects)

    def get_number_of_t_points(self, i_num_t_points: CATVariant) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetNumberOfTPoints(CATVariant iNumTPoints)
                |     Retrieves the number of TPoints of the Track.
                | 
                |     Parameters:
                | 
                |         iNumTPoints
                |             The number of TPoints this Track contains 
                | 
                |     Example:
                | 
                |             This example gets the number of TPoints of myTrack
                |             Track.
                |             
                | 
                |             Dim nbTPoints
                |             myTrack.GetNumberOfTPoints nbTPoints

        :param CATVariant i_num_t_points:
        :return: None
        """
        return self.com_object.GetNumberOfTPoints(i_num_t_points)

    def get_part_relative_position(self, i_moving_object: AnyObject) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetPartRelativePosition(CATBaseDispatch iMovingObject) As
                | CATSafeArrayVariant
                |     Retrieves the offset of the object with Anchor Position.
                | 
                |     Parameters:
                | 
                |         iMovingObject
                |             The moving object for which the offset is computed. iMovingObject
                |             has to be an Occurrence correctly computed int he context of the Track.
                |             
                | 
                |     Returns:
                |         oPartOffset The returned Part Relative Position. 
                |     Example:
                | 
                |             This example gets the offset of the object with the Anchor
                |             Position.
                |             
                | 
                |             Dim movingObjOccurrence As CATBaseDispatch 
                |             Dim PartOffset(11) as Double
                |             Set PartOffset = myTrack.GetPartRelativePosition movingObjOccurrence

        :param AnyObject i_moving_object:
        :return: tuple
        """
        return self.com_object.GetPartRelativePosition(i_moving_object.com_object)

    def refresh(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Refresh()
                |     Updates the Track properties and visualization
                | 
                |     Example:
                | 
                |             This example Updates the Track.
                |             
                | 
                |             myTrack.Refresh

        :return: None
        """
        return self.com_object.Refresh()

    def remove_moving_object(self, i_moving_object: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub RemoveMovingObject(CATBaseDispatch iMovingObject)
                |     Removes the object as moving object from the Track.
                | 
                |     Parameters:
                | 
                |         iMovingObject
                |             The moving object that is to be removed as moving object for this
                |             Track. iMovingObject has to be an Occurrence correctly computed int he context
                |             of the Track. 
                | 
                |     Example:
                | 
                |             This example removes the object as moved by myTrack
                |             Track.
                |             
                | 
                |             Dim movingObjOccurrence As CATBaseDispatch 
                |             myTrack.RemoveMovingObject movingObjOccurrence

        :param AnyObject i_moving_object:
        :return: None
        """
        return self.com_object.RemoveMovingObject(i_moving_object.com_object)

    def set_anchor_position(self, i_components: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2026-02-08 14:05:01.675948))
                | Sub SetAnchorPosition(CATSafeArrayVariant iComponents)
                |     Sets the Anchor Position of the Track.
                |     Role: Sets the Anchor Position of the Track with respect to the absolute
                |     coordinate system.
                |
                |     Parameters:
                |
                |         iComponents
                |             The position of the Anchor Position with respect to the absolute
                |             coordinate system
                |
                |                 iComponents( 0) is the X component of the
                |                 X-axis
                |                 iComponents( 1) is the Y component of the
                |                 X-axis
                |                 iComponents( 2) is the Z component of the
                |                 X-axis
                |                 iComponents( 3) is the X component of the
                |                 Y-axis
                |                 iComponents( 4) is the Y component of the
                |                 Y-axis
                |                 iComponents( 5) is the Z component of the
                |                 Y-axis
                |                 iComponents( 6) is the X component of the
                |                 Z-axis
                |                 iComponents( 7) is the Y component of the
                |                 Z-axis
                |                 iComponents( 8) is the Z component of the
                |                 Z-axis
                |                 iComponents( 9) is the X component of the
                |                 origin
                |                 iComponents(10) is the Y component of the
                |                 origin
                |                 iComponents(11) is the Z component of the origin
                |
                |
                |     Example:
                |
                |             This example sets the Anchor Position of myTrack
                |             Track.
                |
                |
                |             Dim anchorPos(11) As Double
                |             anchorPos( 0) = 1.0
                |             anchorPos( 1) = 0.0
                |             anchorPos( 2) = 0.0
                |             anchorPos( 3) = 0.0
                |             anchorPos( 4) = 1.0
                |             anchorPos( 5) = 0.0
                |             anchorPos( 6) = 0.0
                |             anchorPos( 7) = 0.0
                |             anchorPos( 8) = 1.0
                |             anchorPos( 9) = 100.0
                |             anchorPos(10) = 0.0
                |             anchorPos(11) = 0.0
                |             myTrack.SetAnchorPosition anchorPos

        :param tuple i_components:
        :return: None
        """
        return self.com_object.SetAnchorPosition(i_components)
        # todo: check this method, does it require system service?
        # Autogenerated comment:
        # some methods require a system service call as the methods expects a vb array object
        # passed to it and there is no way to do this directly with python. In those cases the following code
        # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # vba_function_name = 'set_anchor_position'
        # vba_code = """
        # Public Function set_anchor_position(fit_track)
        #     Dim iComponents (2)
        #     fit_track.SetAnchorPosition iComponents
        #     set_anchor_position = iComponents
        # End Function
        # """

        # system_service = SystemService(self.application.SystemService)
        # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_part_relative_position(self, i_moving_object: AnyObject, i_part_offset: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetPartRelativePosition(CATBaseDispatch iMovingObject,CATSafeArrayVariant
                | iPartOffset)
                |     Sets the offset of the object with Anchor Position.
                | 
                |     Parameters:
                | 
                |         iMovingObject
                |             The moving object for which the offset is to be set. iMovingObject
                |             has to be an Occurrence correctly computed int he context of the Track.
                |             
                | 
                |     Example:
                | 
                |             This example sets the offset of the object with the Anchor
                |             Position.
                |             
                | 
                |             Dim movingObjOccurrence As CATBaseDispatch 
                |             Dim PartOffset(11) as Double
                |             PartOffset( 0) = 1.0
                |             PartOffset( 1) = 0.0
                |             PartOffset( 2) = 0.0
                |             PartOffset( 3) = 0.0
                |             PartOffset( 4) = 1.0
                |             PartOffset( 5) = 0.0
                |             PartOffset( 6) = 0.0
                |             PartOffset( 7) = 0.0
                |             PartOffset( 8) = 1.0
                |             PartOffset( 9) = 100.0
                |             PartOffset(10) = 100.0
                |             PartOffset(11) = 100.0
                |             myTrack.SetPartRelativePosition movingObjOccurrence,
                |             PartOffset

        :param AnyObject i_moving_object:
        :param tuple i_part_offset:
        :return: None
        """
        return self.com_object.SetPartRelativePosition(i_moving_object.com_object, i_part_offset)

    def __repr__(self):
        return f'FitTrack(name="{self.name}")'
