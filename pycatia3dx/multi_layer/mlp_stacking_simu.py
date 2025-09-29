"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.multi_layer.mlp_simu_layers import MLPSimuLayers
from pycatia3dx.system.any_object import AnyObject


class MLPStackingSimu(AnyObject):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MLPStackingSimu
                | 
                | CATIAMLPStackingSimu Role:Represents CATIAMLPStackingSimu that allow to query
                | on the stacking.
                | 
                | Example:
                |     This example illustrates how to call CATIAMLPStackingSimu interfaces .
                |     
                | 
                |     'FIND THE STACKING
                |         Set Stacking = myPart.FindObjectByName("Stacking")
                |         Dim StackingSimu As MLPStackingSimu
                |         Set StackingSimu = Stacking.GetItem("CATMLPVBStackingSimu")
                |       
                |     'CREATE MLP SERVICES
                |         Dim StackingSimuService As MLPSimuLayerServices
                |         Set StackingSimuService = Stacking.GetItem("CATMLPVBStackingSimu")
                |         
                |     'RETRIEVE THE LIST OF LAYERS
                |         Dim listOfLayers As MLPSimuLayers
                |         Set listOfLayers = StackingSimu.Layers
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def layers(self) -> MLPSimuLayers:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Layers() As MLPSimuLayers (Read Only)
                |     Returns the list of layers under the stacking.
                | 
                |     Parameters:
                | 
                |         oListOfLayers
                |             List Of layers under the Stacking

        :return: MLPSimuLayers
        """

        return MLPSimuLayers(self.com_object.Layers)

    @property
    def optimized_mode(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property OptimizedMode() As boolean
                |     Returns or set the stacking performance mode (need to be true for
                |     simulation).

        :return: bool
        """

        return self.com_object.OptimizedMode

    @optimized_mode.setter
    def optimized_mode(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.OptimizedMode = value

    def __repr__(self):
        return f'MlpStackingSimu(name="{self.name}")'
