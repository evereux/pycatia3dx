"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.dnb_igp_olp_use.olp_ast_branch import OLPAstBranch
from pycatia3dx.dnb_igp_olp_use.olp_conveyor_tracking_profile import OLPConveyorTrackingProfile
from pycatia3dx.dnb_igp_olp_use.olp_instruction import OLPInstruction


class OLPWait(OLPInstruction):

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
                |                         OlpWait
                | 
                | A wait instruction.
                | 
                | This interface can only be used by a translator within the Robotics Off-line
                | Programming (OLP) Download or Upload command.
                | This is an instruction that waits for the condition expression to evaluate to
                | true. If the timeout is enabled and the specified amount of time elapses before
                | the condition is satisfied, then execution proceeds to the next
                | instruction. This instruction can also be used as a pure
                | delay.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def condition(self) -> OLPAstBranch:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Condition() As OlpAstBranch
                |     The expression that must evaluate to true before execution
                |     continues.
                |     When set, the OlpAstBranch.Value of the AST tree is used for the
                |     expression. When retrieved, the DELMIA expression is parsed and is returned in
                |     the format expected by OlpExpressionFixerDownload. You can find more
                |     information on the OLP Expression AST format in the documentation under
                |     Automation | Robotics | Robotics Offline Programming | Offline Programming
                |     Expression Translation.

        :return: OLPAstBranch
        """

        return OLPAstBranch(self.com_object.Condition)

    @condition.setter
    def condition(self, value: OLPAstBranch):
        """
        :param OLPAstBranch value:
        """

        self.com_object.Condition = value

    @property
    def conveyor_tracking_profile(self) -> OLPConveyorTrackingProfile:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ConveyorTrackingProfile() As
                | OlpConveyorTrackingProfile
                |     Get/Set the conveyor tracking profile associated with the wait instruction
                |     if this is a conveyor tracking wait.

        :return: OLPConveyorTrackingProfile
        """

        return OLPConveyorTrackingProfile(self.com_object.ConveyorTrackingProfile)

    @conveyor_tracking_profile.setter
    def conveyor_tracking_profile(self, value: OLPConveyorTrackingProfile):
        """
        :param OLPConveyorTrackingProfile value:
        """

        self.com_object.ConveyorTrackingProfile = value

    @property
    def is_conveyor_wait(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property IsConveyorWait() As boolean (Read Only)
                |     Get/Set whether the wait instruction is waiting for a conveyor to reach a
                |     certain position.

        :return: bool
        """

        return self.com_object.IsConveyorWait

    @property
    def is_pure_delay(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property IsPureDelay() As boolean (Read Only)
                |     Indicates if this instruction is used as a pure delay.

        :return: bool
        """

        return self.com_object.IsPureDelay

    @property
    def is_simple_conveyor_wait(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property IsSimpleConveyorWait() As boolean (Read Only)
                |     Get/Set whether the wait instruction is in the simple format waiting for
                |     the conveyor to reach the inbound offset of the conveyor tracking profile.

        :return: bool
        """

        return self.com_object.IsSimpleConveyorWait

    @property
    def time_out_express(self) -> OLPAstBranch:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property TimeOutExpress() As OlpAstBranch
                |     Get/Set the timeout value in expression.

        :return: OLPAstBranch
        """

        return OLPAstBranch(self.com_object.TimeOutExpress)

    @time_out_express.setter
    def time_out_express(self, value: OLPAstBranch):
        """
        :param OLPAstBranch value:
        """

        self.com_object.TimeOutExpress = value

    @property
    def timeout(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Timeout() As double
                |     Get/Set the timeout value in seconds.
                |     Only get the timeout value if UseTimeout is set to True.

        :return: float
        """

        return self.com_object.Timeout

    @timeout.setter
    def timeout(self, value: float):
        """
        :param float value:
        """

        self.com_object.Timeout = value

    @property
    def use_timeout(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property UseTimeout() As boolean
                |     Get/Set whether the wait instruction uses a timeout.
                |     If False, then the timeout is effectively infinity and the Timeout property
                |     should not be retrieved. If True, then the Timeout value is used.

        :return: bool
        """

        return self.com_object.UseTimeout

    @use_timeout.setter
    def use_timeout(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.UseTimeout = value

    def make_pure_delay(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub MakePureDelay()
                |     Sets the condition such that this instruction is a pure
                |     delay.
                |     After calling this function you should set the delay time using Timeout.

        :return: None
        """
        return self.com_object.MakePureDelay()

    def __repr__(self):
        return f'OLPWait(name="{ self.name }")'
