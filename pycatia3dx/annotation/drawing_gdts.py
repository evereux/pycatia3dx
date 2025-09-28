"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.annotation.drawing_gdt import DrawingGDT
from pycatia3dx.system.collection import Collection
from pycatia3dx.types.general import CATVariant


class DrawingGDTs(Collection):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     DrawingGDTs
                | 
                | A collection of all the drawing GDTs currently managed by a drawing view of
                | drawing sheet in a drawing document.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def add(self, i_position_leader_x: float, i_position_leader_y: float, i_position_x: float, i_position_y: float, i_gdt_symbol: int, i_text: str) -> DrawingGDT:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Func Add(double iPositionLeaderX,double iPositionLeaderY,double
                | iPositionX,double iPositionY,long iGDTSymbol,CATBSTR iText) As
                | DrawingGDT
                |     Creates a drawing GDT and adds it to the drawing GDTs collection. This
                |     drawing GDT becomes the active one.
                | 
                |     Parameters:
                | 
                |         iPositionLeaderX,
                |             iPositionLeaderY The drawing leader of the GDT x and y coordinates,
                |             expressed in millimeters, and expressed with respect to the view coordinate
                |             system 
                |         iPositionX,
                |             iPositionY The drawing GDT x and y coordinates, expressed in
                |             millimeters, and expressed with respect to the view coordinate system
                |             
                |         iGDTSymbol
                |             The symbol to use in the first row. 
                | 
                |     See also:
                |         CATIADrawingGDT::GetToleranceType
                |     Parameters:
                | 
                |         iText
                |             The text of the iGDTSymbol

        :param float i_position_leader_x:
        :param float i_position_leader_y:
        :param float i_position_x:
        :param float i_position_y:
        :param int i_gdt_symbol:
        :param str i_text:
        :return: DrawingGDT
        """
        return DrawingGDT(self.com_object.Add(i_position_leader_x, i_position_leader_y, i_position_x, i_position_y, i_gdt_symbol, i_text))

    def item(self, i_index: CATVariant) -> DrawingGDT:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Func Item(CATVariant iIndex) As DrawingGDT
                |     Returns a drawing GDT using its index from the drawing GDTs
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of the drawing GDT to retrieve from the collection of
                |             drawing GDTs. As a numerics, this index is the rank of the drawing GDT in the
                |             collection. The index of the first drawing GDT in the collection is 1, and the
                |             index of the last drawing GDT is Count. 
                | 
                |     Returns:
                |         The retrieved drawing GDT 
                | 
                | Example:
                |     This example retrieves in ThisDrawingGDT the second drawing GDT, in the
                |     drawing GDT collection of the active view in the active sheet, in the active
                |     document supposed to be a drawing document.
                | 
                |      Dim MyView  As DrawingView
                |      Set MyView  = MySheet.Views.ActiveView
                |      Dim ThisDrawingGDT As DrawingGDT
                |      Set ThisDrawingGDT = MyView.GDTs.Item(2)

        :param CATVariant i_index:
        :return: DrawingGDT
        """
        return DrawingGDT(self.com_object.Item(i_index))

    def remove(self, i_index: CATVariant) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub Remove(CATVariant iIndex)
                |     Removes a drawing GDT from the drawing GDTs collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of the drawing GDT to remove from the collection of
                |             drawing GDTs. As a numerics, this index is the rank of the drawing GDTs in the
                |             collection. The index of the first drawing GDT in the collection is 1, and the
                |             index of the last drawing GDT is Count. 
                | 
                |     Example:
                |         The following example removes the third drawing GDT from the drawing
                |         GDT collection of the active view of the active document, supposed to be a
                |         drawing document.
                | 
                |          Dim MyView As DrawingView
                |          Set MyView  = MySheet.Views.ActiveView
                |          MyView.GDTs.Remove(3)

        :param CATVariant i_index:
        :return: None
        """
        return self.com_object.Remove(i_index)

    def __repr__(self):
        return f'DrawingGdTs(name="{ self.name }")'
