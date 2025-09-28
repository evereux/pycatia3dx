#! usr/bin/python3.9
"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 12:30:08.885021

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.mmr_automation_interfaces.hybrid_bodies import HybridBodies
from pycatia3dx.mmr_automation_interfaces.hybrid_shape import HybridShape
from pycatia3dx.mmr_automation_interfaces.hybrid_shapes import HybridShapes
from pycatia3dx.mmr_automation_interfaces.ordered_geometrical_sets import OrderedGeometricalSets
from pycatia3dx.mmr_automation_interfaces.shapes import Shapes
from pycatia3dx.mmr_automation_interfaces.sketches import Sketches
from pycatia3dx.system.any_object import AnyObject


class Body(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     Body
                | 
                | The object that manages a sequence of shapes, a set of sketches, a set of
                | hybrid bodies, a set of ordered geometrical sets and a set of hybrid
                | shapes.
                | 
                | It belongs to the Bodies collection of a Part or HybridBody
                | object.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def hybrid_bodies(self) -> HybridBodies:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Property HybridBodies() As HybridBodies (Read Only)
                |     Returns the body's HybridBodies collection.
                | 
                |     Example:
                |         The following example returns in hybridBodyColl the collection of
                |         hybrid bodies of the main body of the 3D shape:
                | 
                |          Set editor = CATIA.ActiveEditor
                |          Set part = editor.ActiveObject
                |          Dim body As Body
                |          Set body = part.Bodies.MainBody
                |          Set hybridBodyColl = body.HybridBodies

        :return: HybridBodies
        """

        return HybridBodies(self.com_object.HybridBodies)

    @property
    def hybrid_shapes(self) -> HybridShapes:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Property HybridShapes() As HybridShapes (Read Only)
                |     Returns the list of hybrid shapes included in the body.
                | 
                |     Returns:
                |         oHybridShapes The list of hybrid shapes in the body (@see
                |         CATIAHybridShapes
                |         for more information).
                | 
                |         Example:
                |             The following example returns in HybridShapes1 the list
                |             of
                |             hybrid shapes in the body Body1:
                | 
                |              Dim HybridShapes1 As HybridShapes
                |              Set HybridShapes1 = Body1.HybridShapes

        :return: HybridShapes
        """

        return HybridShapes(self.com_object.HybridShapes)

    @property
    def in_boolean_operation(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Property InBooleanOperation() As boolean (Read Only)
                |     Returns True if the body is involved in a boolean operation, else returns
                |     False.
                | 
                |     Example:
                |         The following example returns in operated True if the body body1belongs
                |         to a boolean operation.
                | 
                |          operated = body1.InBooleanOperation

        :return: bool
        """

        return self.com_object.InBooleanOperation

    @property
    def ordered_geometrical_sets(self) -> OrderedGeometricalSets:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Property OrderedGeometricalSets() As OrderedGeometricalSets (Read
                | Only)
                |     Returns the body's OrderedGeometricalSets collection.
                | 
                |     ometricalSetColl = Body1.OrderedGeometricalSets Example:
                |         The following example returns in OrderedGeometricalSetColl the
                |         collection of ordered geometrical set of the body Body1
                |         :
                | 
                |          Dim OrderedGeometricalSets1 As OrderedGeometricalSets
                |          Set OrderedGeometricalSets1 = Body1.OrderedGeometricalSets

        :return: OrderedGeometricalSets
        """

        return OrderedGeometricalSets(self.com_object.OrderedGeometricalSets)

    @property
    def shapes(self) -> Shapes:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Property Shapes() As Shapes (Read Only)
                |     Returns the body's Shapes collection. These shapes make up the sequence of
                |     shapes that will produce an intermediate result for the part, or the final
                |     result in the case of the main body.
                | 
                |     Example:
                |         The following example returns in shapColl the collection of shapes
                |         managed by the main body of the active 3D shape:
                | 
                |          Set editor = CATIA.ActiveEditor
                |          Set part = editor.ActiveObject
                |          Dim body As Body
                |          Set body = part.Bodies.MainBody
                |          Set shapColl = body.Shapes

        :return: Shapes
        """

        return Shapes(self.com_object.Shapes)

    @property
    def sketches(self) -> Sketches:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Property Sketches() As Sketches (Read Only)
                |     Returns the body's Sketches collection. These sketches are those inside the
                |     body at all levels.
                | 
                |     Example:
                |         The following example returns in skColl the collection of sketches of
                |         the main body of the 3D shape:
                | 
                |          Set editor = CATIA.ActiveEditor
                |          Set part = editor.ActiveObject
                |          Dim body As Body
                |          Set body = part.Bodies.MainBody
                |          Set skColl = body.Sketches

        :return: Sketches
        """

        return Sketches(self.com_object.Sketches)

    def insert_hybrid_shape(self, i_hybrid_shape: HybridShape) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Sub InsertHybridShape(HybridShape iHybridShape)
                |     Insert a hybrid shape to the body.
                | 
                |     Parameters:
                | 
                |         iHybriShape
                |             The hybrid shape to insert. 
                | 
                |     Example:
                |         This example inserts the hybrid shape HybridShape1 to the body
                |         Body1:
                | 
                |          Body1.InsertHybridShape (HybridShape1)

        :param HybridShape i_hybrid_shape:
        :return: None
        """
        return self.com_object.InsertHybridShape(i_hybrid_shape.com_object)

    def __repr__(self):
        return f'Body(name="{ self.name }")'
