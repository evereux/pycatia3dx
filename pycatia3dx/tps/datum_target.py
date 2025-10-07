"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.tps.user_surface import UserSurface


class DatumTarget(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     DatumTarget
                | 
                | Interface for Datum Target TPS (datum entity).
                | TPS for Technological Product Specifications.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def datum(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Datum() As AnyObject (Read Only)
                |     Retrieves simple datum, the target belongs to.

        :return: AnyObject
        """

        return AnyObject(self.com_object.Datum)

    @property
    def label(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Label() As CATBSTR
                |     Retrieves Label.

        :return: str
        """

        return self.com_object.Label

    @label.setter
    def label(self, value: str):
        """
        :param str value:
        """

        self.com_object.Label = value

    def get_area_form(self, o_area_form: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetAreaForm(CATBSTR oAreaForm)
                |     Gets the form of the target area.
                | 
                |     Parameters:
                | 
                |         oAreaForm
                |             Form of the target area. Legal values are:- Point, Circular,
                |             Rectangular. 
                | 
                |     Returns:
                |         HRESULT S_OK:- the Area Form has been correctly retrieved. E_FAIL or E_NOIMPL : Area Form cannot be retrieved.

        :param str o_area_form:
        :return: None
        """
        return self.com_object.GetAreaForm(o_area_form)

    def get_circular_area_size(self, o_area_size: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetCircularAreaSize(double oAreaSize)
                |     Gets the size of the circular area.
                | 
                |     Parameters:
                | 
                |         oAreaSize
                |             Size of the Circular target area. 
                | 
                |     Returns:
                |         HRESULT S_OK:- the Area Size has been correctly retrieved. E_FAIL or E_NOIMPL : Area Size cannot be retrieved.

        :param float o_area_size:
        :return: None
        """
        return self.com_object.GetCircularAreaSize(o_area_size)

    def get_movable_direction_ttrs(self, op_direction_ttrs: UserSurface) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetMovableDirectionTTRS(UserSurface opDirectionTTRS)
                |     Gets the movable Direction TTRS.
                | 
                |     Parameters:
                | 
                |         ospDirectionTTRS
                |             Movable Direction TTRS 
                | 
                |     Returns:
                |         HRESULT S_OK:- the movable direction has been correctly retrieved. E_FAIL or E_NOIMPL : movable direction cannot be retrieved.

        :param UserSurface op_direction_ttrs:
        :return: None
        """
        return self.com_object.GetMovableDirectionTTRS(op_direction_ttrs.com_object)

    def get_rectangular_area_size(self, o_length: float, o_width: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetRectangularAreaSize(double oLength,double oWidth)
                |     Gets the size of the rectangular area.
                | 
                |     Parameters:
                | 
                |         oLength
                |             Length of the Rectangular target area. 
                |         oWidth
                |             Width of the Rectangular target area. 
                | 
                |     Returns:
                |         HRESULT S_OK:- the Area Size has been correctly retrieved. E_FAIL or E_NOIMPL : Area Size cannot be retrieved.

        :param float o_length:
        :param float o_width:
        :return: None
        """
        return self.com_object.GetRectangularAreaSize(o_length, o_width)

    def set_area_form(self, i_area_form: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetAreaForm(CATBSTR iAreaForm)
                |     Sets the form of the target area.
                | 
                |     Parameters:
                | 
                |         iAreaForm
                |             Form of the target area. Legal values are:- Point, Circular,
                |             Rectangular. 
                | 
                |     Returns:
                |         HRESULT S_OK:- the Area Form has been correctly set. E_FAIL or E_NOIMPL : Area Form cannot be set.

        :param str i_area_form:
        :return: None
        """
        return self.com_object.SetAreaForm(i_area_form)

    def set_circular_area_size(self, i_area_size: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetCircularAreaSize(double iAreaSize)
                |     Sets the size of the circular area.
                | 
                |     Parameters:
                | 
                |         iAreaSize
                |             Size of the Circular target area. 
                | 
                |     Returns:
                |         HRESULT S_OK:- the Area Size has been correctly set. E_FAIL or E_NOIMPL : Area Size cannot be set.

        :param float i_area_size:
        :return: None
        """
        return self.com_object.SetCircularAreaSize(i_area_size)

    def set_movable_direction_ttrs(self, ip_direction_ttrs: UserSurface) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetMovableDirectionTTRS(UserSurface ipDirectionTTRS)
                |     Sets the movable Direction TTRS.
                | 
                |     Parameters:
                | 
                |         ispDirectionTTRS
                |             Movable Direction TTRS If the ipDirectionTTRS is NULL_var, the
                |             direction TTRS inside the model is removed. 
                | 
                |     Returns:
                |         HRESULT S_OK:- the movable direction has been correctly set. E_FAIL or E_NOIMPL : movable direction cannot be set.

        :param UserSurface ip_direction_ttrs:
        :return: None
        """
        return self.com_object.SetMovableDirectionTTRS(ip_direction_ttrs.com_object)

    def set_rectangular_area_size(self, i_length: float, i_width: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetRectangularAreaSize(double iLength,double iWidth)
                |     Sets the size of the rectangular area.
                | 
                |     Parameters:
                | 
                |         iLength
                |             Length of the Rectangular target area. 
                |         iWidth
                |             Width of the Rectangular target area. 
                | 
                |     Returns:
                |         HRESULT S_OK:- the Area Size has been correctly set. E_FAIL or E_NOIMPL : Area Size cannot be set. 

        :param float i_length:
        :param float i_width:
        :return: None
        """
        return self.com_object.SetRectangularAreaSize(i_length, i_width)

    def __repr__(self):
        return f'DatumTarget(name="{ self.name }")'
