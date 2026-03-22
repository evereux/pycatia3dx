import pathlib
from types import ModuleType

import psutil
import importlib.util
import importlib.machinery

from win32com.client import Dispatch

from pycatia3dx.interfaces.application import Application


def _get_com3dx_path() -> pathlib.Path:
    """
    Locate the `com3dx.py` module from the running 3DEXPERIENCE process.

    Returns:
        pathlib.Path: Absolute path to the `com3dx.py` module.

    Raises:
        RuntimeError: If `3DEXPERIENCE.exe` is not currently running.
        FileNotFoundError: If `com3dx.py` does not exist at the derived
            installation path.
    """
    com3dx_path = None

    for proc in psutil.process_iter(['name', 'exe']):
        try:
            if proc.info['name'] == '3DEXPERIENCE.exe':
                exe_location = proc.info['exe']
                com3dx_path = (
                    pathlib.Path(exe_location)
                    .parent
                    .parent
                    .joinpath("python3dx", "lib", "com3dx.py")
                )
                break
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    if com3dx_path is None:
        raise RuntimeError(
            "3DEXPERIENCE.exe is not running. Please launch the application first."
        )

    if not com3dx_path.exists():
        raise FileNotFoundError(
            f"Could not find com3dx.py at the expected location: {com3dx_path}"
        )

    return com3dx_path


def _import_com3dx_module() -> ModuleType:
    """
    Dynamically import the Dassault Systèmes `com3dx` module using importlib.

    Returns:
        ModuleType: The loaded `com3dx` module.

    Raises:
        ImportError: If the module specification or loader cannot be
            created or executed.
    """
    module_path = _get_com3dx_path()
    spec = importlib.util.spec_from_file_location("com3dx", module_path)

    if spec is None or spec.loader is None:
        raise ImportError(f"Could not load module spec from {module_path}")

    com3dx = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(com3dx)
    return com3dx


def catia_application(com3dx: bool=True) -> Application:
    """
    Connects to the active 3DEXPERIENCE session and returns a pycatia3dx
    Application object.

    This function tries to dynamically locate and import the `com3dx` module
    provided by the Dassault Systèmes 3DEXPERIENCE installation. The
    module is typically located at:

        3DX_INSTALL_DIR/win_b64/code/python3dx/lib/com3dx.py

    A running instance of `3DEXPERIENCE.exe` is required in order to identify
    the correct installation path.

    If com3dx is set to False pycatia3dx will fall back to using
    win32com.client.Dispatch.  This should only be necessary if the 3DEXPERIENCE
    installation does not include the com3dx.py file.

    :param bool com3dx:
    :return: Application
    """

    if com3dx:
        return Application(_import_com3dx_module().get3dxClient())
    else:
        return Application(Dispatch('CATIA.Application'))
