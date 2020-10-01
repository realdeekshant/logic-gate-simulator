from PyQt5.QtCore import *
from conf import *
from conf import register_node
from node_base import *
from nodeeditor.utils import dumpException


@register_node(OP_NODE_OR)
class GateNode_Add(GateNode):
    op_code = OP_NODE_OR
    op_title = "OR Gate"
    content_label = "OR"
    content_label_objname = "node_or"

    def evalOperation(self, input1, input2):
        return input1 or input2


@register_node(OP_NODE_AND)
class GateNode_Sub(GateNode):
    op_code = OP_NODE_AND
    op_title = "AND Gate"
    content_label = "AND"
    content_label_objname = "node_and"

    def evalOperation(self, input1, input2):
        return input1 and input2


@register_node(OP_NODE_NOT)
class GateNode_Sub(GateNode):
    op_code = OP_NODE_NOT
    op_title = "NOT Gate"
    content_label = "NOT"
    content_label_objname = "node_not"

    def __init__(self, scene):
        super().__init__(scene, inputs=[1], outputs=[1])

    def evalOperations(self, input1):
        return not input1

    def evalImplementation(self):
        i1 = self.getInput(0)

        if i1 is None:
            self.markInvalid()
            self.markDescendantsDirty()
            self.grNode.setToolTip("Connect all inputs")
            return None

        else:
            val = self.evalOperations(i1.eval())
            self.value = val
            self.markDirty(False)
            self.markInvalid(False)
            self.grNode.setToolTip("")

            self.markDescendantsDirty()
            self.evalChildren()

            return val

    def onInputChanged(self, socket=None):
        print("%s::__onInputChanged" % self.__class__.__name__)
        self.markDirty()
        self.eval()

    def serialize(self):
        res = super().serialize()
        res['op_code'] = self.__class__.op_code
        return res

    def deserialize(self, data, hashmap={}, restore_id=True):
        res = super().deserialize(data, hashmap, restore_id)
        print("Deserialized Node '%s'" % self.__class__.__name__, "res:", res)
        return res


@register_node(OP_NODE_NOR)
class GateNode_Mul(GateNode):
    op_code = OP_NODE_NOR
    op_title = "NOR Gate"
    content_label = "NOR"
    content_label_objname = "node_nor"

    def evalOperation(self, input1, input2):
        return not (input1 or input2)


@register_node(OP_NODE_NAND)
class GateNode_Mul(GateNode):
    op_code = OP_NODE_NAND
    op_title = "NAND Gate"
    content_label = "NAND"
    content_label_objname = "node_nand"

    def evalOperation(self, input1, input2):
        return not (input1 and input2)


@register_node(OP_NODE_XOR)
class GateNode_Div(GateNode):
    op_code = OP_NODE_XOR
    op_title = "XOR Gate"
    content_label = "XOR"
    content_label_objname = "node_xor"

    def evalOperation(self, input1, input2):
        return (input1 and not input2) or (not input1 and input2)


@register_node(OP_NODE_NXOR)
class GateNode_Div(GateNode):
    op_code = OP_NODE_NXOR
    op_title = "XNOR Gate"
    content_label = "XNOR"
    content_label_objname = "node_xnor"

    def evalOperation(self, input1, input2):
        return not ((input1 and not input2) or (not input1 and input2))

# way how to register by function call
# register_node_now(OP_NODE_ADD, GateNode_Add)
