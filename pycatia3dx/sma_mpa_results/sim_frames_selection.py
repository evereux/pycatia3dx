"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class SimFramesSelection(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimFramesSelection
                | 
                | Sets the step and frame information.
                | Role:Frame Selection lets you select steps and frames for a customized frame
                | range for animations, sensors, and envelopes.
                | It can be used to customize a data range with unique combinations of time,
                | mode, or frequency settings.
                | Example:
                | 
                |  Given a SimResultsAnalysisCase object, you can create a Frame Selection object
                |  as following.
                |  
                | 
                |  Dim oFrameSelection As SimFramesSelection
                |  Set oFrameSelection = ResultsAnalysisCase.CreateFrameSelector
                |  
                | 
                | See also:
                |     SimResultsAnalysisCase
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def step_list(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property StepList(CATSafeArrayVariant iStepsList) (Write Only)
                |     Sets the step List.
                |     It is a list of strings which are the steps ID's. The step ID's can be
                |     retrieved from SimResultsStep.GetIdentifier().
                | 
                |     Example:
                | 
                |          The following example shows how to retrieve the step ID from results
                |          step
                |          
                | 
                |          Dim stepId As String
                |          Dim stepName As String
                |          Dim stepDescription As String
                |          oResultsStep.GetIdentifier stepId, stepName,
                |          stepDescription

        :return: bool
        """

        return self.com_object.StepList

    @step_list.setter
    def step_list(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.StepList = value

    @property
    def symbolic_frame_range(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SymbolicFrameRange(SimSymbolicFrameRangesEnum ieSymbolicFrameRange)
                | (Write Only)
                |     Sets the type of symbolic frame Range.
                |     Following are the list of available values:
                |     SimUndefined
                |     SimAllFrames
                |     SimLastFrameOfEachStep
                |     SimAllFramesInStep
                |     SimTimeBasedFrames
                |     SimFrequencyFrames In case of SimAllFramesInStep, one must use the StepList
                |     method
                |     to specify the step ID.

        :return: bool
        """

        return self.com_object.SymbolicFrameRange

    @symbolic_frame_range.setter
    def symbolic_frame_range(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.SymbolicFrameRange = value

    def set_frames(self, i_nb_frames: tuple, i_frame_index: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetFrames(CATSafeArrayVariant iNbFrames,CATSafeArrayVariant
                | iFrameIndex)
                |     Sets the frames to the frame selector. The array size must be same as that
                |     of steps/load cases.
                | 
                |     Parameters:
                | 
                |         iNbFrames
                |             The number of frames in step/load case to set. 
                |         iFrameIndex
                |             The frame index to set.

        :param tuple i_nb_frames:
        :param tuple i_frame_index:
        :return: None
        """
        return self.com_object.SetFrames(i_nb_frames, i_frame_index)

    def set_load_cases(self, i_nb_load_cases_in_step: tuple, i_load_case_id_list: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetLoadCases(CATSafeArrayVariant iNbLoadCasesInStep,CATSafeArrayVariant
                | iLoadCaseIDList)
                |     Sets the load cases to the frame selector. This method must be called if
                |     anyone has specified a list of steps (given through StepList() method). No need
                |     to call this if there are no load cases in the steps. Suppose if there are two
                |     steps and only one out of them has load cases, then for the steps without load
                |     cases the user will have to specify the values as zero and the load case ID as
                |     NULL string.
                | 
                |     Parameters:
                | 
                |         iNbLoadCasesInStep
                |             It is the number of load cases in the step. The size of list must
                |             be same as the steps specified in the StepList() method. Also it must be in the
                |             same order as that of the steps. 
                |         iLoadCaseIDList
                |             List of load case ID's to set. The ID's can be retrieved through
                |             SMAIAMpaResultsManager::GetLoadCaseIdentifier() method.

        :param tuple i_nb_load_cases_in_step:
        :param tuple i_load_case_id_list:
        :return: None
        """
        return self.com_object.SetLoadCases(i_nb_load_cases_in_step, i_load_case_id_list)

    def __repr__(self):
        return f'SimFramesSelection(name="{ self.name }")'
