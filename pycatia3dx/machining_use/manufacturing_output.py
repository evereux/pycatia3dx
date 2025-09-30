"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class ManufacturingOutput(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ManufacturingOutput
                | 
                | Object that represents the output machining code.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def close_stream(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub CloseStream()
                |     Close the Stream.

        :return: None
        """
        return self.com_object.CloseStream()

    def flush(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Flush()
                |     Flush all Data in the Stream.

        :return: None
        """
        return self.com_object.Flush()

    def new_line(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub NewLine()
                |     Create a New Line in the underlying output stream.

        :return: None
        """
        return self.com_object.NewLine()

    def write_chars(self, i_text: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub write_Chars(CATBSTR iText)
                |     Write the specified string to the underlying output stream.

        :param str i_text:
        :return: None
        """
        return self.com_object.write_Chars(i_text)

    def __repr__(self):
        return f'ManufacturingOutput(name="{ self.name }")'
