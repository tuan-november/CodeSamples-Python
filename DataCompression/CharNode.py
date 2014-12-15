# =======================================================================================
# DataCompression - Python Code Samples
# CharNode.py
#
# Written by Tuan Anh Nguyen - Software Engineer
#                              www.MyAIvisions.com
# CopyRight - Dec 11, 2014
#
# =======================================================================================

def add(a, b):
	return a + b

class CCharNode:
  def __init__(self):
  	self.character = '*'
  	self.frequency = 0
  	self.parent = None
  	self.left_child = None
  	self.right_child = None
  	self.node_code = 'X'

  def printNode(self):
	  print 'CharNode: '
	  print "%(self)s (code: %(code)s) - %(character)s - %(frequency)s" \
	         %{ "self":hex(id(self)), "code":self.node_code, "character": self.character, "frequency":self.frequency }
	  print "P: %(parent)s - L: %(left_child)s - R: %(right_child)s" \
	         %{ "parent":hex(id(self.parent)), "left_child":hex(id(self.left_child)), "right_child":hex(id(self.right_child)) }

  def printNodeCompact(self):
    print "(%(code)s)%(character)s - %(self)s - P:%(parent)s" \
          %{ "code":self.node_code, "character":self.character, "self":hex(id(self)), "parent":hex(id(self.parent))} 
	
