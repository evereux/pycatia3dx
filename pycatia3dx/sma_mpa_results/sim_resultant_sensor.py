"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.sma_mpa_results.sim_sensor_base import SimSensorBase


class SimResultantSensor(SimSensorBase):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SMAMpaResultsIDLItf.SimSensorBase
                |                         SimResultantSensor
                | 
                | Represents the resultant sensor.
                | Role:After creating the resultant sensor, one needs to set the support using
                | SimSensorBase.Support or SimSensorBase.SimSupport.
                | Then set the frame selection to the sensor using the
                | SimSensorBase.FrameSelector()
                | and update the sensor using and the SimSensorBase.Update()
                | method.
                | Example:
                | 
                |  Given a SimResultsAnalysisCase object, you can create a resultant Sensor
                |  object as following.
                |  
                | 
                |  Dim oResultantSensor As SimResultantSensor
                |  Set oResultantSensor = ResultsAnalysisCase.CreateResultantSensor
                |  The current step can be retrieved from the current analysis
                |  case
                |  oCurrentStep.GetIdentifier oStepID, oStepName,
                |  oStepDescription
                |  oResultantSensor.SetStepAndFrame( oStepID, 1, 2 )
                |  oResultantSensor.Update
                |  
                | 
                | See also:
                |     #SimResultsAnalysisCase and .SimResultsStep
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def set_step_and_frame(self, ics_persistent_step_id: str, in_frame_index: int, in_load_case_index: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetStepAndFrame(CATBSTR icsPersistentStepID,long inFrameIndex,long
                | inLoadCaseIndex)
                |     Sets the step, frame and load case information needed to create the
                |     sensor.
                | 
                |     Parameters:
                | 
                |         icsPersistentStepID
                |             The persistent ID of the step. 
                |         inFrameIndex
                |             The frame index. The index starts from 1. 
                |         inLoadCaseIndex
                |             The load case index. The index starts from 1. 

        :param str ics_persistent_step_id:
        :param int in_frame_index:
        :param int in_load_case_index:
        :return: None
        """
        return self.com_object.SetStepAndFrame(ics_persistent_step_id, in_frame_index, in_load_case_index)

    def __repr__(self):
        return f'SimResultantSensor(name="{ self.name }")'
