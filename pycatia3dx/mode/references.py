"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2020 on 2025-09-13 15:35:27.265802

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.mode.reference import Reference
from pycatia3dx.system.collection import Collection
from pycatia3dx.types.general import CATVariant


class References(Collection):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     References
                | 
                | A collection of all the references aggregated in an object.
                | 
                | See also:
                |     Reference
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def item(self, i_index: CATVariant) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Func Item(CATVariant iIndex) As Reference
                |     Returns a reference using its index or its name from the References
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the reference to retrieve from the
                |             collection of references. As a numerics, this index is the rank of the
                |             reference in the collection. The index of the first reference in the collection
                |             is 1, and the index of the last reference is Count. As a string, it is the name
                |             you assigned to the reference using the AnyObject.Name property.
                |             
                | 
                |     Returns:
                |         The retrieved reference 
                |     Example:
                |         This example retrieves the last item in the RefList reference
                |         collection by means of the Count property.
                | 
                |          Dim LastRef As Reference
                |          Set LastRef = RefList.Item(RefList.Count)

        :param CATVariant i_index:
        :return: Reference
        """
        return Reference(self.com_object.Item(i_index))

    def __repr__(self):
        return f'References(name="{self.name}")'
