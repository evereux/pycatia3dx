from pycatia3dx.part.add import Add
from pycatia3dx.part.assemble import Assemble
from pycatia3dx.part.auto_draft import AutoDraft
from pycatia3dx.part.auto_fillet import AutoFillet
from pycatia3dx.part.chamfer import Chamfer
from pycatia3dx.part.circ_pattern import CircPattern
from pycatia3dx.part.close_surface import CloseSurface
from pycatia3dx.part.const_rad_edge_fillet import ConstRadEdgeFillet
from pycatia3dx.part.defeaturing import Defeaturing
from pycatia3dx.part.draft import Draft
from pycatia3dx.part.face_fillet import FaceFillet
from pycatia3dx.part.groove import Groove
from pycatia3dx.part.hole import Hole
from pycatia3dx.part.intersect import Intersect
from pycatia3dx.part.loft import Loft
from pycatia3dx.part.mirror import Mirror
from pycatia3dx.part.pad import Pad
from pycatia3dx.part.partition import Partition
from pycatia3dx.part.pocket import Pocket
from pycatia3dx.part.rect_pattern import RectPattern
from pycatia3dx.part.remove import Remove
from pycatia3dx.part.remove_face import RemoveFace
from pycatia3dx.part.replace_face import ReplaceFace
from pycatia3dx.part.rib import Rib
from pycatia3dx.part.scaling import Scaling
from pycatia3dx.part.sew_surface import SewSurface
from pycatia3dx.part.shaft import Shaft
from pycatia3dx.part.shell import Shell
from pycatia3dx.part.slot import Slot
from pycatia3dx.part.solid_combine import SolidCombine
from pycatia3dx.part.split import Split
from pycatia3dx.part.stiffener import Stiffener
from pycatia3dx.part.thick_surface import ThickSurface
from pycatia3dx.part.thickness import Thickness
from pycatia3dx.part.thread import Thread
from pycatia3dx.part.trim import Trim
from pycatia3dx.part.tritangent_fillet import TritangentFillet
from pycatia3dx.part.user_pattern import UserPattern
from pycatia3dx.part.var_rad_edge_fillet import VarRadEdgeFillet

shape_types = {
    'Add': Add,
    'Assemble': Assemble,
    'AutoDraft': AutoDraft,
    'AutoFillet': AutoFillet,
    'Chamfer': Chamfer,
    'CircPattern': CircPattern,
    'CloseSurface': CloseSurface,
    'ConstRadEdgeFillet': ConstRadEdgeFillet,
    'Defeaturing': Defeaturing,
    'Draft': Draft,
    'FaceFillet': FaceFillet,
    'Groove': Groove,
    'Hole': Hole,
    'Intersect': Intersect,
    'Loft': Loft,
    'Mirror': Mirror,
    'Pad': Pad,
    'Partition': Partition,
    'Pocket': Pocket,
    'RectPattern': RectPattern,
    'Remove': Remove,
    'RemoveFace': RemoveFace,
    'ReplaceFace': ReplaceFace,
    'Rib': Rib,
    'Scaling': Scaling,
    'SewSurface': SewSurface,
    'Shaft': Shaft,
    'Shell': Shell,
    'Slot': Slot,
    'SolidCombine': SolidCombine,
    'Stiffener': Stiffener,
    'Split': Split,
    'ThickSurface': ThickSurface,
    'Thickness': Thickness,
    'Thread': Thread,
    'Trim': Trim,
    'TritangentFillet': TritangentFillet,
    'UserPattern': UserPattern,
    'VarRadEdgeFillet': VarRadEdgeFillet,
}
