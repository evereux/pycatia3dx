"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.system.cat_base_unknown import CATBaseUnknown
from pycatia3dx.del_curve_trajectory.curve_trajectory import CurveTrajectory


class CurveTrajectoryFactory(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     CurveTrajectoryFactory
                | 
                | Interface representing a Curve Trajectory factory to create and delete Curve
                | Trajectory.
                | 
                | Role: This interface is used to create and delete Curve
                | Trajectory.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def create_curve_trajectory(self, i_trajectory_type: int, i_name: str) -> CurveTrajectory:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CreateCurveTrajectory(DNBTrajectoryType iTrajectoryType,CATBSTR iName) As
                | CurveTrajectory
                |     This method creates a CurveTrajectory
                | 
                |     Parameters:
                | 
                |         iTrajectoryType,
                |             The trajectory type. The approved list of trajectory type are:
                |             Weld, Sealant, Adhesive, General 
                |         iName,
                |             Name of the Curve Trajectory to create. 
                | 
                |     Returns:
                |         The created Curve Trajectory. 
                |     Example:
                | 
                |          Dim objCurveTrajectoryFactory As
                |          CurveTrajectoryFactory
                |                ........
                |          Dim TrajectoryName As String
                |          TrajectoryName = "CurveTrajectory.VB"
                |          Dim objCurveTrajectory As CurveTrajectory
                |          Set objCurveTrajectory = objCurveTrajectoryFactory.CreateCurveTrajectory("Weld", TrajectoryName)

        :param int i_trajectory_type:
        :param str i_name:
        :return: CurveTrajectory
        """
        return CurveTrajectory(self.com_object.CreateCurveTrajectory(i_trajectory_type, i_name))

    def destroy_curve_trajectory(self, isp_curve_traj: CATBaseUnknown) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub DestroyCurveTrajectory(CATBaseUnknown ispCurveTraj)
                |     This method destroys a CurveTrajectory
                | 
                |     Parameters:
                | 
                |         ispCurveTraj
                |             CurveTrajectory to be deleted. 
                |         Example:
                | 
                |              Dim objCurveTrajectoryFactory As
                |              CurveTrajectoryFactory
                |              Dim objCurveTrajectory As CurveTrajectory
                |                    ........
                |              Call
objCurveTrajectoryFactory.DestroyCurveTrajectory(objCurveTrajectory)

        :param CATBaseUnknown isp_curve_traj:
        :return: None
        """
        return self.com_object.DestroyCurveTrajectory(isp_curve_traj.com_object)

    def set_generic_prefix(self, ib_generic: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetGenericPrefix(boolean ibGeneric)
                |     This method must be called prior to CreateCurveTrajectory to define the
                |     prefix used for the feature name.
                | 
                |     Parameters:
                | 
                |         ibGeneric,
                |             TRUE to define the prefix as "Arc". FALSE to define the prefix
                |             accordingly to the type. ex.: "Weld", "Sealant", "Adhesive" By default the
                |             value is FALSE. 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure. 

        :param bool ib_generic:
        :return: None
        """
        return self.com_object.SetGenericPrefix(ib_generic)

    def __repr__(self):
        return f'CurveTrajectoryFactory(name="{ self.name }")'
