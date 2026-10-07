"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from typing import Iterator

from pycatia3dx.system.collection import Collection
from pycatia3dx.dnb_igp_olp_use.olp_motion_group import OLPMotionGroup


class OLPMotionGroups(Collection):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     OlpMotionGroups
                | 
                | A list of motion groups.
                | 
                | This interface can only be used by a translator within the Robotics Off-line
                | Programming (OLP) Download or Upload command.
                | This object can be retrieved using
                | OlpTranslatorHelper.MotionGroups
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=OLPMotionGroup)
        self.com_object = com_object

    def item(self, i_index: int) -> OLPMotionGroup:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Item(long iIndex) As OlpMotionGroup
                |     Retrieves a motion group by its index.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of the first motion group is 1, and the index of the last
                |             motion group is Count. If the index is out of bounds, the function fails.
                |             
                | 
                |     Returns:
                |         The motion group. 

        :param int i_index:
        :return: OLPMotionGroup
        """
        return OLPMotionGroup(self.com_object.Item(i_index))

    def __getitem__(self, n: int) -> OLPMotionGroup:
        if (n + 1) > self.count:
            raise StopIteration

        return OLPMotionGroup(self.com_object.Item(n + 1))

    def __iter__(self) -> Iterator[OLPMotionGroup]:
        for i in range(self.count):
            yield OLPMotionGroup(self.com_object.Item(i + 1))

    def __repr__(self):
        return f'OLPMotionGroups(name="{self.name}")'
