"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class InertiaBox(AnyObject):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     InertiaBox
                | 
                | Interface representing the inertia Bounding Box of an element.
                | Get the computation mode of the results.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def get_bounding_box(self, o_bounding_box_origin: tuple, o_bounding_box_lenths: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetBoundingBox(CATSafeArrayVariant oBoundingBoxOrigin,CATSafeArrayVariant
                | oBoundingBoxLenths)
                |     Retrieves the bounding box of inertia. The compute of the bounding box is
                |     optimized taking into account the inertia principal axes and center of
                |     gravity.
                | 
                |     Parameters:
                | 
                |         oBoundingBoxOrigin
                |             The array of the bounding box origin:
                | 
                |                 oBoundingBoxOrigin(0) is the origin value with respect to the
                |                 first principal axe of inertia
                |                 oBoundingBoxOrigin(1) is the origin value with respect to the
                |                 second principal axe of inertia
                |                 oBoundingBoxOrigin(2) is the origin value with respect to the
                |                 third principal axe of inertia 
                | 
                |         oBoundingBoxLengths
                |             The array of the bounding box lengths:
                | 
                |                 oBoundingBoxLengths(0) is the length value with respect to the
                |                 first principal axe of inertia
                |                 oBoundingBoxLengths(1) is the length value with respect to the
                |                 second principal axe of inertia
                |                 oBoundingBoxLengths(2) is the length value with respect to the
                |                 third principal axe of inertia 
                | 
                |     Example:
                | 
                |             This  example  retrieves  the bounding box of
                |             theInertiaBoxElement.
                |             
                | 
                |               Set theInertiaBoxService = CATIA.ActiveEditor.GetService("InertiaBoxService")
                |               Dim theInertiaBoxElement As InertiaBox
                |               Set theInertiaBoxElement = theInertiaBoxService.GetInertiaBoxElement(theSelection)
                |               Dim theBoundingBoxOrigin(2)
                |               Dim theBoundingBoxLengths(2)
                |               theInertiaBoxElement.GetBoundingBox theBoundingBoxOrigin,
                |               theBoundingBoxLengths

        :param tuple o_bounding_box_origin:
        :param tuple o_bounding_box_lenths:
        :return: None
        """
        return self.com_object.GetBoundingBox(o_bounding_box_origin, o_bounding_box_lenths)

    def __repr__(self):
        return f'InertiaBox(name="{self.name}")'
