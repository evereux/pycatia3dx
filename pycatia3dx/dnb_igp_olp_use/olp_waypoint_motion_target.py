"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.dnb_igp_olp_use.olp_robot_motion_target import OLPRobotMotionTarget


class OLPWaypointMotionTarget(OLPRobotMotionTarget):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     DNBIgpOlpUseItf.OlpRobotMotionTarget
                |                         OlpWaypointMotionTarget
                | 
                | Interface representing a Waypoint Motion within a Waypoint
                | Operation.
                | This interface can only be used by a translator within the Robotics Off-line
                | Programming (OLP) Download or Upload command.
                | Role: Components that implement DELMIAOlpWaypointMotionTarget are
                | DELMIAOlpRobotMotionTargets that have a waypoint ID set
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def waypoint_escape_motion_type(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property WaypointEscapeMotionType() As CATBSTR
                |     Get/Set the waypoint escape motion type.
                |     The motion type constrains the direction of motion during a waypoint move.
                |     Valid values are X, Y, Z, XY, XZ, YZ, XYZ, Orient, X_Orient, Y_Orient,
                |     XY_Orient, Z_Orient, XZ_Orient, YZ_Orient, XYZ_Orient. Applies both to the
                |     waypoint motion and the drill/rivet action. 

        :return: str
        """

        return self.com_object.WaypointEscapeMotionType

    @waypoint_escape_motion_type.setter
    def waypoint_escape_motion_type(self, value: str):
        """
        :param str value:
        """

        self.com_object.WaypointEscapeMotionType = value

    def __repr__(self):
        return f'OLPWaypointMotionTarget(name="{ self.name }")'
