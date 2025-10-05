"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class SimAnalysisRestartStepProperty(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimAnalysisRestartStepProperty
                | 
                | Represents the restart property for a step.
                | The SimAnalysisRestartStepProperty is an object that provides access to restart
                | options on the step object in the upstream SimAnalysisCase.
                | 
                | Example:
                |     This example demonstrates how to retrieve the
                |     SimAnalysisRestartStepProperty object from a SimStaticStep. The same pattern
                |     applies to all supported steps.
                | 
                |      Dim MyStaticStep As SimStaticStep
                |      ...
                |      Dim MyRestartStepProperty As
                |      SimAnalysisRestartStepProperty
                |      Set MyRestartStepProperty = MyStaticStep.RestartStepProperty
                |      
                | 
                | Example in Python:
                | 
                |      MyRestartStepProperty = MyStaticStep.RestartStepProperty
                |      
                | 
                | See also:
                |     SimAnalysisRestart
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def generate_flag(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property GenerateFlag() As boolean
                |     Returns or sets the flag that determines if the restart generation is
                |     requested.
                |     True: the restart generation is requested.
                |     False: the restart generation is not requested. 

        :return: bool
        """

        return self.com_object.GenerateFlag

    @generate_flag.setter
    def generate_flag(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.GenerateFlag = value

    def __repr__(self):
        return f'SimAnalysisRestartStepProperty(name="{ self.name }")'
