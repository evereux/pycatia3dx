"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2020 on 2025-09-13 15:35:27.265802

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.interfaces.editor import Editor
from pycatia3dx.system.collection import Collection
from pycatia3dx.types.general import CATVariant


class Editors(Collection):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     Editors
                | 
                | A collection of all the editors objects currently managed by the
                | application.
                | 
                | See also:
                |     Editor
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def item(self, i_index: CATVariant) -> Editor:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Func Item(CATVariant iIndex) As Editor
                |     Returns an editor using its index from the editors
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of the editor to retrieve from the collection of editors.
                |             This index is the rank of the editor in the collection. The index of the first
                |             editor in the collection is 1, and the index of the last editor is Count.
                |             
                | 
                |     Returns:
                |         The retrieved editor 
                |     Example:
                |         This example retrieves in ThisEditor the fifth editor in the
                |         collection.
                | 
                |          Dim ThisEditor As Editor
                |          Set ThisEditor = Editors.Item(5)

        :param CATVariant i_index:
        :return: Editor
        """
        return Editor(self.com_object.Item(i_index))

    def __repr__(self):
        return f'Editors(name="{self.name}")'
