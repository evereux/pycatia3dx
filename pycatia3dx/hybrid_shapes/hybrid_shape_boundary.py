"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 14:29:47.477239

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.mmr_automation_interfaces.hybrid_shape import HybridShape
from pycatia3dx.mode.reference import Reference


class HybridShapeBoundary(HybridShape):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     CATMmrAutomationInterfaces.HybridShape
                |                         HybridShapeBoundary
                | 
                | Represents the hybrid shape boundary feature object.
                | Role: To access the data of the hybrid shape boundary feature object. This data
                | includes:
                | 
                |     The boundary propagation
                |     The initial element used for the boundary propagation
                |     The boundary support
                | 
                | Use the CATIAHybridShapeFactory to create a HybridShapeBoundary
                | object.
                | 
                | See also:
                |     HybridShapeFactory
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def from_(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property From() As Reference
                |     Removes or sets the ending limit(i.e Limit2) of the boundary

        :return: Reference
        """

        return Reference(self.com_object.From)

    @from_.setter
    def from_(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.From = value

    @property
    def from_orientation(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property FromOrientation() As long
                |     Gets or sets the Ending Limit Orientation (i.e same or inverse)

        :return: int
        """

        return self.com_object.FromOrientation

    @from_orientation.setter
    def from_orientation(self, value: int):
        """
        :param int value:
        """

        self.com_object.FromOrientation = value

    @property
    def initial_element(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property InitialElement() As Reference
                |     Returns or sets the element used to initialize the boundary
                |     propagation.
                |     Sub-element(s) supported (see Boundary object):
                |     BiDimFeatEdge.
                | 
                |     Example:
                |         This example retrieves in InitElem the initial element of the
                |         ShpBoundary hybrid shape boundary feature.
                | 
                |          Dim InitElem As Reference
                |          InitElem = ShpBoundary.InitialElement

        :return: Reference
        """

        return Reference(self.com_object.InitialElement)

    @initial_element.setter
    def initial_element(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.InitialElement = value

    @property
    def propagation(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Propagation() As long
                |     Returns or sets the boundary propagation.
                |     Legal values: xxxxxxxxxx
                | 
                |     Example:
                |         This example retrieves in Prop the boundary propagation of the
                |         ShpBoundary hybrid shape boundary feature.
                | 
                |          Prop = ShpBoundary.Propagation

        :return: int
        """

        return self.com_object.Propagation

    @propagation.setter
    def propagation(self, value: int):
        """
        :param int value:
        """

        self.com_object.Propagation = value

    @property
    def support(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Support() As Reference
                |     Returns or sets the support surface around which the boundary is
                |     computed.
                |     Sub-element(s) supported (see Boundary object): Face.
                | 
                |     Example:
                |         This example retrieves in SupSurf the initial element of the
                |         ShpBoundary hybrid shape boundary feature.
                | 
                |          Dim SupSurf As Reference
                |          SupSurf = ShpBoundary.Support

        :return: Reference
        """

        return Reference(self.com_object.Support)

    @support.setter
    def support(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.Support = value

    @property
    def to(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property To() As Reference
                |     Removes or sets the starting limit(i.e Limit1) of the boundary

        :return: Reference
        """

        return Reference(self.com_object.To)

    @to.setter
    def to(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.To = value

    @property
    def to_orientation(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property ToOrientation() As long
                |     Gets or sets the Starting Limit Orientation (i.e same or inverse)

        :return: int
        """

        return self.com_object.ToOrientation

    @to_orientation.setter
    def to_orientation(self, value: int):
        """
        :param int value:
        """

        self.com_object.ToOrientation = value

    def __repr__(self):
        return f'HybridShapeBoundary(name="{ self.name }")'
