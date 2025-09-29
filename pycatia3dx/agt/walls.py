"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.agt.wall import Wall
from pycatia3dx.system.collection import Collection
from pycatia3dx.types.general import CATVariant


class Walls(Collection):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     Walls
                | 
                | Object for Walls.
                | To retrieve a wall from collection.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def item(self, i_index: CATVariant) -> Wall:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Func Item(CATVariant iIndex) As Wall
                |     Retrieves a Wall from the collection of Wall.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of Wall 
                | 
                |     Example:
                | 
                | 
                |              This example retrieves Wall from the list of
                |              walls
                |              
                | 
                |              Dim myPart as CATIAPart
                |              Set myPart = CATIA.ActiveEditor.ActievObject
                |              Dim MyAGTRoot As AGTRoot
                |              Set MyAGTRoot = myPart.GetItem("CATAGTRoot")
                |              'Get a second wall from the list of wall by index
                |              Dim WallByIndex As Wall
                |              Set WallByIndex = MyAGTRoot.Walls.Item(2)
                |              'Get a wall named "MyWall.2" from the list of wall by
                |              name
                |              Dim WallByName As Wall
                |              Set WallByName = MyAGTRoot.Walls.Item("MyWall.2")

        :param CATVariant i_index:
        :return: Wall
        """
        return Wall(self.com_object.Item(i_index))

    def __repr__(self):
        return f'Walls(name="{self.name}")'
