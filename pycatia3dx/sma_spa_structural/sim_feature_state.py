"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.sma_mpa_foundation.sim_step import SimStep
from pycatia3dx.system.any_object import AnyObject


class SimFeatureState(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimFeatureState
                | 
                | Represents the Feature State object.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def amplitude(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Amplitude() As CATBaseDispatch
                |     Returns or sets the amplitude reference. It will adhere to
                |     SMAIMpaTabularAmplitude interface if the amplitude reference points to a
                |     tabular amplitude.

        :return: AnyObject
        """

        return AnyObject(self.com_object.Amplitude)

    @amplitude.setter
    def amplitude(self, value: AnyObject):
        """
        :param AnyObject value:
        """

        self.com_object.Amplitude = value

    @property
    def amplitude_flag(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property AmplitudeFlag() As boolean (Read Only)
                |     Returns or sets the flag that determines if the feature has an
                |     amplitude.
                |     TRUE: the feature has an amplitude.
                |     FALSE: the feature has no amplitude.

        :return: bool
        """

        return self.com_object.AmplitudeFlag

    @property
    def beginning_increment(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property BeginningIncrement() As long
                |     Returns or sets the Beginning Increment. Use 1 for the first increment. Use
                |     999999 for the last increment.

        :return: int
        """

        return self.com_object.BeginningIncrement

    @beginning_increment.setter
    def beginning_increment(self, value: int):
        """
        :param int value:
        """

        self.com_object.BeginningIncrement = value

    @property
    def beginning_step(self) -> SimStep:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property BeginningStep() As SimStep
                |     Returns or sets the Beginning Step.

        :return: SimStep
        """

        return SimStep(self.com_object.BeginningStep)

    @beginning_step.setter
    def beginning_step(self, value: SimStep):
        """
        :param SimStep value:
        """

        self.com_object.BeginningStep = value

    @property
    def ending_increment(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property EndingIncrement() As long
                |     Returns or sets the Ending Increment. Use 1 for the first increment. Use
                |     999999 for the last increment.

        :return: int
        """

        return self.com_object.EndingIncrement

    @ending_increment.setter
    def ending_increment(self, value: int):
        """
        :param int value:
        """

        self.com_object.EndingIncrement = value

    @property
    def ending_step(self) -> SimStep:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property EndingStep() As SimStep
                |     Returns or sets the Ending Step.

        :return: SimStep
        """

        return SimStep(self.com_object.EndingStep)

    @ending_step.setter
    def ending_step(self, value: SimStep):
        """
        :param SimStep value:
        """

        self.com_object.EndingStep = value

    @property
    def feature(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Feature() As CATBaseDispatch (Read Only)
                |     Returns the feature referenced by the feature state.

        :return: AnyObject
        """

        return AnyObject(self.com_object.Feature)

    @property
    def field_flag(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property FieldFlag() As boolean (Read Only)
                |     Returns if the feature state has a field. This example demonstrates how to
                |     use SimFeatureState from a field.
                | 
                |      Dim MyFeatureState As SimFeatureState
                |      Dim MySteadyStateHeatTransferStep As
                |      SimSteadyStateHeatTransferStep
                |      ...
                |      If MyFeatureState.FieldFlag = True Then
                |          MyFeatureState.BeginningStep = MySteadyStateHeatTransferStep
                |          MyFeatureState.BeginningIncrement = 1
                |          MyFeatureState.EndingStep = MySteadyStateHeatTransferStep
                |          MyFeatureState.EndingIncrement = 999999
                |      End If

        :return: bool
        """

        return self.com_object.FieldFlag

    @property
    def phase_angle(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property PhaseAngle() As double
                |     Returns or sets the phase angle value.

        :return: float
        """

        return self.com_object.PhaseAngle

    @phase_angle.setter
    def phase_angle(self, value: float):
        """
        :param float value:
        """

        self.com_object.PhaseAngle = value

    @property
    def phase_angle_flag(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property PhaseAngleFlag() As boolean (Read Only)
                |     Returns or sets the flag that determines if the feature has a phase
                |     angle.
                |     TRUE: the feature has a phase angle.
                |     FALSE: the feature has no phase angle.

        :return: bool
        """

        return self.com_object.PhaseAngleFlag

    @property
    def propagation_state(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property PropagationState() As CATBSTR (Read Only)
                |     Returns the propagation state of the feature referenced by the feature
                |     state. Possible values:
                | 
                |     Created
                |         Created in this step.
                |     Propagated
                |         Propagated from a preceding General step in this General
                |         step.
                |     Modified
                |         Propagated and modified in this General step.
                |     Deactivated
                |         Propagated and deactivated in this General step.
                |     Inactive
                |         Propagated and inactive in this step.
                |     Reactivated
                |         Deactivated in preceding General step is activated in this General
                |         step.
                |     PropagatedfromBaseState
                |         Propagated from a preceding General step into this Perturbation
                |         step.
                |     ModifiedfromBaseState
                |         Propagated and modified from a preceding General step in this
                |         Perturbation step.
                |     DeactivatedfromBaseState
                |         Propagated and deactivated from a preceding General step in this
                |         Perturbation step.
                |     BuiltintoBaseState
                |         Inherited state from the preceding General step in this Perturbation
                |         step. Applies only to boundary conditions.
                |     BuiltintoMode
                |         Inherited modes of the preceding Frequency step in this Linear Dynamic
                |         step. Applies only to boundary conditions.
                |     NotApplicable
                |         Does not apply in this step.

        :return: str
        """

        return self.com_object.PropagationState

    @property
    def scale_factor(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ScaleFactor() As double
                |     Returns or sets the scale factor value.

        :return: float
        """

        return self.com_object.ScaleFactor

    @scale_factor.setter
    def scale_factor(self, value: float):
        """
        :param float value:
        """

        self.com_object.ScaleFactor = value

    @property
    def scale_factor_flag(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ScaleFactorFlag() As boolean (Read Only)
                |     Returns or sets the flag that determines if the feature has a scale
                |     factor.
                |     TRUE: the feature has a scale factor.
                |     FALSE: the feature has no scale factor. 

        :return: bool
        """

        return self.com_object.ScaleFactorFlag

    def __repr__(self):
        return f'SimFeatureState(name="{ self.name }")'
