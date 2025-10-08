"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from typing import TYPE_CHECKING

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.tps.user_surface import UserSurface
from pycatia3dx.types.general import CATVariant

if TYPE_CHECKING:
    from pycatia3dx.tps.annotations import Annotations


class ReferenceFrame(AnyObject):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ReferenceFrame
                | 
                | Interface designed to manage reference frame associated to a
                | TPS.
                | Reference frame is composed of three boxes.
                | 
                |                          Reference Frame
                |                         / 
                |                   _____|_____
                |                  /           \
                |          ---------------------
                |          |   |   |Box|Box|Box|
                |          |   |   | 1 | 2 | 3 |
                |          ---------------------
                |
                |  Property Index
                |
                |     AllDatumsSimple
                | 	  Retrieves all datums simple used in Reference Frame.
                |  
                |  Method Index
                |
                |     Frame
                | 	  Retrieves Frame of the TPS.
                |   
                |     GetAxisSystemTTRS
                | 	  Gets the AxisSystem TTRS.
                |   
                |     GetDegreesOfFreedom
                | 	  Retrieves the values of Degrees Of Freedom(DOF)
                | [x,y,z,u,v,w].
                |   
                |     SetAxisSystemTTRS
                | 	  Sets the AxisSystem TTRS.
                |   
                |     SetDegreesOfFreedom
                | 	  Sets the values of Degrees Of Freedom(DOF) [x,y,z,u,v,w].
                |   
                |     SetFrame
                | 	  Set Frame of the TPS.
                |
                | Properties
                |
                | Property AllDatumsSimple() As Annotations  (Read Only)
                |      Retrieves all datums simple used in Reference Frame.
                |      Parameters:
                |          opiListDatumsSimple
                |                  All objects of the collection
                |
                | Methods
                |
                | Sub Frame(CATBSTR oFirstBox,CATBSTR oSecondBox,CATBSTR
                | oThirdBox)
                |      Retrieves Frame of the TPS.
                |      Parameters:
                |          oFirstBox
                |          oSecondBox
                |          oThirdBox
                |                  Texts in first, second and third boxes.
                |
                | Sub GetAxisSystemTTRS(UserSurface opAxisSystemTTRS)
                |      Gets the AxisSystem TTRS.
                |      Parameters:
                |          opAxisSystemTTRS
                |                AxisSystem TTRS
                |      Returns:
                |           HRESULT   S_OK:- the Axis System has been correctly
                |           retrieved.
                |            E_FAIL or E_NOIMPL : Axis System cannot be retrieved.
                |
                | Sub GetDegreesOfFreedom(CATVariant inBox,CATBSTR oValue)
                |      Retrieves the values of Degrees Of Freedom(DOF)
                |      [x,y,z,u,v,w].
                |      Is only defined when "Axis System" attribute is valued.
                |      Only for ASME 2009 (does not exist in ISO).
                |      Parameters:
                |          inBox
                |                First, Second or the Third Box of the DRF on
                |                which
                |                the Degrees Of Freedom is to be retrieved.
                |          oValue
                |                oValue begins with the symbol :"[" and ends by the symbol
                |                "]".
                |                and between these symbols "[..]", value are a a combination
                |                of
                |                following legal values:
                |                x,
                |                y,
                |                z,
                |                u,
                |                v,
                |                w
                |      Returns:
                |           HRESULT    S_OK : the Degrees Of Freedom has been correctly retrieved.
                |             E_FAIL or E_NOIMPL : the Degrees Of Freedom cannot be retrieved.
                |          
                | Sub SetAxisSystemTTRS(UserSurface ipAxisSystemTTRS)
                |      Sets the AxisSystem TTRS.
                |      Parameters:
                |          ipAxisSystemTTRS
                |                AxisSystem TTRS. If it is NULL, the AxisSystem TTRS in the
                |                model
                |                will be removed.
                |      Returns:
                |           HRESULT   S_OK:- the Axis System has been correctly
                |           set.
                |            E_FAIL or E_NOIMPL : Axis System cannot be set.
                |          
                | Sub SetDegreesOfFreedom(CATVariant inBox,CATBSTR iValue)
                |      Sets the values of Degrees Of Freedom(DOF) [x,y,z,u,v,w].
                |      Is only defined when "Axis System" attribute is valued.
                |      Only for ASME 2009 (does not exist in ISO).
                |      Parameters:
                |          inBox
                |                First, Second or the Third Box of the DRF on
                |                which
                |                the Degrees Of Freedom is to be set.
                |          iValue
                |                iValue must begin by the symbol :"[" and must end by the symbol
                |                "]".
                |                and between these symbols "[..]", value must be a combination
                |                of
                |                following legal values:
                |                x,
                |                y,
                |                z,
                |                u,
                |                v,
                |                w
                |                E.G.1:- To set [x,z] as the DOF:-
                |                               iValue = [x,z];
                |                E.G.2:- To set [y] as the DOF:-
                |                               iValue = [y];
                |      Returns:
                |           HRESULT    S_OK : the Degrees Of Freedom has been correctly set.
                |             E_FAIL or E_NOIMPL : the Degrees Of Freedom cannot be set.
                |          
                | Sub SetFrame(CATBSTR iFirstBox,CATBSTR iSecondBox,CATBSTR
                | iThirdBox)
                |      Set Frame of the TPS.
                |      Parameters:
                |          oFirstBox
                |          oSecondBox
                |          oThirdBox
                |                  Texts in first, second and third boxes.

    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def all_datums_simple(self) -> 'Annotations':
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property AllDatumsSimple() As Annotations  (Read Only)
                |
                |      Retrieves all datums simple used in Reference Frame.
                |
                |      Parameters:
                |          opiListDatumsSimple
                |                  All objects of the collection

        :return: Annotations
        """
        from pycatia3dx.tps.annotations import Annotations
        return Annotations(self.com_object.AllDatumsSimple)

    def frame(self, o_first_box: str, o_second_box: str, o_third_box: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Frame(CATBSTR oFirstBox,CATBSTR oSecondBox,CATBSTR
                | oThirdBox)
                |
                |      Retrieves Frame of the TPS.
                |
                |      Parameters:
                |          oFirstBox
                |          oSecondBox
                |          oThirdBox
                |                  Texts in first, second and third boxes.

        :param str o_first_box:
        :param str o_second_box:
        :param str o_third_box:
        :return: None
        """
        return self.com_object.Frame(o_first_box, o_second_box, o_third_box)

    def get_axis_system_ttrs(self, op_axis_system_ttrs: UserSurface) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetAxisSystemTTRS(UserSurface opAxisSystemTTRS)
                |
                |      Gets the AxisSystem TTRS.
                |
                |      Parameters:
                |          opAxisSystemTTRS
                |                AxisSystem TTRS
                |      Returns:
                |           HRESULT   S_OK:- the Axis System has been correctly
                |           retrieved.
                |            E_FAIL or E_NOIMPL : Axis System cannot be retrieved.

        :param UserSurface op_axis_system_ttrs:
        :return: None
        """
        return self.com_object.GetAxisSystemTTRS(op_axis_system_ttrs.com_object)

    def get_degrees_of_freedom(self, in_box: CATVariant, o_value: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetDegreesOfFreedom(CATVariant inBox,CATBSTR oValue)
                |
                |      Retrieves the values of Degrees Of Freedom(DOF)
                |      [x,y,z,u,v,w].
                |      Is only defined when "Axis System" attribute is valued.
                |      Only for ASME 2009 (does not exist in ISO).
                |
                |      Parameters:
                |          inBox
                |                First, Second or the Third Box of the DRF on
                |                which
                |                the Degrees Of Freedom is to be retrieved.
                |          oValue
                |                oValue begins with the symbol :"[" and ends by the symbol
                |                "]".
                |                and between these symbols "[..]", value are a a combination
                |                of
                |                following legal values:
                |                x,
                |                y,
                |                z,
                |                u,
                |                v,
                |                w
                |               
                |      Returns:
                |           HRESULT    S_OK : the Degrees Of Freedom has been correctly retrieved.
                |             E_FAIL or E_NOIMPL : the Degrees Of Freedom cannot be retrieved.

        :param CATVariant in_box:
        :param str o_value:
        :return: None
        """
        return self.com_object.GetDegreesOfFreedom(in_box, o_value)

    def set_axis_system_ttrs(self, ip_axis_system_ttrs: UserSurface) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetAxisSystemTTRS(UserSurface ipAxisSystemTTRS)
                |
                |      Sets the AxisSystem TTRS.
                |       
                |      Parameters:
                |          ipAxisSystemTTRS
                |                AxisSystem TTRS. If it is NULL, the AxisSystem TTRS in the
                |                model
                |                will be removed.
                |      Returns:
                |           HRESULT   S_OK:- the Axis System has been correctly
                |           set.
                |            E_FAIL or E_NOIMPL : Axis System cannot be set.

        :param UserSurface ip_axis_system_ttrs:
        :return: None
        """
        return self.com_object.SetAxisSystemTTRS(ip_axis_system_ttrs.com_object)

    def set_degrees_of_freedom(self, in_box: CATVariant, i_value: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetDegreesOfFreedom(CATVariant inBox,CATBSTR iValue)
                |
                |      Sets the values of Degrees Of Freedom(DOF) [x,y,z,u,v,w].
                |      Is only defined when "Axis System" attribute is valued.
                |      Only for ASME 2009 (does not exist in ISO).
                |       
                |      Parameters:
                |          inBox
                |                First, Second or the Third Box of the DRF on
                |                which
                |                the Degrees Of Freedom is to be set.
                |          iValue
                |                iValue must begin by the symbol :"[" and must end by the symbol
                |                "]".
                |                and between these symbols "[..]", value must be a combination
                |                of
                |                following legal values:
                |                x,
                |                y,
                |                z,
                |                u,
                |                v,
                |                w
                |                E.G.1:- To set [x,z] as the DOF:-
                |                               iValue = [x,z];
                |                E.G.2:- To set [y] as the DOF:-
                |                               iValue = [y];
                |
                |      Returns: 
                |           HRESULT    S_OK : the Degrees Of Freedom has been correctly set.
                |             E_FAIL or E_NOIMPL : the Degrees Of Freedom cannot be set.

        :param CATVariant in_box:
        :param str i_value:
        :return: None
        """
        return self.com_object.SetDegreesOfFreedom(in_box, i_value)

    def set_frame(self, i_first_box: str, i_second_box: str, i_third_box: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetFrame(CATBSTR iFirstBox,CATBSTR iSecondBox,CATBSTR
                | iThirdBox)
                |
                |      Set Frame of the TPS.
                |        
                |      Parameters:
                |          oFirstBox
                |          oSecondBox
                |          oThirdBox
                |                  Texts in first, second and third boxes.

        :param str i_first_box:
        :param str i_second_box:
        :param str i_third_box:
        :return: None
        """
        return self.com_object.SetFrame(i_first_box, i_second_box, i_third_box)

    def __repr__(self):
        return f'ReferenceFrame(name="{self.name}")'
