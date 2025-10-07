"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.collection import Collection
from pycatia3dx.dnb_fitting.fit_track_t_point import FitTrackTPoint
from pycatia3dx.types.general import CATVariant


class FitTrackTPoints(Collection):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     FitTrackTPoints
                | 
                | Represents a collection FitTrackTPoints.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def insert_t_point(self, i_index: CATVariant, i_t_point_pos: tuple, i_t_point_compass_trans: tuple, i_duration: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub InsertTPoint(CATVariant iIndex,CATSafeArrayVariant
                | iTPointPos,CATSafeArrayVariant iTPointCompassTrans,double
                | iDuration)
                |     Inserts a new TPoint at a given Index.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             Index at which the TPoint is to be inserted. Index starts from 1.
                |             
                |         iTPointPos
                |             The Relative Position of the TPoint to be inserted with Anchor
                |             Position. 
                |         iTPointCompassTrans
                |             The Offset of the Compass with iTPointPos. 
                |         iDuration
                |             Duration of the inserted TPoint. 
                | 
                |     Example:
                | 
                |             This example inserts a new TPoint at the index 2 with duration
                |             5.
                |             
                | 
                |             Dim TPointPos(11) As Double
                |             TPointPos( 0) = 1.0
                |             TPointPos( 1) = 0.0
                |             TPointPos( 2) = 0.0
                |             TPointPos( 3) = 0.0
                |             TPointPos( 4) = 1.0
                |             TPointPos( 5) = 0.0
                |             TPointPos( 6) = 0.0
                |             TPointPos( 7) = 0.0
                |             TPointPos( 8) = 1.0
                |             TPointPos( 9) = 100.0
                |             TPointPos(10) = 100.0
                |             TPointPos(11) = 100.0
                |             myTPoints.InsertTPoint 2, TPointPos, 5

        :param CATVariant i_index:
        :param tuple i_t_point_pos:
        :param tuple i_t_point_compass_trans:
        :param float i_duration:
        :return: None
        """
        return self.com_object.InsertTPoint(i_index, i_t_point_pos, i_t_point_compass_trans, i_duration)

    def item(self, i_index: CATVariant) -> FitTrackTPoint:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Item(CATVariant iIndex) As FitTrackTPoint
                |     Returns a TPoint at a given Index.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             Index for which the TPoint is retrieved.
                | 
                |     Returns:
                |         oTPoint The returned FitTrackTPoint. 
                |     Example:
                | 
                |             This example retrieves the TPoint at the index 2.
                |             
                | 
                |             Dim myTPoint As FitTrackTPoint
                |             Set myTPoint = myTPoints.Item 2

        :param CATVariant i_index:
        :return: FitTrackTPoint
        """
        return FitTrackTPoint(self.com_object.Item(i_index))

    def remove_t_point(self, i_index: CATVariant) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub RemoveTPoint(CATVariant iIndex)
                |     Removes a new TPoint at a given Index.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             Index at which the TPoint is to be removed. 
                | 
                |     Example:
                | 
                |             This example removes a TPoint at the index 2.
                |             
                | 
                |             myTPoints.RemoveTPoint 2

        :param CATVariant i_index:
        :return: None
        """
        return self.com_object.RemoveTPoint(i_index)

    def __repr__(self):
        return f'FitTrackTPoints(name="{ self.name }")'
