"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class FitTrackTPoint(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     FitTrackTPoint
                | 
                | Represents the FitTrackTPoint.
                | 
                | Role: FitTrackTPoint is an object that reprsents each Transient Anchor Point in
                | the Trajectory of a FitTrack.
    
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
                | Property Duration(double iDuration)
                |     Returns or sets the TPoint Duration.
                | 
                |     Example:
                | 
                |             This example first sets the TPoint duration to 5 and then returns
                |             it in TPointDur.
                |           
                | 
                |           Dim TPointDur As Double
                |           TPointDur = 5.0
                | 
                |           myFitTPoint.Duration = TPointDur
                |           TPointDur = myFitTPoint.Duration

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
    def position(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Position(CATSafeArrayVariant iMatrix)
                |     Returns or sets the TPoint Position.
                | 
                |     Example:
                | 
                |             This example first sets the TPoint Position and then returns it in
                |             TPointPos.
                |           
                | 
                |           Dim TPointPos(11)
                |           TPointPos(0) = 1
                |           TPointPos(1) = 0
                |           TPointPos(2) = 0
                |           TPointPos(3) = 0
                |           TPointPos(4) = 1
                |           TPointPos(5) = 0
                |           TPointPos(6) = 0
                |           TPointPos(7) = 0
                |           TPointPos(8) = 1
                |           TPointPos(9) = 100
                |           TPointPos(10) = 0
                |           TPointPos(11) = 0
                | 
                |           myFitTPoint.Position = TPointPos
                |           TPointPos = myFitTPoint.Position

        :return: tuple
        """

        return self.com_object.Position

    @position.setter
    def position(self, value: tuple):
        """
        :param tuple value:
        """

        self.com_object.Position = value

    def __repr__(self):
        return f'FitTrackTPoint(name="{ self.name }")'
