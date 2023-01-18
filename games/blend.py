from typing import Union, List
from colorama import Fore, Style
import bpy
from mathutils import Vector
# from games.scripts.modules import bpy_types


bpy.ops.wm.open_mainfile("EXEC_DEFAULT", filepath="D:\\Yel\\Python\\test_project\\games\\blend.blend")
objs: List[bpy.types.Object] = list(bpy.data.objects)

def print_main_info(ob, head_color=Fore.GREEN, info_color=Fore.LIGHTGREEN_EX):
    loc: Vector = ob.location
    print(end=head_color + Style.BRIGHT)
    print(ob.name, end=":\n")

    # Location
    print("\tLocation:", end="\n\t\t")

    print(end=info_color + Style.NORMAL)

    print(loc.x, loc.y, loc.z, sep="\n\t\t")


for obj in objs:
    match obj.data.__class__:
        case bpy.types.Mesh:
            print_main_info(obj)

            # Vertices
            vertices = obj.data.vertices
            print(
                Style.BRIGHT +
                Fore.GREEN +
                f"\tVertices:" +
                Fore.LIGHTGREEN_EX +
                Style.NORMAL
            )
            if len(vertices) < 20:
                for v in vertices:
                    print(f"\t\t{v.co.x:>10.5f} {v.co.y:>10.5f} {v.co.z:>10.5f}")
            else:
                print(f"\t\t{len(vertices)} vertices")
            print(end=Fore.RESET)
        case bpy.types.Curve:
            print_main_info(obj, Fore.LIGHTYELLOW_EX, Fore.BLUE)
        case bpy.types.Camera:
            print_main_info(obj, Fore.LIGHTBLUE_EX, Fore.LIGHTBLUE_EX)
        case t:
            print_main_info(obj, Fore.LIGHTWHITE_EX, Fore.WHITE)


print()
