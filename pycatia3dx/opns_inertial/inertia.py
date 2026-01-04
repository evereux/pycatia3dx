"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from typing import cast

from pycatia3dx.system.any_object import AnyObject


class Inertia(AnyObject):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     Inertia
                | 
                | Interface representing the inertia of an element.
                | Get the computation mode of the results.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def get_area(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetArea() As double
                |     Retrieves the area.
                | 
                |     Example:
                | 
                |            This example retrieves the area of
                |            theInertiaElement.
                |            
                | 
                |              Set theInertiaService = CATIA.ActiveEditor.GetService("InertiaService")
                |              Dim theInertiaElement As Inertia
                |              Set theInertiaElement = theInertiaService.GetInertiaElement(theSelection)
                |              Dim theArea As Double
                |              theArea = theInertiaElement.GetArea

        :return: float
        """
        return self.com_object.GetArea()

    def get_cog_position(self) -> tuple[float, float, float]:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetCOGPosition(double oXCOG,double oYCOG,double oZCOG)
                |     Retrieves the position of the center of gravity.
                | 
                |     Example:
                | 
                |            This example retrieves the position of the center of gravity of
                |            theInertiaElement.
                |            
                | 
                |              Set theInertiaService = CATIA.ActiveEditor.GetService("InertiaService")
                |              Dim theInertiaElement As Inertia
                |              Set theInertiaElement = theInertiaService.GetInertiaElement(theSelection)
                |              Dim theXCOG As Double
                |              Dim theYCOG As Double
                |              Dim theZCOG As Double
                |              theInertiaElement.GetCOGPosition theXCOG, theYCOG,
                |              theZCOG

        :return: tuple[float, float, float]
        """
        vba_function_name = 'get_cog_position'
        vba_code = """
        Public Function get_cog_position(inertia)
            Dim oCoordinates (2)
            inertia.GetCOGPosition oCoordinates
            get_cog_position = oCoordinates
        End Function
        """
        system_service = self.application.system_service
        result = system_service.evaluate(vba_code, 0, vba_function_name, tuple([self.com_object]))
        return cast(tuple[int, int, int], cast(object, result))

    def get_inertia_matrix(self) -> tuple[float, ...]:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetInertiaMatrix(CATSafeArrayVariant oMatrix)
                |     Retrieves the matrix of inertia.
                | 
                |     Parameters:
                | 
                |         oMatrix
                |             The matrix of inertia array:
                | 
                |                 oMatrix(0) is the Ixx component
                |                 oMatrix(1) is the Ixy component
                |                 oMatrix(2) is the Ixz component
                |                 oMatrix(3) is the Iyx component
                |                 oMatrix(4) is the Iyy component
                |                 oMatrix(5) is the Iyz component
                |                 oMatrix(6) is the Izx component
                |                 oMatrix(7) is the Izy component
                |                 oMatrix(8) is the Izz component 
                | 
                |     Example:
                | 
                |            This example retrieves the inertia matrix of
                |            theInertiaElement.
                |            
                | 
                |              Set theInertiaService = CATIA.ActiveEditor.GetService("InertiaService")
                |              Dim theInertiaElement As Inertia
                |              Set theInertiaElement = theInertiaService.GetInertiaElement(theSelection)
                |              Dim theMatrix(8)
                |              theInertiaElement.GetInertiaMatrix theMatrix

        :return: tuple[int, ...]
        """
        vba_function_name = 'get_inertia_matrix'
        vba_code = """
        Public Function get_inertia_matrix(inertia)
            Dim oMatrix (8)
            inertia.GetInertiaMatrix oMatrix
            get_inertia_matrix = oMatrix
        End Function
        """

        system_service = self.application.system_service
        result  = system_service.evaluate(vba_code, 0, vba_function_name, tuple([self.com_object]))
        return cast(tuple[float, ...], cast(object, result))

    def get_mass(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetMass() As double
                |     Retrieves the mass.
                | 
                |     Example:
                | 
                |            This example retrieves the mass of
                |            theInertiaElement.
                |            
                | 
                |              Set theInertiaService = CATIA.ActiveEditor.GetService("InertiaService")
                |              Dim theInertiaElement As Inertia
                |              Set theInertiaElement = theInertiaService.GetInertiaElement(theSelection)
                |              Dim theMass As Double
                |              theMass = theInertiaElement.GetMass

        :return: float
        """
        return self.com_object.GetMass()

    def get_principal_axes(self) -> tuple[float, ...]:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetPrincipalAxes(CATSafeArrayVariant oAxes)
                |     Retrieves the principal axes of inertia.
                | 
                |     Parameters:
                | 
                |         oAxes
                |             The principal axes of inertia array (A1, A2 and A3 are the
                |             principal axes of inertia):
                | 
                |                 oAxes(0) is the A1x component
                |                 oAxes(1) is the A2x component
                |                 oAxes(2) is the A3x component
                |                 oAxes(3) is the A1y component
                |                 oAxes(4) is the A2y component
                |                 oAxes(5) is the A3y component
                |                 oAxes(6) is the A1z component
                |                 oAxes(7) is the A2z component
                |                 oAxes(8) is the A3z component 
                | 
                |     Example:
                | 
                |             This example retrieves the principal axes of
                |             theInertiaElement.
                |             
                | 
                |               Set theInertiaService = CATIA.ActiveEditor.GetService("InertiaService")
                |               Dim theInertiaElement As Inertia
                |               Set theInertiaElement = theInertiaService.GetInertiaElement(theSelection)
                |               Dim theAxes(8)
                |               theInertiaElement.GetPrincipalAxes theAxes

        :return: tuple[float, ...]
        """
        vba_function_name = 'get_principal_axes'
        vba_code = """
        Public Function get_principal_axes(inertia)
            Dim oComponents(8)
            inertia.GetPrincipalAxes oComponents
            get_principal_axes = oComponents
        End Function
        """

        system_service = self.application.system_service
        result  = system_service.evaluate(vba_code, 0, vba_function_name, tuple([self.com_object]))
        return cast(tuple[float, ...], cast(object, result))

        return self.com_object.GetPrincipalAxes(o_axes)

    def get_principal_moments(self) -> tuple[float, float, float]:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetPrincipalMoments(CATSafeArrayVariant oMoments)
                |     Retrieves the principal moments of inertia.
                | 
                |     Parameters:
                | 
                |         oMoments
                |             The principal moments of inertia array:
                | 
                |                 oMoments(0) is the M1 value with respect to the first principal
                |                 axes of inertia
                |                 oMoments(1) is the M2 value with respect to the second
                |                 principal axes of inertia
                |                 oMoments(2) is the M3 value with respect to the third principal
                |                 axes of inertia 
                | 
                |     Example:
                | 
                |             This  example  retrieves  principal  moments  of  inertia  of
                |             theInertiaElement.
                |             
                | 
                |               Set theInertiaService = CATIA.ActiveEditor.GetService("InertiaService")
                |               Dim theInertiaElement As Inertia
                |               Set theInertiaElement = theInertiaService.GetInertiaElement(theSelection)
                |               Dim theMoments(2)
                |               theInertiaElement.GetPrincipalMoments theMoments

        :return: tuple[float, float, float]
        """
        vba_function_name = 'get_principal_moments'
        vba_code = """
        Public Function get_principal_moments(inertia)
            Dim oValues (2)
            inertia.GetPrincipalMoments oValues
            get_principal_moments = oValues
        End Function
        """
        system_service = self.application.system_service
        result  = system_service.evaluate(vba_code, 0, vba_function_name, tuple([self.com_object]))
        return cast(tuple[float, float, float], cast(object, result))

    def get_volume(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetVolume() As double
                |     Retrieves the volume.
                | 
                |     Example:
                | 
                |            This example retrieves the volume of
                |            theInertiaElement.
                |            
                | 
                |              Set theInertiaService = CATIA.ActiveEditor.GetService("InertiaService")
                |              Dim theInertiaElement As Inertia
                |              Set theInertiaElement = theInertiaService.GetInertiaElement(theSelection)
                |              Dim theVolume As Double
                |              theVolume = theInertiaElement.GetVolume

        :return: float
        """
        return self.com_object.GetVolume()

    def only_main_body(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub OnlyMainBody()
                |     Inertia is only computed for the main body of the part if this method is
                |     called before Get methods.
                | 
                |     Example:
                | 
                |             This  example  retrieves  principal  moments  of  inertia  of
                |             theInertiaElement.
                |             
                | 
                |               Set theInertiaService = CATIA.ActiveEditor.GetService("InertiaService")
                |               Dim theInertiaElement As Inertia
                |               Set theInertiaElement = theInertiaService.GetInertiaElement(theSelection)
                |               theInertiaElement.OnlyMainBody

        :return: None
        """
        return self.com_object.OnlyMainBody()

    def __repr__(self):
        return f'Inertia(name="{self.name}")'
