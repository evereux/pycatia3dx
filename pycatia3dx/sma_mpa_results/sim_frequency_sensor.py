"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.sma_mpa_results.sim_sensor_base import SimSensorBase


class SimFrequencySensor(SimSensorBase):

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
                |                         SimFrequencySensor
                | 
                | Represents the frequency sensor.
                | Role:After creating the frequency sensor, one needs to set the frame selection
                | to the sensor using
                | the SimSensorBase.FrameSelector()
                | and update the sensor using and the SimSensorBase.Update()
                | method.
                | Example:
                | 
                |  Given a SimResultsAnalysisCase object, you can create a Frequency Sensor
                |  object as following.
                |  
                | 
                |  Dim oFrequencySensor As SimFrequencySensor
                |  Set oFrequencySensor = ResultsAnalysisCase.CreateFrequencySensor
                |  Dim oFrameSelection As SimFramesSelection
                |  Set oFrameSelection = ResultsAnalysisCase.CreateFrameSelector
                |  oFrameSelection.SymbolicFrameRange = SimLastFrameOfEachStep
                |  oFrequencySensor.FrameSelector = oFrameSelection
                |  oFrequencySensor.Update
                |  
                | 
                | See also:
                |     SimResultsAnalysisCase

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def __repr__(self):
        return f'SimFrequencySensor(name="{ self.name }")'
