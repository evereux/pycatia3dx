"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-13 15:35:27.265802

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class SystemConfiguration(AnyObject):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SystemConfiguration
                | 
                | Provides abstractions to resources which depend on the platform or the current
                | configuration
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def operating_system(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Property OperatingSystem() As CATBSTR (Read Only)
                |     Returns a string which identifies the operating system on which the
                |     application is currently running. Examples of identifiers include: intel_a,
                |     solaris_a, aix_a, win_a, irix_a and hpux_a.
                | 
                |     Parameters:
                | 
                |         oOperatingSystem
                |             The operating system identifier.

        :return: str
        """

        return self.com_object.OperatingSystem

    @property
    def product_count(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Property ProductCount() As long (Read Only)
                |     Returns the number of product names names currently known to the
                |     system.
                | 
                |     Parameters:
                | 
                |         oProductCount
                |             The number of product names currently known to the system.

        :return: int
        """

        return self.com_object.ProductCount

    @property
    def release(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Property Release() As long (Read Only)
                |     Returns the CATIA release number.
                | 
                |     Parameters:
                | 
                |         oVersion
                |             The CATIA release number.

        :return: int
        """

        return self.com_object.Release

    @property
    def service_pack(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Property ServicePack() As long (Read Only)
                |     Returns the CATIA service pack number.
                | 
                |     Parameters:
                | 
                |         oServicePack
                |             The CATIA service pack number.

        :return: int
        """

        return self.com_object.ServicePack

    @property
    def version(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Property Version() As long (Read Only)
                |     Returns the CATIA version number (usually version 5).
                | 
                |     Parameters:
                | 
                |         oVersion
                |             The CATIA version.

        :return: int
        """

        return self.com_object.Version

        def get_product_names(self, io_product_names: tuple) -> None:
            """
            .. note::
                :class: toggle

                3DEXPERIENCE Automation Help (2026-02-08 14:05:01.675948))
                    | Sub GetProductNames(CATSafeArrayVariant ioProductNames)
                    |     Returns the product names of all the licenses currently known to the
                    |     system.
                    |
                    |     Parameters:
                    |
                    |         CATSafeArrayVariant
                    |             An properly dimensioned array of strings in which the product names
                    |             will be stored.
                    |
                    |             Example:
                    |                 This example determines if the first product in the list of
                    |                 known product names is authorized.
                    |
                    |                  Dim SystemConfiguration1 As
                    |                  SystemConfiguration
                    |                  Set SystemConfiguration1 = CATIA.SystemConfiguration
                    |                  ReDim NameArray(SystemConfiguration1.ProductCount-1)                |                  SystemConfiguration1.GetProductNames
                    |                  NameArray
                    |                  MsgBox "IsProductAuthorized for product " & NameArray(0) & "
                    |                  returns " & SystemConfiguration1.IsProductAuthorized(NameArray(0))

            :param tuple io_product_names:
            :return: None
            """
            return self.com_object.GetProductNames(io_product_names)
            # todo: check this method, does it require system service?
            # Autogenerated comment:
            # some methods require a system service call as the methods expects a vb array object
            # passed to it and there is no way to do this directly with python. In those cases the following code
            # should be uncommented and edited accordingly. Otherwise completely remove all this.
            # vba_function_name = 'get_product_names'
            # vba_code = """
            # Public Function get_product_names(system_configuration)
            #     Dim ioProductNames (2)
            #     system_configuration.GetProductNames ioProductNames
            #     get_product_names = ioProductNames
            # End Function
            # """

            # system_service = SystemService(self.application.SystemService)
            # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def is_product_authorized(self, i_product_name: str) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Func IsProductAuthorized(CATBSTR iProductName) As boolean
                |     Returns True if the specified product is authorized, False
                |     otherwise
                | 
                |     Parameters:
                | 
                |         iProductName
                |             The name of the product to check. 
                |         oAuthorized
                |             A boolean which specifies if the product is authorized.

        :param str i_product_name:
        :return: bool
        """
        return self.com_object.IsProductAuthorized(i_product_name)

    def __repr__(self):
        return f'SystemConfiguration(name="{self.name}")'
