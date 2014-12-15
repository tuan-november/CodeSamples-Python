# =======================================================================================
# DataCompression - Python Code Samples
# EternalBox.py
#
# Written by Tuan Anh Nguyen - Software Engineer
#                              www.MyAIvisions.com
# CopyRight - Dec 11, 2014
#
# =======================================================================================

from CharNode import CCharNode

class CEternalBox:
  def __init__(self):
  	self.char_node              = CCharNode()
  	self.decoded_char           = ''
  	self.encoded_sequence       = ''
  	self.encoded_sequence_index = 0

