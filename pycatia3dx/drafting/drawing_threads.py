"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.drafting.drawing_thread import DrawingThread
from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.system.collection import Collection
from pycatia3dx.types.general import CATVariant


class DrawingThreads(Collection):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     DrawingThreads
                | 
                | A collection of all the drawing threads currently managed by a drawing view of
                | drawing sheet in a drawing representation.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def add(self, i_geom_elem: AnyObject) -> DrawingThread:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Add(CATBaseDispatch iGeomElem) As DrawingThread
                |     Creates a drawing thread and adds it to the DrawingThreads collection.
                |     
                |     Notice that an authoring product licence is required.
                | 
                |     Parameters:
                | 
                |         iGeomElem
                |             Geometry to create the thread on. Be careful, this geometry must be
                |             a 2D geometry 
                | 
                |     Returns:
                |         The created drawing thread 
                | 
                | Example:
                |     The following example creates a drawing thread and retrieved in MyThread in
                |     the drawing view collection of the MyView drawing view. This view belongs to
                |     the drawing view collection of the drawing sheet
                | 
                |      Dim MyView As DrawingView
                |      Set MyView = MySheet.Views.ActiveView
                |      Dim MyThread As DrawingThread
                |      Set MyThread = MyView.Threads.Add(iGeomElem)

        :param AnyObject i_geom_elem:
        :return: DrawingThread
        """
        return DrawingThread(self.com_object.Add(i_geom_elem.com_object))

    def item(self, i_index: CATVariant) -> DrawingThread:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Item(CATVariant iIndex) As DrawingThread
                |     Returns a drawing thread using its index from the DrawingThreads
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of the drawing thread to retrieve from the collection of
                |             drawing threads. As a numerics, this index is the rank of the drawing thread in
                |             the collection. The index of the first drawing thread in the collection is 1,
                |             and the index of the last drawing thread is Count. As a string, it is the name
                |             you assigned to the drawing thread using the AnyObject.Name property or when
                |             creating it using the Add method. 
                | 
                |     Returns:
                |         The retrieved drawing thread 
                |     Example:
                |         This example retrieves in ThisDrawingThread the second drawing thread,
                |         in the drawing view collection of the active view in the active sheet, in the
                |         active representation supposed to be a drawing
                |         representation.
                | 
                |          Dim MyView  As DrawingView
                |          Set MyView  = MySheet.Views.ActiveView
                |          Dim ThisDrawingThread As DrawingThread
                |          Set ThisDrawingThread = MyView.Threads.Item(2)

        :param CATVariant i_index:
        :return: DrawingThread
        """
        return DrawingThread(self.com_object.Item(i_index))

    def remove(self, i_index: CATVariant) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Remove(CATVariant iIndex)
                |     Removes a drawing thread from the DrawingThreads collection.
                |     
                |     Notice that an authoring product licence is required.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of the drawing thread to remove from the collection of
                |             drawing threads. As a numerics, this index is the rank of the drawing thread in
                |             the collection. The index of the first drawing thread in the collection is 1,
                |             and the index of the last drawing thread is Count.
                |             
                | 
                |     Example:
                |         The following example removes the third drawing thread in the drawing
                |         thread collection of the active view of the active representation, supposed to
                |         be a drawing representation.
                | 
                |          Dim MyView As DrawingView
                |          Set MyView  = MySheet.Views.ActiveView
                |          MyView.DrawingThreads.Remove(3)

        :param CATVariant i_index:
        :return: None
        """
        return self.com_object.Remove(i_index)

    def __repr__(self):
        return f'DrawingThreads(name="{self.name}")'
