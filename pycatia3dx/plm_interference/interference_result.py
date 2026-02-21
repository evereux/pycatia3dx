"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.plm_modeller_base.plm_entity import PLMEntity
from pycatia3dx.plm_modeller_base.plm_occurrence import PLMOccurrence


class InterferenceResult(PLMEntity):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     PLMModelerBaseIDLItf.PLMEntity
                |                         InterferenceResult
                | 
                | Interface representing an Interference Result.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def analysis_status(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property AnalysisStatus() As CatInterferenceResultStatus
                |     Returns or sets the status defined by user for the result.
                | 
                |     Parameters:
                | 
                |         iStatus
                |             The status.
                |             Legal values:
                | 
                |             catInterferenceResultStatusOK
                |                 The result is OK.
                |             catInterferenceResultStatusKO
                |                 The result is KO.
                |             catInterferenceResultStatusNotAnalyzed
                |                 The result is not analyzed.
                | 
                |     Returns:
                |         The status. 
                |     Example:
                | 
                |            This example sets the status of oITFResult1 result to OK and
                |            retrieves it.
                |            
                | 
                |            Dim oITFResult1 As InterferenceResult
                |            oITFResult1.AnalysisStatus = catInterferenceResultStatusOK
                |            status = oITFResult1.AnalysisStatus

        :return: int
        """

        return self.com_object.AnalysisStatus

    @analysis_status.setter
    def analysis_status(self, value: int):
        """
        :param int value:
        """

        self.com_object.AnalysisStatus = value

    @property
    def first_product(self) -> PLMOccurrence:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property FirstProduct() As PLMOccurrence (Read Only)
                |     Retrieves the first product in interference.
                | 
                |     Returns:
                |         A product.

        :return: PLMOccurrence
        """

        return PLMOccurrence(self.com_object.FirstProduct)

    @property
    def second_product(self) -> PLMOccurrence:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SecondProduct() As PLMOccurrence (Read Only)
                |     Retrieves the second product in interference.
                | 
                |     Returns:
                |         A product

        :return: PLMOccurrence
        """

        return PLMOccurrence(self.com_object.SecondProduct)

    @property
    def type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Type() As CatInterferenceResultType (Read Only)
                |     Retrieves the type computed for the result.
                | 
                |     Returns:
                |         The type.
                |         Legal values:
                | 
                |         catInterferenceResultTypeClash
                |             The computed result is a clash.
                |         catInterferenceResultTypeContact
                |             The computed result is a contact.
                |         catInterferenceResultTypeClearance
                |             The computed result is a clearance.

        :return: int
        """

        return self.com_object.Type

    @property
    def user_comment(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property UserComment() As CATBSTR
                |     Returns or sets the comment defined by user for the
                |     result.
                | 
                |     Parameters:
                | 
                |         iComment
                |             The comment.
                |             Legal values:
                | 
                |             Any character string
                |                 The result has this string as comment.
                | 
                |     Returns:
                |         The comment. 
                |     Example:
                | 
                |            This example sets the comment of oITFResult1 result to "It is a
                |            deformable part" and retrieves it.
                |            
                | 
                |            Dim oITFResult1 As InterferenceResult
                |            oITFResult1.UserComment = "It is a deformable part"
                |            cmt = oITFResult1.UserComment

        :return: str
        """

        return self.com_object.UserComment

    @user_comment.setter
    def user_comment(self, value: str):
        """
        :param str value:
        """

        self.com_object.UserComment = value

    @property
    def user_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property UserType() As CatInterferenceResultUserType
                |     Returns or sets the type defined by user for the result.
                | 
                |     Parameters:
                | 
                |         iType
                |             The type.
                |             Legal values:
                | 
                |             catInterferenceResultUserTypeClash
                |                 The result is considered as a clash.
                |             catInterferenceResultUserTypeContact
                |                 The result is considered as a contact.
                |             catInterferenceResultUserTypeClearance
                |                 The result is considered as a clearance.
                |             CatInterferenceResultUserTypeNoInterference
                |                 The result is not an interference.
                |             CatInterferenceResultUserTypeUndefined
                |                 The result is not categorized.
                | 
                |     Returns:
                |         The type. 
                |     Example:
                | 
                |            This example sets the type of oITFResult1 result to clash and
                |            retrieves it.
                |            
                | 
                |            Dim oITFResult1 As InterferenceResult
                |            oITFResult1.UserType = catInterferenceResultUserTypeClash
                |            usertype = oITFResult1.UserType

        :return: int
        """

        return self.com_object.UserType

    @user_type.setter
    def user_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.UserType = value

    def compute_picture(self, i_full_path: str, i_format: str, i_width: int, i_height: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub ComputePicture(CATBSTR iFullPath,CATBSTR iFormat,long iWidth,long
                | iHeight)
                |     Returns an image corresponding to the result.
                | 
                |     Parameters:
                | 
                |         iFullPath
                |             The full path of the image.
                |             Legal values:
                | 
                |             Any valid path
                |                 The image is stored at this loacation.
                | 
                |         iFormat
                |             The format of the image.
                |             Legal values:
                | 
                |             "JPEG"
                |                 The image is stored as a jpeg.
                | 
                |         iWidth
                |             The width of the image.
                |             Legal values:
                | 
                |             Any positive
                |                 The image is computed.
                | 
                |         iHeight
                |             The height of the image.
                |             Legal values:
                | 
                |             Any positive
                |                 The image is computed.
                | 
                |     Example:
                | 
                |            This example returns the jpeg image corresponding to oITFResult1
                |            result in "c:\tmp\result1.jpg".
                |            
                | 
                |            Dim oITFResult1 As InterferenceResult
                |            oITFResult1.ComputePicture "c:\tmp\result1.jpg", "JPEG", 1500,
                |            1000

        :param str i_full_path:
        :param str i_format:
        :param int i_width:
        :param int i_height:
        :return: None
        """
        return self.com_object.ComputePicture(i_full_path, i_format, i_width, i_height)

    def get_geometrical_values(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2026-02-08 14:05:01.675948))
                | Sub GetGeometricalValues(CATSafeArrayVariant oPoint1,CATSafeArrayVariant
                | oPoint2,double oDistance)
                |     Retrieves the Geomtrical Values for the result.
                |
                |     Returns:
                |         A minimal distance and points for clearance and contact

        :return: tuple
        """
        return self.com_object.GetGeometricalValues()
        # todo: check this method, does it require system service?
        # Autogenerated comment:
        # some methods require a system service call as the methods expects a vb array object
        # passed to it and there is no way to do this directly with python. In those cases the following code
        # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # vba_function_name = 'get_geometrical_values'
        # vba_code = """
        # Public Function get_geometrical_values(interference_result)
        #     Dim oPoint1 (2)
        #     interference_result.GetGeometricalValues oPoint1
        #     get_geometrical_values = oPoint1
        # End Function
        # """

        # system_service = SystemService(self.application.SystemService)
        # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_intersection_volume(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2026-02-08 14:05:01.675948))
                | Sub GetIntersectionVolume(CATSafeArrayVariant oPt_CoG,double
                | oVolInter)
                |     Retrieves the intersection volume and its center of gravity for the
                |     result.
                |     Intersection volume and its center of gravity are meaningful only if the
                |     interference is a clash.
                |     Value of volume is given in cubic millimeter.
                |     Coordinates of the point is given in millimeter in the absolute
                |     frame.
                |
                |     Returns:
                |         A point (the center of gravity) and the value of volume. An error can
                |         be raise during the computation of the volume. Generally, this problem occurs
                |         when part are non-watertight or non-volumic. Associated message of this error
                |         can be found by the property "Description" of the error.

        :return: tuple
        """
        return self.com_object.GetIntersectionVolume()
        # todo: check this method, does it require system service?
        # Autogenerated comment:
        # some methods require a system service call as the methods expects a vb array object
        # passed to it and there is no way to do this directly with python. In those cases the following code
        # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # vba_function_name = 'get_intersection_volume'
        # vba_code = """
        # Public Function get_intersection_volume(interference_result)
        #     Dim oPt_CoG (2)
        #     interference_result.GetIntersectionVolume oPt_CoG
        #     get_intersection_volume = oPt_CoG
        # End Function
        # """

        # system_service = SystemService(self.application.SystemService)
        # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'InterferenceResult(name="{self.name}")'
