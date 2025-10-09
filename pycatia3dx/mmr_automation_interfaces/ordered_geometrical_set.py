#! usr/bin/python3.9
"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 12:30:08.885021

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from typing import TYPE_CHECKING

from pycatia3dx.mmr_automation_interfaces.hybrid_shape import HybridShape
from pycatia3dx.mmr_automation_interfaces.hybrid_shapes import HybridShapes
from pycatia3dx.mmr_automation_interfaces.sketches import Sketches
from pycatia3dx.system.any_object import AnyObject

if TYPE_CHECKING:
    from pycatia3dx.mmr_automation_interfaces.bodies import Bodies
    from pycatia3dx.mmr_automation_interfaces.ordered_geometrical_sets import OrderedGeometricalSets


class OrderedGeometricalSet(AnyObject):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     OrderedGeometricalSet
                | 
                | The object is an ordered geometrical set.
                | The ordered geometrical set manages a set of hybrid shapes, a set of bodies and
                | a set of ordered geometrical sets.
                | It belongs to the OrderedGeometricalSets collection of a Part or
                | OrderedGeometricalSet object.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def bodies(self) -> 'Bodies':
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Property Bodies() As Bodies (Read Only)
                |     Returns the ordered geometrical set's Bodies collection.
                | 
                |     Example:
                |         The following example returns in bodyColl the collection of bodies of
                |         the ordered geometrical set OrderedGeometricalSet1 :
                | 
                |          Set bodyColl = OrderedGeometricalSet1.Bodies

        :return: Bodies
        """
        from pycatia3dx.mmr_automation_interfaces.bodies import Bodies
        return Bodies(self.com_object.Bodies)

    @property
    def hybrid_shapes(self) -> HybridShapes:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Property HybridShapes() As HybridShapes (Read Only)
                |     Returns the list of hybrid shapes included in the ordered geometrical
                |     set.
                | 
                |     Returns:
                |         oHybridShapes The list of hybrid shapes in the ordered geometrical set
                |         (@see CATIAHybridShapes
                |         for more information).
                | 
                |         Example:
                |             The following example returns in HybridShapes1 the list
                |             of
                |             hybrid shapes in the ordered geometrical
                |             setOrderedGeometricalSet1:
                | 
                |              Dim HybridShapes1 As HybridShapes
                |              Set HybridShapes1 = OrderedGeometricalSet1.HybridShapes

        :return: HybridShapes
        """

        return HybridShapes(self.com_object.HybridShapes)

    @property
    def ordered_geometrical_sets(self) -> 'OrderedGeometricalSets':
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Property OrderedGeometricalSets() As OrderedGeometricalSets (Read
                | Only)
                |     Returns the ordered geometrical set's OrderedGeometricalSets
                |     collection.
                | 
                |     Example:
                |         The following example returns in OrderedGeometricalSetColl the
                |         collection of ordered geometrical set of the ordered geometrical set
                |         OrderedGeometricalSet1 :
                | 
                |          Set OrderedGeometricalSetColl = OrderedGeometricalSet1.OrderedGeometricalSets

        :return: OrderedGeometricalSets
        """
        from pycatia3dx.mmr_automation_interfaces.ordered_geometrical_sets import OrderedGeometricalSets
        return OrderedGeometricalSets(self.com_object.OrderedGeometricalSets)

    @property
    def ordered_sketches(self) -> Sketches:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Property OrderedSketches() As Sketches (Read Only)
                |     Returns the ordered geometrical set's Sketches collection. These sketches
                |     are those inside the ordered geometrical set at all
                |     levels.
                | 
                |     Example:
                |         The following example returns in sketchesCollection the collection of
                |         sketches of an ordered geometrical set :
                | 
                |          Set sketchesCollection = OrderedGeometricalSet1.OrderedSketches

        :return: Sketches
        """

        return Sketches(self.com_object.OrderedSketches)

    def insert_hybrid_shape(self, i_hybrid_shape: HybridShape) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Sub InsertHybridShape(HybridShape iHybridShape)
                |     Inserts a hybrid shape to the ordered geometrical set.
                | 
                |     Parameters:
                | 
                |         iHybridShape
                |             The hybrid shape to insert. 
                | 
                |     Example:
                |         This example inserts the hybrid shape HybridShape1 to the ordered
                |         geometrical set OrderedGeometricalSet1:
                | 
                |          OrderedGeometricalSet1.InsertHybridShape
                |          (HybridShape1)

        :param HybridShape i_hybrid_shape:
        :return: None
        """
        return self.com_object.InsertHybridShape(i_hybrid_shape.com_object)

    def __repr__(self):
        return f'OrderedGeometricalSet(name="{self.name}")'
