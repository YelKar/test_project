from typing import Union, List

import bpy
from mathutils import Vector

from games.scripts.modules.bpy_types import Object, Mesh


bpy.ops.wm.open_mainfile("EXEC_DEFAULT", filepath="D:\\Yel\\Python\\test_project\\games\\blend.blend")
objs: List[Object] = list(bpy.data.objects)

for obj in objs:
    obj.location: Vector
    print(obj.data.original, obj.location)
    if hasattr(obj.data, "vertices"):
        print("\t", end="")
        for vert in obj.data.vertices:
            print(vert.co.x, vert.co.y, vert.co.z)

print(dir(Mesh))