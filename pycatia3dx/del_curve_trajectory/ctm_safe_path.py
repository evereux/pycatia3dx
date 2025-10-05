"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class CtmSafePath(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     CtmSafePath
                | 
                | Interface representing a Path.
                | 
                | Role: This interface is used to see if a path is an Approach or
                | Departure.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def is_approach(self, o_approach: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub IsApproach(boolean oApproach)
                |     Validates type of safe path
                | 
                |     Parameters:
                | 
                |         oApproach
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure.
                |         Legal values:
                | 
                |         TRUE
                |             The safe path is an approach path.
                |         FALSE
                |             The safe path is not an approach path.
                | 
                |     Example:
                | 
                |          Dim oCurveTrajectory As CurveTrajectory
                |                ........
                |          Dim oApproach
                |          Call oCurveTrajectory.GetApproach(oApproach)
                |          If oApproach Is Nothing Then
                |          Call oCurveTrajectory.CreateApproach(oApproach)
                |          End If
                |          Dim oPath As CtmSafePath
                |          Set oPath = oApproach
                |          Dim oBool As Boolean
                |          Call oPath.IsApproach(oBool)

        :param bool o_approach:
        :return: None
        """
        return self.com_object.IsApproach(o_approach)

    def is_departure(self, o_depart: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub IsDeparture(boolean oDepart)
                |     Validates type of safe path
                | 
                |     Parameters:
                | 
                |         oDepart
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure.
                |         Legal values:
                | 
                |         TRUE
                |             The safe path is an departure path.
                |         FALSE
                |             The safe path is not a departure path.
                | 
                |     Example:
                | 
                |          Dim oCurveTrajectory As CurveTrajectory
                |                ........
                |          Dim oApproach
                |          Call oCurveTrajectory.GetApproach(oApproach)
                |          If oApproach Is Nothing Then
                |          Call oCurveTrajectory.CreateApproach(oApproach)
                |          End If
                |          Dim oPath As CtmSafePath
                |          Set oPath = oApproach
                |          Dim oBool As Boolean
                |          Call oPath.IsDeparture(oBool)

        :param bool o_depart:
        :return: None
        """
        return self.com_object.IsDeparture(o_depart)

    def __repr__(self):
        return f'CtmSafePath(name="{ self.name }")'
