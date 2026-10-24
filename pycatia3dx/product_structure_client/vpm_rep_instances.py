"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from typing import Iterator

from pycatia3dx.plm_modeller_base.plm_entities import PLMEntities
from pycatia3dx.product_structure_client.vpm_rep_instance import VPMRepInstance
from pycatia3dx.types import CATVariant


class VPMRepInstances(PLMEntities):
    """
        .. note::

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     PLMModelerBaseIDLItf.PLMEntities
                |                         VPMRepInstances
                | 
                | A collection of PLM Product Representation Instances.
                | This collection contains the children of a PLM Product
                | Reference.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def item(self, i_index: CATVariant) -> VPMRepInstance:
        """
        :param CATVariant i_index:
        :return: VPMRepInstance
        """
        return VPMRepInstance(self.com_object.Item(i_index))

    def __getitem__(self, n: int) -> VPMRepInstance:
        if (n + 1) > self.count:
            raise StopIteration

        return VPMRepInstance(self.com_object.Item(n + 1))

    def __iter__(self) -> Iterator[VPMRepInstance]:
        for i in range(self.count):
            yield VPMRepInstance(self.com_object.Item(i + 1))

    def __repr__(self):
        return f'VPMRepInstances(name="{self.name}")'
