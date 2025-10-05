"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.sma_mpa_foundation.sim_analysis_case import SimAnalysisCase
from pycatia3dx.sma_mpa_foundation.sim_step import SimStep
from pycatia3dx.system.any_object import AnyObject


class SimAnalysisRestart(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimAnalysisRestart
                | 
                | Represents the analysis restart object.
                | The SimAnalysisRestart is an object that connects the downstream
                | SimAnalysisCase to an upstream SimAnalysisCase to continue the simulation from
                | the specifed upstream step. The SimAnalysisRestart is created in the downstream
                | SimAnalysisCase by the following example:
                | 
                | Example:
                |     This example demonstrates how to create the SimAnalysisRestart object from
                |     the SimAnalysisCase.Features property.
                | 
                |      Dim MyDownstreamCase As SimAnalysisCase
                |      ...
                |      Dim MyFeatureSet As SimFeatureSet
                |      Set MyFeatureSet = MyDownstreamCase.Features
                |      Dim MyRestart As SimAnalysisRestart
                |      Set MyRestart = MyFeatureSet.Add("SimAnalysisRestart")
                |      
                | 
                | Example in Python:
                | 
                |      MyFeatureSet = MyDownstreamCase.Features
                |      MyRestart = MyFeatureSet.Add("SimAnalysisRestart")
                |      
                | 
                | Restrictions:
                | 
                |     Only one SimAnalysisRestart can be created per
                |     SimAnalysisCase.
                |     The SimAnalysisRestart cannot be removed from the
                |     SimAnalysisCase.
                |     The SimAnalysisCase must be an SimStructuralAnalysisCase.
                |     The SimAnalysisCase must be empty to create a SimAnalysisRestart
                |     object.
                | 
                | An error will be returned if these restrictions are not met.
                | 
                | 
                | Usage of the SimAnalysisRestart object is demonstrated in the following
                | example:
                | 
                | Example:
                |     This example demonstrates how to use the properties of the
                |     SimAnalysisRestart object. Setting the UpstreamStep property will valuate the
                |     UpstreamAnalysisCase property, the UpstreamSimulation property, and clone the
                |     features from the upstream SimAnalysisCase.
                | 
                |      Dim MyUpstreamCase As SimAnalysisCase
                |      ...
                |      Dim MyLastStep As SimStaticStep
                |      ...
                |      Dim MyDownstreamCase As SimAnalysisCase
                |      ...
                |      Dim MyRestart As SimAnalysisRestart
                |      ...
                |      MyRestart.UpstreamStep = MyLastStep
                |      
                | 
                | Example in Python:
                | 
                |      MyRestart.UpstreamStep = MyLastStep
                |      
                | 
                | See also:
                |     SimAnalysisRestartStepProperty
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def upstream_analysis_case(self) -> SimAnalysisCase:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property UpstreamAnalysisCase() As SimAnalysisCase (Read Only)
                |     Returns the upstream analysis case to restart from.

        :return: SimAnalysisCase
        """

        return SimAnalysisCase(self.com_object.UpstreamAnalysisCase)

    @property
    def upstream_simulation(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property UpstreamSimulation() As AnyObject (Read Only)
                |     Returns the upstream simulation to restart from.

        :return: AnyObject
        """

        return AnyObject(self.com_object.UpstreamSimulation)

    @property
    def upstream_step(self) -> SimStep:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property UpstreamStep() As SimStep
                |     Sets or returns the upstream step to restart from. 
                | Copyright © 1999-2024, Dassault Systèmes. All rights reserved.

        :return: SimStep
        """

        return SimStep(self.com_object.UpstreamStep)

    @upstream_step.setter
    def upstream_step(self, value: SimStep):
        """
        :param SimStep value:
        """

        self.com_object.UpstreamStep = value

    def __repr__(self):
        return f'SimAnalysisRestart(name="{ self.name }")'
