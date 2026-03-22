"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.multi_layer.mlp_simu_layer import MLPSimuLayer
from pycatia3dx.system.collection import Collection
from pycatia3dx.types.general import CATVariant


class MLPSimuLayers(Collection):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     MLPSimuLayers
                | 
                | Represents CATIAMLPSimuLayers that allow to have a list of
                | CATIAMLPSimuLayer.
                | Role: List ofCATIAMLPSimuLayer .
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=MLPSimuLayer)
        self.com_object = com_object

    def item(self, i_index: CATVariant) -> MLPSimuLayer:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Item(CATVariant iIndex) As MLPSimuLayer
                |     Retrieves a layer with the specified name or index.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The specified name/index of the object to retrieve
                |             
                |         oLayerSimu
                |             The returned object

        :param CATVariant i_index:
        :return: MLPSimuLayer
        """
        return MLPSimuLayer(self.com_object.Item(i_index))

    def __repr__(self):
        return f'MlpSimuLayers(name="{self.name}")'
