"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 14:29:47.477239

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.knowledge_interfaces.length import Length
from pycatia3dx.mmr_automation_interfaces.hybrid_shape import HybridShape
from pycatia3dx.mode.reference import Reference


class HybridShapeIntegratedLaw(HybridShape):

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
                |                         HybridShapeIntegratedLaw
                | 
                | Represents the hybrid shape "integrated" law feature object.
                | Role: To access the data of the hybrid shape "integrated" law feature
                | object.
                | 
                | Use the CATIAHybridShapeFactory to create a HybridShapeIntegratedLaw
                | object.
                | 
                | See also:
                |     HybridShapeFactory.AddNewIntegratedLaw
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def advanced_law(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property AdvancedLaw() As Reference
                |     Gets or sets the external law.
                |     Note: Used for law type = 4(Advanced)
                | 
                |     Parameters:
                | 
                |         AdvancedLaw
                |             External Law This example retrieves in ALaw the external law for
                |             the IntegratedLaw hybrid shape feature.
                | 
                |              Dim ALaw
                |              Set ALaw = IntegratedLaw.AdvancedLaw

        :return: Reference
        """

        return Reference(self.com_object.AdvancedLaw)

    @advanced_law.setter
    def advanced_law(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.AdvancedLaw = value

    @property
    def end_param(self) -> Length:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property EndParam() As Length (Read Only)
                |     Gets end parameter.
                |     Note: Used for law type = 2(Linear) and 3(SType).
                | 
                |     Parameters:
                | 
                |         EndParam
                |             Parameter This example retrieves in EParam the end parameter for
                |             the IntegratedLaw hybrid shape feature.
                | 
                |              Dim EParam
                |              Set EParam = IntegratedLaw.EndParam

        :return: Length
        """

        return Length(self.com_object.EndParam)

    @property
    def implicit_law_interpolation_mode(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property ImplicitLawInterpolationMode() As long
                |     Gets or sets Interpolation mode for implicit law.
                |     Note: Used for law type = 5(Implicit)
                | 
                |     Parameters:
                | 
                |         ImplicitLawInterpolationMode
                |             Implicit law interpolation mode ImplicitLawInterpolationMode = 0 : CATGSMImplicitLawInterpo_None = 1 : CATGSMImplicitLawInterpo_Linear = 2 : CATGSMImplicitLawInterpo_Cubic This example retrieves in InterpolLawMode the Interpolation mode for the IntegratedLaw hybrid shape feature.
                | 
                |              Dim InterpolLawMode
                |              Set InterpolLawMode = IntegratedLaw.ImplicitLawInterpolationMode

        :return: int
        """

        return self.com_object.ImplicitLawInterpolationMode

    @implicit_law_interpolation_mode.setter
    def implicit_law_interpolation_mode(self, value: int):
        """
        :param int value:
        """

        self.com_object.ImplicitLawInterpolationMode = value

    @property
    def invert_mapping_law(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property InvertMappingLaw() As boolean
                |     Gets or sets the mapping orientation of the law.
                | 
                |     Parameters:
                | 
                |         InvertMappingLaw
                |             False : Law is applied from the beginning to the end of the curve (mapping is not inverted).
                |             True : Law is applied from the end to the beginning of the curve (mapping is inverted). This example retrieves in IMappingLaw the mapping orientation of the law for the IntegratedLaw hybrid shape feature.
                | 
                |              Dim IMappingLaw
                |              Set IMappingLaw = IntegratedLaw.InvertMappingLaw

        :return: bool
        """

        return self.com_object.InvertMappingLaw

    @invert_mapping_law.setter
    def invert_mapping_law(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.InvertMappingLaw = value

    @property
    def pitch_law_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property PitchLawType() As long
                |     Gets or sets pitch law type.
                | 
                |     Parameters:
                | 
                |         PitchLawType
                |             Type of law PitchLawType = 0 : None = 1 : Constant = 2 : Linear = 3 : SType = 4 : Advanced = 5 : Implicit This example retrieves in PLawType the pitch law type for the IntegratedLaw hybrid shape feature.
                | 
                |              Dim PLawType
                |              Set PLawType = IntegratedLaw.PitchLawType

        :return: int
        """

        return self.com_object.PitchLawType

    @pitch_law_type.setter
    def pitch_law_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.PitchLawType = value

    @property
    def spine(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Spine() As Reference
                |     Gets or sets Spine for implicit law.
                |     Note: Used for law type = 5 (Implicit)
                | 
                |     Parameters:
                | 
                |         Spine
                |             Spine on which implicit law inputs points are defined This example
                |             retrieves in Spine1 the spine for the IntegratedLaw hybrid shape
                |             feature.
                | 
                |              Dim Spine1
                |              Set Spine1 = IntegratedLaw.Spine

        :return: Reference
        """

        return Reference(self.com_object.Spine)

    @spine.setter
    def spine(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.Spine = value

    @property
    def start_param(self) -> Length:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property StartParam() As Length (Read Only)
                |     Gets start parameter.
                |     Note: Used for law type = 1(Constant) ,2(Linear) and 3(SType)
                | 
                |     Parameters:
                | 
                |         StartParam
                |             Parameter This example retrieves in SParam the start parameter for
                |             the IntegratedLaw hybrid shape feature.
                | 
                |              Dim SParam
                |              Set SParam = IntegratedLaw.StartParam

        :return: Length
        """

        return Length(self.com_object.StartParam)

    def append_new_point_and_param(self, i_point: Reference, i_param: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub AppendNewPointAndParam(Reference iPoint,long iParam)
                |     Sets 'Point on spine' and associated parameter.
                |     Note: Used for law type = 5(Implicit)
                | 
                |     Parameters:
                | 
                |         iPoint
                |             Point on spine 
                |         iParam
                |             Corresponding parameter

        :param Reference i_point:
        :param int i_param:
        :return: None
        """
        return self.com_object.AppendNewPointAndParam(i_point.com_object, i_param)

    def get_point_and_param(self, i_pos: int, o_point: Reference, o_param: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub GetPointAndParam(long iPos,Reference oPoint,Reference
                | oParam)
                |     Gets the point on spine and associated parameter at a given
                |     position.
                |     Note: Used for law type = 5(Implicit)
                | 
                |     Parameters:
                | 
                |         iPos
                |             given position 
                |         oPoint
                |             point on spine 
                |         oParam
                |             corresponding parameter

        :param int i_pos:
        :param Reference o_point:
        :param Reference o_param:
        :return: None
        """
        return self.com_object.GetPointAndParam(i_pos, o_point.com_object, o_param.com_object)

    def get_size(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Func GetSize() As long
                |     Gets the size of the list in the law i.e. number of points in the list of
                |     the law.
                | 
                |     Parameters:
                | 
                |         oSize
                |             size of the list.

        :return: int
        """
        return self.com_object.GetSize()

    def remove_all_points_and_params(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub RemoveAllPointsAndParams()
                |     Removes all the points and associated parameters.
                |     Note: Used for law type = 5(Implicit)

        :return: None
        """
        return self.com_object.RemoveAllPointsAndParams()

    def remove_point_and_param(self, i_point: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub RemovePointAndParam(Reference iPoint)
                |     Removes a point and its parameter. for law type = 5(Implicit)
                | 
                |     Parameters:
                | 
                |         iSpecPoint
                |             Point to remove

        :param Reference i_point:
        :return: None
        """
        return self.com_object.RemovePointAndParam(i_point.com_object)

    def set_end_param(self, i_end_param: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub SetEndParam(long iEndParam)
                |     Sets end parameter.
                |     Note: Used for law type = 2(Linear) and 3(SType).
                | 
                |     Parameters:
                | 
                |         iEndParam
                |             Parameter

        :param int i_end_param:
        :return: None
        """
        return self.com_object.SetEndParam(i_end_param)

    def set_start_param(self, i_start_param: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub SetStartParam(long iStartParam)
                |     Sets start parameter.
                |     Note: Used for law type = 1(Constant) ,2(Linear) and 3(SType).
                | 
                |     Parameters:
                | 
                |         iStartParam
                |             Parameter

        :param int i_start_param:
        :return: None
        """
        return self.com_object.SetStartParam(i_start_param)

    def __repr__(self):
        return f'HybridShapeIntegratedLaw(name="{ self.name }")'
