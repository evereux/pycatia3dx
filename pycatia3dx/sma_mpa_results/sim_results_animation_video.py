"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class SimResultsAnimationVideo(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimResultsAnimationVideo
                | 
                | Represents the animation video creation class.
                | Role:The animation video can be created using this class.
                | Example:
                | 
                |  Given a  SimResultRepManager object, you can set the various video
                |  options.
                |  
                | 
                |  Dim oResAnimVideo As SimResultsAnimationVideo
                |  Set oResAnimVideo = oResultRepManager.GetItem("SimResultsAnimationVideo")
                |  set oResAnimVideo.PlotWidth = 1000
                |  set oResAnimVideo.PlotHeight = 800
                |  oResAnimVideo.CreateMovie "D:\temp", "PlotMovie.1"
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def plot_height(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property PlotHeight() As long
                |     Sets and gets the height of the plot for movie creation.

        :return: int
        """

        return self.com_object.PlotHeight

    @plot_height.setter
    def plot_height(self, value: int):
        """
        :param int value:
        """

        self.com_object.PlotHeight = value

    @property
    def plot_width(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property PlotWidth() As long
                |     Sets and gets the width of the plot for movie creation.

        :return: int
        """

        return self.com_object.PlotWidth

    @plot_width.setter
    def plot_width(self, value: int):
        """
        :param int value:
        """

        self.com_object.PlotWidth = value

    def create_movie(self, ics_file_path: str, ics_file_name: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub CreateMovie(CATBSTR icsFilePath,CATBSTR icsFileName)
                |     Creates the movie at the given path. If none of the above attributes are
                |     set, the movie will be created using default setting.
                | 
                |     Parameters:
                | 
                |         icsFilePath
                |             Valid path should be provided else the movie creation will fail.
                |             For e.g. "C:\\Users\\temp".
                |         icsFileName
                |             Valid file name should be provided else the movie creation will
                |             fail.

        :param str ics_file_path:
        :param str ics_file_name:
        :return: None
        """
        return self.com_object.CreateMovie(ics_file_path, ics_file_name)

    def get_list_of_codec_options(self, ocs_codec_options: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetListOfCodecOptions(CATSafeArrayVariant ocsCodecOptions)
                |     Gets the list of codec options available.
                | 
                |     Parameters:
                | 
                |         ocsCodecOptions
                |             The available list of string of the codec options. The optons can
                |             be IntelIYUV, MicrosoftVideo1, FullFrames(compressed) etc.

        :param tuple ocs_codec_options:
        :return: None
        """
        return self.com_object.GetListOfCodecOptions(ocs_codec_options)

    def set_codec(self, ics_codec: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetCodec(CATBSTR icsCodec)
                |     Sets the codecs type. Use GetListOfCodecOptions() method to get the list of
                |     available options.
                | 
                |     Parameters:
                | 
                |         icsCodec
                |             Sets the codecs type. Use GetListOfCodecOptions() method to get the
                |             list of available options. The SetCompressionOptions() API can be used to set
                |             the options for Microsoft Video 1 codec.

        :param str ics_codec:
        :return: None
        """
        return self.com_object.SetCodec(ics_codec)

    def set_compression_options(self, id_temp_quality_ratio: float, ib_is_key_frame_on: bool, inb_key_frame: int, inb_compression_quality: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetCompressionOptions(double idTempQualityRatio,boolean ibIsKeyFrameOn,long
                | inbKeyFrame,long inbCompressionQuality)
                |     Sets the compression options. These options are only avaialble for
                |     "Microsoft Video 1".
                | 
                |     Parameters:
                | 
                |         idTempQualityRatio
                |             Sets the temporary quality ratio. It is available in the UI in the
                |             configure option. 
                |         ibIsKeyFrameOn
                |             Set as true to show the key frames after every specific number of
                |             frames 
                |         inbKeyFrame
                |             Number of frames after which key frames are to be shown.
                |             
                |         inbCompressionQuality
                |             Specify the compression quality. Its value ranges from 1 to 100.

        :param float id_temp_quality_ratio:
        :param bool ib_is_key_frame_on:
        :param int inb_key_frame:
        :param int inb_compression_quality:
        :return: None
        """
        return self.com_object.SetCompressionOptions(id_temp_quality_ratio, ib_is_key_frame_on, inb_key_frame, inb_compression_quality)

    def set_playback(self, ie_playback: int, id_value: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetPlayback(SimAnimPlaybackTypes iePlayback,double
                | idValue)
                |     Sets the playback options.
                | 
                |     Parameters:
                | 
                |         iePlayback
                |             The available options can be found in SimAnimPlaybackTypes.idl
                |             
                |         idValue
                |             It is fps for frames per second and second for total time.

        :param int ie_playback:
        :param float id_value:
        :return: None
        """
        return self.com_object.SetPlayback(ie_playback, id_value)

    def set_ray_trace_options(self, inb_compression_quality: int, ib_is_ray_trace_on: bool, inb_ray_trace_quality: int, ib_is_denoise_on: bool, ib_is_use_gpu_on: bool, ib_is_max_time_on: bool, inb_time_value: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetRayTraceOptions(long inbCompressionQuality,boolean ibIsRayTraceOn,long
                | inbRayTraceQuality,boolean ibIsDenoiseOn,boolean ibIsUseGPUOn,boolean
                | ibIsMaxTimeOn,long inbTimeValue)
                |     Sets the ray trace options. These options are available only for "H.264 /
                |     MPEG-4 AVC".
                | 
                |     Parameters:
                | 
                |         inbCompressionQuality
                |             Compression quality values are in range 0 to 4. Values are
                |             "0-Tiff", "1-Low", "2-Medium", "3-High", "4-Lossless". The below options are
                |             available only for Microsoft Video 1 codec. 
                |         ibIsRayTraceOn
                |             Set as true to include the ray trace options. 
                |         inbRayTraceQuality
                |             The values are 0 to 2. O-Low, 1-Medium, 2-High. 
                |         ibIsDenoiseOn
                |             Set as true to enable the denoise 
                |         ibIsUseGPUOn
                |             Set as true to use the GPU. 
                |         ibIsMaxTimeOn
                |             Set as true to use the max time or frames. 
                |         inbTimeValue
                |             Max Time or frame values in seconds.

        :param int inb_compression_quality:
        :param bool ib_is_ray_trace_on:
        :param int inb_ray_trace_quality:
        :param bool ib_is_denoise_on:
        :param bool ib_is_use_gpu_on:
        :param bool ib_is_max_time_on:
        :param int inb_time_value:
        :return: None
        """
        return self.com_object.SetRayTraceOptions(inb_compression_quality, ib_is_ray_trace_on, inb_ray_trace_quality, ib_is_denoise_on, ib_is_use_gpu_on, ib_is_max_time_on, inb_time_value)

    def set_xy_plot_options(self, ib_include_xy_plot: bool, inb_height: int, inb_width: int, inb_x_position: int, inb_y_position: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetXYPlotOptions(boolean ibIncludeXYPlot,long inbHeight,long inbWidth,long
                | inbXPosition,long inbYPosition)
                |     Specifies the XYPlot options to be included in the video.
                | 
                |     Parameters:
                | 
                |         ibIncludeXYPlot
                |             Set true to include the XY plot in the video. If set false, no need
                |             to set the below parameters. By default, the XY plot will not be included.
                |             
                |         idHeight
                |             Sets the height percentage for the XY viewer. 
                |         idWidth
                |             Sets the width percentage for the XY viewer. 
                |         idXPosition
                |             Sets the X position percentage for the XY viewer. If set zero, the
                |             viewer will be shown at the left most side in the video.
                |             
                |         idYPosition
                |             Sets the Y position percentage for the XY viewer. If set zero, the
                |             viewer will be shown at the bottom most side in the video.

        :param bool ib_include_xy_plot:
        :param int inb_height:
        :param int inb_width:
        :param int inb_x_position:
        :param int inb_y_position:
        :return: None
        """
        return self.com_object.SetXYPlotOptions(ib_include_xy_plot, inb_height, inb_width, inb_x_position, inb_y_position)

    def __repr__(self):
        return f'SimResultsAnimationVideo(name="{ self.name }")'
