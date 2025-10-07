"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class OLPDrillRivetAction(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     OlpDrillRivetAction
                | 
                | A Drill and Rivet Action Instruction.
                | 
                | This interface can only be used by a translator within the Robotics Off-line
                | Programming (OLP) Download or Upload command.
                | 
                | Drill and Rivet Actions are treated as a template instruction. They contain one
                | or more instructions and by default a new drill rivet action contains both a
                | drill operation and rivet operation.
                | 
                | During download, you can identify a drill rivet action because the instruction
                | type will be delOlpTemplate. A drill rivet action has the following template
                | property values:
                | OlpTemplate.LibraryName = "DrillRivet"
                | OlpTemplate.TemplateType = "DrillRivetAction"
                | OlpTemplate.TemplateName = "DrillRivetAction"
                | OlpTemplate.TemplateType = "Spot"
                | OlpTemplate.TemplateType = "Action"
                | 
                | You create a drill rivet action during upload using the
                | OlpInstructions.CreateInstructionFromTemplate method with the attributes listed
                | above.
                | 
                | Example: (VB.NET)
                | 
                |  Dim Task As OlpProcedure
                |  Dim Instructions As OlpInstructions = Task.Instructions
                |  Dim Action As OlpDrillRivetAction = Instructions.CreateInstructionFromTemplate("DrillRivet", "DrillRivetAction", "Spot", "Action", Nothing, True)
    
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

    @property
    def waypoint_escape_zone(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property WaypointEscapeZone() As CATBSTR

        :return: str
        """

        return self.com_object.WaypointEscapeZone

    @waypoint_escape_zone.setter
    def waypoint_escape_zone(self, value: str):
        """
        :param str value:
        """

        self.com_object.WaypointEscapeZone = value

    @property
    def waypoint_id(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property WaypointID() As CATBSTR
                |     Get/Set the waypoint ID.
                |     The waypoint ID is defined on waypoint motions and also on motions that
                |     declare the closest waypoint. For actions, the WaypointID can be retrieved from
                |     the target or from the OlpTemplate that represents the action.

        :return: str
        """

        return self.com_object.WaypointID

    @waypoint_id.setter
    def waypoint_id(self, value: str):
        """
        :param str value:
        """

        self.com_object.WaypointID = value

    @property
    def waypoint_safe_zone(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property WaypointSafeZone() As CATBSTR
                |     Get / Set the waypoint safe zone for a drill / rivet
                |     action.

        :return: str
        """

        return self.com_object.WaypointSafeZone

    @waypoint_safe_zone.setter
    def waypoint_safe_zone(self, value: str):
        """
        :param str value:
        """

        self.com_object.WaypointSafeZone = value

    def __repr__(self):
        return f'OLPDrillRivetAction(name="{ self.name }")'
