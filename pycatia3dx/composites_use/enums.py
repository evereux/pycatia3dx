from enum import IntEnum


class CATCompositesTypeEnum(IntEnum):
    Unknown = 0
    Stacking = 1
    PlyGroup = 2
    Sequence = 3
    CutPieceGroup = 4
    Ply = 5
    Core = 6
    CutPiece = 7
