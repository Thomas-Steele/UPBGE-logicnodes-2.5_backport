from .socket import SOCKET_COLOR_INTEGER, SOCKET_TYPE_INT, NodeSocketLogic
from .socket import socket_type
from .socket import update_draw
from ..enum_types import _enum_local_axis
from bpy.types import NodeSocket
from bpy.props import EnumProperty


@socket_type
class NodeSocketLogicAxis(NodeSocket, NodeSocketLogic):
    bl_idname = "NLSocketLocalAxis"
    bl_label = "Local Axis"

    value: EnumProperty(
        name='Axis',
        items=_enum_local_axis,
        update=update_draw
    )

    color = SOCKET_COLOR_INTEGER
    nl_color = SOCKET_TYPE_INT

    def draw(self, context, layout, node, text):
        if self.is_linked:
            layout.label(text=text)
        else:
            parts = layout.split()
            parts.label(text=text)
            parts.prop(self, "value", text='')

    def get_unlinked_value(self):
        return self.value
