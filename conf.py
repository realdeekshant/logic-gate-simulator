LISTBOX_MIMETYPE = "application/x-item"

OP_NODE_INPUT = 1
OP_NODE_OUTPUT = 2
OP_NODE_OR = 3
OP_NODE_AND = 4
OP_NODE_NOR = 5
OP_NODE_NAND = 6
OP_NODE_NOT = 7
OP_NODE_XOR = 8
OP_NODE_NXOR = 9

GATE_NODES = {
}

class ConfException(Exception): pass
class InvalidNodeRegistration(ConfException): pass
class OpCodeNotRegistered(ConfException): pass

def register_node_now(op_code, class_reference):
    if op_code in GATE_NODES:
        raise InvalidNodeRegistration("Duplicite node registration of '%s'. There is already %s" % (
            op_code, GATE_NODES[op_code]
        ))
    GATE_NODES[op_code] = class_reference


def register_node(op_code):
    def decorator(original_class):
        register_node_now(op_code, original_class)
        return original_class

    return decorator


def get_class_from_opcode(op_code):
    if op_code not in GATE_NODES: raise OpCodeNotRegistered("OpCode '%d' is not registered" % op_code)
    return GATE_NODES[op_code]


# import all nodes and register them
from nodes.input import *
from nodes.output import *
from nodes.operations import *
