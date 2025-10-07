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


class OLPPulse(OLPInstruction):

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
                |                         OlpPulse
                | 
                | An instruction used to asynchronously change the value of an external
                | output.
                | 
                | This interface can only be used by a translator within the Robotics Off-line
                | Programming (OLP) Download or Upload command.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def delay(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Delay() As double
                |     Get/Set the delay value in seconds.

        :return: float
        """

        return self.com_object.Delay

    @delay.setter
    def delay(self, value: float):
        """
        :param float value:
        """

        self.com_object.Delay = value

    @property
    def delay_express(self) -> OLPAstBranch:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property DelayExpress() As OlpAstBranch
                |     Get/Set the timeout value in expression.

        :return: OLPAstBranch
        """

        return OLPAstBranch(self.com_object.DelayExpress)

    @delay_express.setter
    def delay_express(self, value: OLPAstBranch):
        """
        :param OLPAstBranch value:
        """

        self.com_object.DelayExpress = value

    @property
    def destination(self) -> OLPVariable:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Destination() As OlpVariable
                |     The variable which is being assigned.
                |     You can retrieve an existing variable using OlpInstruction.FindVariable or
                |     create a new one using OlpVariables.

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

    @property
    def duration(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Duration() As double
                |     Get/Set the duration value in seconds.
                |     Only get the duration value if UseDuration is set to True.

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
    def duration_express(self) -> OLPAstBranch:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property DurationExpress() As OlpAstBranch
                |     Get/Set the timeout value in expression.

        :return: OLPAstBranch
        """

        return OLPAstBranch(self.com_object.DurationExpress)

    @duration_express.setter
    def duration_express(self, value: OLPAstBranch):
        """
        :param OLPAstBranch value:
        """

        self.com_object.DurationExpress = value

    @property
    def source(self) -> OLPAstBranch:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Source() As OlpAstBranch
                |     The expression that evaluates to the value being assigned.
                |     When set the OlpAstBranch.Value of the AST tree is used for the expression.
                |     When retrieved the DELMIA expression is parsed and is returned in the format
                |     expected by OlpExpressionFixerDownload. You can find more information on the
                |     OLP Expression AST format in the documentation under Automation | Robotics |
                |     Robotics Offline Programming | Offline Programming Expression Translation.

        :return: OLPAstBranch
        """

        return OLPAstBranch(self.com_object.Source)

    @source.setter
    def source(self, value: OLPAstBranch):
        """
        :param OLPAstBranch value:
        """

        self.com_object.Source = value

    @property
    def source_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SourceType() As DELOlpPulseType
                |     Get/Set the type of Pulse value.
                |     This is a simple way to access the most common types of pulsed values. If
                |     this property is set, the Source expression is automatically generated.

        :return: DELOlpPulseType
        """

        return self.com_object.SourceType

    @source_type.setter
    def source_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.SourceType = value

    @property
    def use_duration(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property UseDuration() As boolean
                |     Get/Set whether the duration is used.
                |     If False, then the duration is effectively infinity and the Duration
                |     property should not be retrieved. If True, then the Duration value is used.

        :return: bool
        """

        return self.com_object.UseDuration

    @use_duration.setter
    def use_duration(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.UseDuration = value

    def __repr__(self):
        return f'OLPPulse(name="{ self.name }")'
