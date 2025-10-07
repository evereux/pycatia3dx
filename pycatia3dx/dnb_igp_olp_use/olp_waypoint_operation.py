"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.dnb_igp_olp_use.olp_instruction import OLPInstruction
from pycatia3dx.dnb_igp_olp_use.olp_instructions import OLPInstructions
from pycatia3dx.dnb_igp_olp_use.olp_procedure import OLPProcedure


class OLPWaypointOperation(OLPInstruction):

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
                |                         OlpWaypointOperation
                | 
                | An instruction that contains the path of waypoint motions.
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
                |     The list of instructions in the waypoint operation. All instructions must
                |     be waypoint motions.

        :return: OLPInstructions
        """

        return OLPInstructions(self.com_object.Instructions)

    @property
    def waypoint_task(self) -> OLPProcedure:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property WaypointTask() As OlpProcedure
                |     The waypoint task used for this waypoint operation. The same waypoint task
                |     must be used for all waypoint operations. This must be set during upload. It
                |     may not be available during download in the case of a template task being used.

        :return: OLPProcedure
        """

        return OLPProcedure(self.com_object.WaypointTask)

    @waypoint_task.setter
    def waypoint_task(self, value: OLPProcedure):
        """
        :param OLPProcedure value:
        """

        self.com_object.WaypointTask = value

    def __repr__(self):
        return f'OLPWaypointOperation(name="{ self.name }")'
