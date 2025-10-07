"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.mode.reference import Reference
from pycatia3dx.part.transformation_shape import TransformationShape
from pycatia3dx.system.any_object import AnyObject


class Mirror(TransformationShape):

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
                |                         CATPartIDLItf.TransformationShape
                |                             Mirror
                | 
                | Represents the mirror shape.
                | It duplicates a shape with respect to a planar mirroring element, such as a
                | planar face or a plane.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def design_intent(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property DesignIntent() As double
                |     Returns or sets the Design Intent attribute of the mirror feature. Set is
                |     called when the value of Keep Specifications check button is changed or based
                |     on the type of object to mirror Parm oDsgInt - Returns the value in the model
                |     Parm iDsgInt - Input value of the Design Intent to be set. Legal Values - 0 if
                |     mirror of currnt solid or as result - 1 if Mirror of list or with Keep Spec.

        :return: float
        """

        return self.com_object.DesignIntent

    @design_intent.setter
    def design_intent(self, value: float):
        """
        :param float value:
        """

        self.com_object.DesignIntent = value

    @property
    def mirroring_object(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property MirroringObject() As AnyObject (Read Only)
                |     Returns the mirroring Object.

        :return: AnyObject
        """

        return AnyObject(self.com_object.MirroringObject)

    @property
    def mirroring_plane(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property MirroringPlane() As Reference
                |     Returns or sets the mirroring reference plane. It can be a plane, or a
                |     plane face.
                |     To set the property, you can use the following Boundary object:
                |     PlanarFace.
                | 
                |     Example:
                |         The following example returns in ref the mirroring reference plane of
                |         the mirroring firstMirroring, and then sets it to the created
                |         MyRef:
                | 
                |          Set ref = firstMirroring.MirroringPlane
                |          Set MyRef = part.CreateReferenceFromGeometry (plane)
                |          firstMirroring.MirroringPlane = MyRef

        :return: Reference
        """

        return Reference(self.com_object.MirroringPlane)

    @mirroring_plane.setter
    def mirroring_plane(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.MirroringPlane = value

    def __repr__(self):
        return f'Mirror(name="{ self.name }")'
