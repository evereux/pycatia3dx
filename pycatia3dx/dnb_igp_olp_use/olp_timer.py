"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.dnb_igp_olp_use.olp_ast_branch import OLPAstBranch
from pycatia3dx.dnb_igp_olp_use.olp_instruction import OLPInstruction
from pycatia3dx.dnb_igp_olp_use.olp_variable import OLPVariable


class OLPTimer(OLPInstruction):

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
                |                         OlpTimer
                | 
                | An instruction to start, stop or reset a timer.
                | 
                | This interface can only be used by a translator within the Robotics Off-line
                | Programming (OLP) Download or Upload command.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def action(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Action() As DELOlpTimerAction
                |     The action to perform on the timer.

        :return: DELOlpTimerAction
        """

        return self.com_object.Action

    @action.setter
    def action(self, value: int):
        """
        :param int value:
        """

        self.com_object.Action = value

    @property
    def destination(self) -> OLPVariable:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Destination() As OlpVariable
                |     The timer which is being started, stopped or reset.
                |     You can retrieve an existing timer using OlpInstruction.FindVariable or
                |     create a new one using OlpVariables. The variable assigned, must be of type
                |     timer.

        :return: OLPVariable
        """

        return OLPVariable(self.com_object.Destination)

    @destination.setter
    def destination(self, value: OLPVariable):
        """
        :param OLPVariable value:
        """

        self.com_object.Destination = value

    @property
    def destination_express(self) -> OLPAstBranch:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property DestinationExpress() As OlpAstBranch
                |     The variable which is being assigned as an expression.

        :return: OLPAstBranch
        """

        return OLPAstBranch(self.com_object.DestinationExpress)

    @destination_express.setter
    def destination_express(self, value: OLPAstBranch):
        """
        :param OLPAstBranch value:
        """

        self.com_object.DestinationExpress = value

    def __repr__(self):
        return f'OLPTimer(name="{ self.name }")'
