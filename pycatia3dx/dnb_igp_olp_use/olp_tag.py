"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.types.general import CATVariant


class OLPTag(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     OlpTag
                | 
                | A named Cartesian target of a robot motion.
                | 
                | This object represents any Cartesian target of a robot motion that can be given
                | a name and be reused on multiple motions. This could be a tag or a
                | manufacturing fastener. This interface can only be used by a translator within
                | the Robotics Off-line Programming (OLP) Download or Upload
                | command.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def design_fastener(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property DesignFastener() As CATBaseDispatch (Read Only)
                |     Get the design fastener.
                |     This object is only available during download. The design fastener is the
                |     entity that represents the process point in the design product data. The object
                |     returned is the fastener occurrence from the product DAG (EBOM). From the
                |     occurrence you can retrieve the reference and then use PLMEntity to access any
                |     attributes of the fastener.

        :return: AnyObject
        """

        return AnyObject(self.com_object.DesignFastener)

    @property
    def manufacturing_fastener(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ManufacturingFastener() As CATBaseDispatch (Read
                | Only)
                |     Get the manufacturing fastener.
                |     This object is only available during download. In most cases you should use
                |     the GetParameter method of this object to get parameters from the manufacturing
                |     fastener. In cases where you need additional functionality, the manufacturing
                |     fastener is the entity in the resource structure that represents the process
                |     point. Depending on the application this could be a spot weld fastener, a drill
                |     and rivet manufacturing fastener or some type of tag. It can be used to
                |     retrieve process attributes directly from the fastener to customize the
                |     download. Depending on the application you can use one of these interfaces or
                |     perhaps a different one to access the object properties:
                |     DrManufacturingFastener, TagPoint

        :return: AnyObject
        """

        return AnyObject(self.com_object.ManufacturingFastener)

    @property
    def parameter_names(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ParameterNames() As CATSafeArrayVariant (Read Only)
                |     Get the list of all parameter names.
                |     Retrieve the list of all parameter names that can be retrieved with
                |     OlpTag.GetParameter. You can add new attributes by calling OlpTag.SetParameter.

        :return: tuple
        """

        return self.com_object.ParameterNames

    def get_parameter(self, i_parameter_name: str) -> CATVariant:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetParameter(CATBSTR iParameterName) As CATVariant
                |     Get the specified tag or manufacturing fastener attribute
                |     value.
                |     For tags, the value displayed in the trajectory table is retrieved from
                |     either the tag or tag group as appropriate. For manufacturing fasteners, the
                |     values displayed in the properties dialog can be retrieved including standard
                |     and user parameters.
                | 
                |     Parameters:
                | 
                |         iParameterName
                |             The name of the parameter. 
                |         oValue
                |             The value of the parameter.

        :param str i_parameter_name:
        :return: CATVariant
        """
        return self.com_object.GetParameter(i_parameter_name)

    def set_parameter(self, i_parameter_name: str, i_value: CATVariant, i_type: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetParameter(CATBSTR iParameterName,CATVariant iValue,CATBSTR
                | iType)
                |     Set the specified tag or manufacturing fastener attribute
                |     value.
                |     The attribute is created with the specified type if it doesn't
                |     exist.
                | 
                |     Parameters:
                | 
                |         iParameterName
                |             The name of the parameter. 
                |         oValue
                |             The value of the parameter. 
                |         iType
                |             iType can be any Knowledgeware magnitude or a simple type. The
                |             simple types are "Integer", "Double", "String" and "Boolean". The method will
                |             fail if an unsupported type is specified. For tags "Length", "Angle", "Time"
                |             and "Mass" are supported. For manufacturing fasteners only "Length" and "Angle"
                |             are supported. 

        :param str i_parameter_name:
        :param CATVariant i_value:
        :param str i_type:
        :return: None
        """
        return self.com_object.SetParameter(i_parameter_name, i_value, i_type)

    def __repr__(self):
        return f'OLPTag(name="{ self.name }")'
