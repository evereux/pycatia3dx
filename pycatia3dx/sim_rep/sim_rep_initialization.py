"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.sim_rep.sim_parameter_set import SimParameterSet
from pycatia3dx.system.cat_base_dispatch import CATBaseDispatch
from pycatia3dx.types.general import Variant


class SimRepInitialization(CATBaseDispatch):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 SimRepInitialization
                | 
                | Represents the simulation representation initialization
                | services.
                | Role: Initialize simulation representation with contents.
                | 
                | Example:
                | 
                |      This example shows how to retrieve the initialization service from the
                |      representation reference:
                |      
                | 
                |      Dim myRepRef As VPMRepReference
                |      Set myRepRef = ...
                |      Dim myRepInitialization As SimRepInitialization
                |      Set myRepInitialization = myRepRef.GetItem("SimRepInitialization")
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def parameters(self) -> SimParameterSet:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Parameters() As SimParameterSet (Read Only)
                |     Gets the parameters of the initialization operation.

        :return: SimParameterSet
        """

        return SimParameterSet(self.com_object.Parameters)

    @property
    def results(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Results() As CATSafeArrayVariant (Read Only)
                |     Gets the list of features created during the initialization operation.

        :return: tuple
        """

        return self.com_object.Results

    def initialize_rep(self, i_parameter_set: SimParameterSet) -> Variant:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub InitializeRep(SimParameterSet iParameterSet)
                |     Initialize a simulation representation.
                | 
                |     Parameters:
                | 
                |         iParameterSet
                |             The parameter set which contains all the objects and values to
                |             initialize the representation.
                | 
                |                 "Mode" (string) : define the initialization method (mandatory)
                |                 Legal values:
                |                     "GlobalImport" : Initialize an Abstraction Shape with a list of 3D Shape.
                |                 "3DShapes" (array of variant) : array of 3D shape representation occurrence.
                | 
                |     Example:
                | 
                |          This exemple returns the Asbtraction Shape initialized with the bodies
                |          of 3d Shape.
                |          
                | 
                |          Dim my3DShapeOcc as VPMRepOccurrence
                |          Set my3DShapeOcc = ...
                |          Dim myParamSet As SimParameterSet
                |          Set myParamSet = myRepInitialization.Parameters
                |          myParamSet.SetStringParameter "Mode", "GlobalImport"
                |          Dim my3DShapeArray(0) As Variant
                |          Set my3DShapeArray(0) = my3DShapeOcc
                |          myParamSet.SetObjectArrayParameter "3DShapes",
                |          my3DShapeArray
                |          myRepInitialization.InitializeRep myParamSet

        :param SimParameterSet i_parameter_set:
        :return: Variant
        """
        return Variant(self.com_object.InitializeRep(i_parameter_set.com_object))

    def __repr__(self):
        return f'SimRepInitialization()'
