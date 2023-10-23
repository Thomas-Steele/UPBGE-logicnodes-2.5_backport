from ..node import node_type
from ..node import LogicNodeActionType
from ...sockets import NodeSocketLogicCondition
from ...sockets import NodeSocketLogicObject
from ...sockets import NodeSocketLogicVectorXYZ
from ...sockets import NodeSocketLogicFloatPositive
from bpy.props import BoolProperty


@node_type
class LogicNodeCharacterSetVelocity(LogicNodeActionType):
    bl_idname = "NLActionSetCharacterVelocity"
    bl_label = "Set Velocity"
    nl_module = 'uplogic.nodes.actions'
    nl_class = "ULSetCharacterVelocity"

    local: BoolProperty(default=True, name='Local')

    def init(self, context):
        self.add_input(NodeSocketLogicCondition, "Condition")
        self.add_input(NodeSocketLogicObject, "Object")
        self.add_input(NodeSocketLogicVectorXYZ, "Velocity")
        self.add_input(NodeSocketLogicFloatPositive, "Time")
        self.add_output(NodeSocketLogicCondition, 'Done')
        LogicNodeActionType.init(self, context)

    def get_output_names(self):
        return ["OUT"]

    def draw_buttons(self, context, layout):
        layout.prop(self, "local")

    def get_input_names(self):
        return ["condition", "game_object", 'vel', 'time']

    def get_attributes(self):
        return [("local", self.local)]
