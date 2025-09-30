"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.system.cat_base_unknown import CATBaseUnknown
from pycatia3dx.todo_machining_use.manufacturing_output import ManufacturingOutput


class ManufacturingGeneratorData(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ManufacturingGeneratorData
                | 
                | Represents the manufacturing output stream object.
                | This object contains the output stream generated for the output files (APT,
                | etc.).
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def add_object_to_generate(self, i_object: CATBaseUnknown) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub AddObjectToGenerate(CATBaseUnknown iObject)
                |     Adds an object to the output stream.
                | 
                |     Parameters:
                | 
                |         iObject
                |             The object to add

        :param CATBaseUnknown i_object:
        :return: None
        """
        return self.com_object.AddObjectToGenerate(i_object.com_object)

    def add_object_to_generate_from_buffer(self, i_object: CATBaseUnknown) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub AddObjectToGenerateFromBuffer(CATBaseUnknown iObject)
                |     Adds an object to the output stream from the buffer.
                | 
                |     Parameters:
                | 
                |         iObject
                |             The object to add

        :param CATBaseUnknown i_object:
        :return: None
        """
        return self.com_object.AddObjectToGenerateFromBuffer(i_object.com_object)

    def add_object_to_generate_with_buffer(self, i_object: CATBaseUnknown) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub AddObjectToGenerateWithBuffer(CATBaseUnknown iObject)
                |     Adds an object to the output stream within the buffer.
                | 
                |     Parameters:
                | 
                |         iObject
                |             The object to add

        :param CATBaseUnknown i_object:
        :return: None
        """
        return self.com_object.AddObjectToGenerateWithBuffer(i_object.com_object)

    def add_object_to_generate_with_out_buffer(self, i_object: CATBaseUnknown) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub AddObjectToGenerateWithOutBuffer(CATBaseUnknown iObject)
                |     Adds an object to the output stream without the buffer.
                | 
                |     Parameters:
                | 
                |         iObject
                |             The object to add

        :param CATBaseUnknown i_object:
        :return: None
        """
        return self.com_object.AddObjectToGenerateWithOutBuffer(i_object.com_object)

    def add_object_to_modal_values(self, i_object: CATBaseUnknown) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub AddObjectToModalValues(CATBaseUnknown iObject)
                |     Adds an object to the modal values manager only.
                | 
                |     Parameters:
                | 
                |         iObject
                |             The object to add

        :param CATBaseUnknown i_object:
        :return: None
        """
        return self.com_object.AddObjectToModalValues(i_object.com_object)

    def get_ft06_stream(self, o_stream: ManufacturingOutput) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetFT06Stream(ManufacturingOutput oStream)
                |     Retrieves the FT06 stream.
                | 
                |     Parameters:
                | 
                |         oStream
                |             The retrieved stream

        :param ManufacturingOutput o_stream:
        :return: None
        """
        return self.com_object.GetFT06Stream(o_stream.com_object)

    def get_last_object_to_generate(self, o_object: CATBaseUnknown) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetLastObjectToGenerate(CATBaseUnknown oObject)
                |     Retrieves the last object to generate.
                | 
                |     Parameters:
                | 
                |         oObject
                |             The retrieved object

        :param CATBaseUnknown o_object:
        :return: None
        """
        return self.com_object.GetLastObjectToGenerate(o_object.com_object)

    def get_output_stream(self, o_stream: ManufacturingOutput) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetOutputStream(ManufacturingOutput oStream)
                |     Retrieves the output stream.
                | 
                |     Parameters:
                | 
                |         oStream
                |             The retrieved stream

        :param ManufacturingOutput o_stream:
        :return: None
        """
        return self.com_object.GetOutputStream(o_stream.com_object)

    def keep_stream_open(self, i_keep_open: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub KeepStreamOpen(boolean iKeepOpen)
                |     Keep the stream open at end of current generation The default behavior is
                |     to close stream at end of output generation for current program. In case
                |     multiple program outputs need to be appended in a single file, this method
                |     should be called after InitFileGenerator with TRUE for initial programs and
                |     FALSE for final program.
                | 
                |     Parameters:
                | 
                |         iKeepOpen
                |             A flag to indicate whether the stream should be kept open or
                |             closed
                |             Legal values:
                | 
                |                 TRUE: Keep the stream open
                |                 FALSE: Close the stream

        :param bool i_keep_open:
        :return: None
        """
        return self.com_object.KeepStreamOpen(i_keep_open)

    def reset_all_modal_values(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub ResetAllModalValues()
                |     Resets all modal values.

        :return: None
        """
        return self.com_object.ResetAllModalValues()

    def set_last_object_to_generate(self, i_object: CATBaseUnknown) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetLastObjectToGenerate(CATBaseUnknown iObject)
                |     Sets the last Activity to generate.
                | 
                |     Parameters:
                | 
                |         iObject
                |             The activity to generate

        :param CATBaseUnknown i_object:
        :return: None
        """
        return self.com_object.SetLastObjectToGenerate(i_object.com_object)

    def __repr__(self):
        return f'ManufacturingGeneratorData(name="{ self.name }")'
