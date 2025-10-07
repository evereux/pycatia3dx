"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.knowledge_interfaces.real_param import RealParam
from pycatia3dx.mode.reference import Reference
from pycatia3dx.todo_part.dress_up_shape import DressUpShape


class Scaling(DressUpShape):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     CATMmrAutomationInterfaces.Shape
                |                         CATPartIDLItf.DressUpShape
                |                             Scaling
                | 
                | Represents the scaling shape.
                | The scaling shape is made up of a scaling reference element, such as a point,
                | and a scaling factor.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def factor(self) -> RealParam:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Factor() As RealParam (Read Only)
                |     Returns the scaling factor.
                | 
                |     Example:
                |         The following example returns in factor the scaling factor of the
                |         scaling firstScaling:
                | 
                |          Set factor = firstScaling.Factor

        :return: RealParam
        """

        return RealParam(self.com_object.Factor)

    @property
    def scaling_reference(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ScalingReference() As Reference
                |     Returns or sets the scaling reference element. It can be a
                |     point.
                |     To set the property, you can use one of the following Boundary objects:
                |     PlanarFace or Vertex.
                | 
                |     Example:
                |         The following example returns in ref the scaling reference element of
                |         the scaling firstScaling, and then sets it to the created
                |         MyRef:
                | 
                |          Set ref = firstScaling.ScalingSupport
                |          Set MyRef = part.CreateReferenceFromGeometry (Point)
                |          firstScaling.ScalingSupport = MyRef

        :return: Reference
        """

        return Reference(self.com_object.ScalingReference)

    @scaling_reference.setter
    def scaling_reference(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.ScalingReference = value

    def __repr__(self):
        return f'Scaling(name="{ self.name }")'
