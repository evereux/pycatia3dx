"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class VSOMorphing(AnyObject):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     VSOMorphing
                | 
                | Interface representing a RSO Morphing feature.
                | 
                | Role: Components that implement CATIAVSOMorphing are Virtual to Real Shape
                | Morphind features. This interface allows adding new vector fields as input
                | morphing laws.
                | 
                | ClassReference, Class#MethodReference, #InternalMethod...
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def add_vector_field(self, i_vector_field: AnyObject, i_scale: float, i_copy_vector_field_as_result: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub AddVectorField(AnyObject iVectorField,double iScale,boolean
                | iCopyVectorFieldAsResult)

        :param AnyObject i_vector_field:
        :param float i_scale:
        :param bool i_copy_vector_field_as_result:
        :return: None
        """
        return self.com_object.AddVectorField(i_vector_field.com_object, i_scale, i_copy_vector_field_as_result)

    def __repr__(self):
        return f'VsoMorphing(name="{self.name}")'
