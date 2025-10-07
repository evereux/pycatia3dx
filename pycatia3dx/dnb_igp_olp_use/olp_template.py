"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.dnb_igp_olp_use.olp_instruction import OLPInstruction
from pycatia3dx.dnb_igp_olp_use.olp_instructions import OLPInstructions


class OLPTemplate(OLPInstruction):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     DNBIgpOlpUseItf.OlpInstruction
                |                         OlpTemplate
                | 
                | A template instruction.
                | 
                | This interface can only be used by a translator within the Robotics Off-line
                | Programming (OLP) Download or Upload command.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def instructions(self) -> OLPInstructions:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Instructions() As OlpInstructions (Read Only)
                |     Returns the list of instructions in the template.

        :return: OLPInstructions
        """

        return OLPInstructions(self.com_object.Instructions)

    @property
    def library_name(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property LibraryName() As CATBSTR (Read Only)
                |     Returns library name of the template.

        :return: str
        """

        return self.com_object.LibraryName

    @property
    def sub_type(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SubType() As CATBSTR (Read Only)
                |     Returns subtype of the template.

        :return: str
        """

        return self.com_object.SubType

    @property
    def template_name(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property TemplateName() As CATBSTR (Read Only)
                |     Returns name of the template.

        :return: str
        """

        return self.com_object.TemplateName

    @property
    def template_type(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property TemplateType() As CATBSTR (Read Only)
                |     Returns type of the template.

        :return: str
        """

        return self.com_object.TemplateType

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
                |     the OlpRobotMotionTarget or from the OlpTemplate that represents the action.

        :return: str
        """

        return self.com_object.WaypointID

    @waypoint_id.setter
    def waypoint_id(self, value: str):
        """
        :param str value:
        """

        self.com_object.WaypointID = value

    def __repr__(self):
        return f'OLPTemplate(name="{ self.name }")'
