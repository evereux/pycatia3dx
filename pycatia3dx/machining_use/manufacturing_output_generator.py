"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.machining_use.manufacturing_generator_data import ManufacturingGeneratorData


class ManufacturingOutputGenerator(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ManufacturingOutputGenerator
                | 
                | Father object to generate output machining code.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def add_me_to_buffer(self, o_add_me: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub AddMeToBuffer(long oAddMe)
                |     Management of specific buffer for aligned points elimination.

        :param int o_add_me:
        :return: None
        """
        return self.com_object.AddMeToBuffer(o_add_me)

    def generate_output_code(self, i_data: ManufacturingGeneratorData) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GenerateOutputCode(ManufacturingGeneratorData iData)
                |     Return the Output Code for an object in the right CNC Machine.

        :param ManufacturingGeneratorData i_data:
        :return: None
        """
        return self.com_object.GenerateOutputCode(i_data.com_object)

    def get_apt_code(self, i_data: ManufacturingGeneratorData, o_code: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetAPTCode(ManufacturingGeneratorData iData,CATBSTR oCode)
                |     Retrieve generated APT code.

        :param ManufacturingGeneratorData i_data:
        :param str o_code:
        :return: None
        """
        return self.com_object.GetAPTCode(i_data.com_object, o_code)

    def get_current_object(self, o_current_object: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetCurrentObject(long oCurrentObject)
                |     Get current object from buffer.

        :param int o_current_object:
        :return: None
        """
        return self.com_object.GetCurrentObject(o_current_object)

    def has_to_reset_modal_values(self, o_is_modal: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub HasToResetModalValues(long oIsModal)
                |     Return the characteristic of an object : Reset or not Modal Values.

        :param int o_is_modal:
        :return: None
        """
        return self.com_object.HasToResetModalValues(o_is_modal)

    def init_file_generator(self, i_format: str, i_file_name: str, o_data: ManufacturingGeneratorData) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub InitFileGenerator(CATBSTR iFormat,CATBSTR
                | iFileName,ManufacturingGeneratorData oData)
                |     Init the Output Generator on the current Object and initialise all datas.
                |     Generation of NC code can start from the Process, Setup, Program or an
                |     Activity.
                | 
                |     Parameters:
                | 
                |         iFormat
                |             Format of the output file : "APT", ... 
                |         iFileName
                |             Output file name 
                |         oData
                |             iData contains all the information about the generated NC code

        :param str i_format:
        :param str i_file_name:
        :param ManufacturingGeneratorData o_data:
        :return: None
        """
        return self.com_object.InitFileGenerator(i_format, i_file_name, o_data.com_object)

    def is_modal(self, o_is_modal: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub IsModal(long oIsModal)
                |     Return the characteristic of an object : Modal or Not Modal.

        :param int o_is_modal:
        :return: None
        """
        return self.com_object.IsModal(o_is_modal)

    def is_similar_to(self, i_object: 'ManufacturingOutputGenerator') -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func IsSimilarTo(ManufacturingOutputGenerator iObject) As long
                |     Implement a method to specify if two objects are same (when Modal Mode).
                |     The result depends on the tolerance on the values (to points)

        :param ManufacturingOutputGenerator i_object:
        :return: int
        """
        return self.com_object.IsSimilarTo(i_object.com_object)

    def run_file_generator(self, i_data: ManufacturingGeneratorData) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub RunFileGenerator(ManufacturingGeneratorData iData)
                |     Runs the Output Generator on the datas used for generation. Generation of
                |     NC code can start from the Process, Setup, Program or an
                |     Activity.
                | 
                |     Parameters:
                | 
                |         iData
                |             iData contains all the information about the generated NC code

        :param ManufacturingGeneratorData i_data:
        :return: None
        """
        return self.com_object.RunFileGenerator(i_data.com_object)

    def set_current_object(self, i_current_object: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetCurrentObject(long iCurrentObject)
                |     Set current object to buffer.

        :param int i_current_object:
        :return: None
        """
        return self.com_object.SetCurrentObject(i_current_object)

    def __repr__(self):
        return f'ManufacturingOutputGenerator(name="{ self.name }")'
