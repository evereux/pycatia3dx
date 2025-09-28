#! usr/bin/python3.9
"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 12:30:08.885021

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.mmr_automation_interfaces.geometric_elements import GeometricElements
from pycatia3dx.mmr_automation_interfaces.hybrid_bodies import HybridBodies
from pycatia3dx.mmr_automation_interfaces.hybrid_shape import HybridShape
from pycatia3dx.mmr_automation_interfaces.hybrid_shapes import HybridShapes
from pycatia3dx.mmr_automation_interfaces.sketches import Sketches
from pycatia3dx.system.any_object import AnyObject


class HybridBody(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     HybridBody
                | 
                | A hybrid body (VB meaning) is a non ordered geometrical set.
                | It may contain wireframe and surface elements, sketches and other non ordered
                | geometrical sets.
                | It belongs to the HybridBodies collection of a Part or @ref CATIABody or
                | HybridBody object.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def geometric_elements(self) -> GeometricElements:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Property GeometricElements() As GeometricElements (Read Only)
                |     Returns the list of geometrical elements included in the hybrid
                |     body.
                | 
                |     Returns:
                |         oGeometricElements The list of geometric elements in the hybrid body
                |         (@see CATIAGeometricElements
                |         for more information).
                | 
                |         Example:
                |             The following example returns in geometricElements the list
                |             of
                |             geometrical elements in the Hybrid body
                |             hybridBody:
                | 
                |              Dim geometricElements As GeometricElements
                |              Set geometricElements = hybridBody.GeometricElements

        :return: GeometricElements
        """

        return GeometricElements(self.com_object.GeometricElements)

    @property
    def hybrid_bodies(self) -> HybridBodies:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Property HybridBodies() As HybridBodies (Read Only)
                |     Returns the hybrid body's HybridBodies collection.
                | 
                |     Example:
                |         The following example returns in hybridBodyColl the collection of
                |         hybrid bodies of the hybrid body hybridBody :
                | 
                |          Set hybridBodyColl = hybridBody.HybridBodies

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
                |     Returns the list of hybrid shapes included in the hybrid
                |     body.
                | 
                |     Returns:
                |         oHybridShapes The list of hybrid shapes in the hybrid body (@see
                |         CATIAHybridShapes
                |         for more information).
                | 
                |         Example:
                |             The following example returns in hybridShapes the list
                |             of
                |             hybrid shapes in the hybrid body hybridBody:
                | 
                |              Dim hybridShapes As HybridShapes
                |              Set hybridShapes = hybridBody.HybridShapes

        :return: HybridShapes
        """

        return HybridShapes(self.com_object.HybridShapes)

    @property
    def hybrid_sketches(self) -> Sketches:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Property HybridSketches() As Sketches (Read Only)
                |     Returns the hybrid body's Sketches collection. These sketches are those
                |     inside the hybrid body at all levels.
                | 
                |     Example:
                |         The following example returns in skColl the collection of sketches of a
                |         hybrid body :
                | 
                |          Set skColl = hybridBody.HybridSketches

        :return: Sketches
        """

        return Sketches(self.com_object.HybridSketches)

    def append_hybrid_shape(self, i_hybrid_shape: HybridShape) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Sub AppendHybridShape(HybridShape iHybridShape)
                |     Appends a hybrid shape to the hybrid body.
                | 
                |     Parameters:
                | 
                |         iHybriShape
                |             The hybrid shape to append. 
                | 
                |     Example:
                |         This example appends the hybrid shape hybridShape to the hybrid body
                |         hybridBody:
                | 
                |          hybridBody.AppendHybridShape (hybridShape)

        :param HybridShape i_hybrid_shape:
        :return: None
        """
        return self.com_object.AppendHybridShape(i_hybrid_shape.com_object)

    def __repr__(self):
        return f'HybridBody(name="{ self.name }")'
