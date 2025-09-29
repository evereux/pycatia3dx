"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.fmt_mode.sim_method import SimMethod
from pycatia3dx.system.cat_base_dispatch import CATBaseDispatch
from pycatia3dx.types.general import CATVariant


class SimMethodSet(CATBaseDispatch):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 SimMethodSet
                | 
                | Interface representing the simulation set that owns method
                | objects.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def item(self, i_index: CATVariant) -> SimMethod:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Item(CATVariant iIndex) As SimMethod
                |     Returns a method using its index from the collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of the method to retrieve from the
                |             collection.
                |             This index is the rank of the method in the collection. The index
                |             of the first method in the collection is 1, and the index of the last method is
                |             Count. 
                | 
                |     Returns:
                |         The retrieved method.

        :param CATVariant i_index:
        :return: SimMethod
        """
        return SimMethod(self.com_object.Item(i_index))

    def __repr__(self):
        return f'SimMethodSet()'
