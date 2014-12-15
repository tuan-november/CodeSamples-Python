# =======================================================================================
# DataCompression - Python Code Samples
# Codec.py
#
# Written by Tuan Anh Nguyen - Software Engineer
#                              www.MyAIvisions.com
# CopyRight - Dec 11, 2014
#
# =======================================================================================

from collections import Counter
from CharNode import CCharNode
from EternalBox import CEternalBox

class CCodec:
  def __init__(self):
    self.__root = CCharNode()
    # self.__root.printNode()

  def encodeString(self, input_str):
    self.__generateCharTree(input_str)
    encoded_str = ''

    for c in input_str:
      eternal_box = CEternalBox()
      self.__locateCharNode(c, self.__root, eternal_box)
      eternal_box.char_node.printNode
      self.__encodeChar(eternal_box.char_node, eternal_box)
      encoded_str += eternal_box.encoded_sequence
      # print '%(char)s - %(encoded)s' %{'char': c, 'encoded': eternal_box.encoded_sequence}
    return encoded_str

  def decodeString(self, encoded_sequence):
    eternal_box = CEternalBox()
    eternal_box.encoded_sequence = encoded_sequence
    eternal_box.encoded_sequence_index = 0

    char_node_queue = []
    char_node_queue.append(self.__root)
    
    decoded_string = ''
    # print "len: ", len(encoded_sequence)
    while(eternal_box.encoded_sequence_index < len(encoded_sequence)):
      self.__decodeChar(self.__root, eternal_box)
      # print "decoded_char: ", eternal_box.decoded_char
      decoded_string += eternal_box.decoded_char
      # print "decoded_string: ", decoded_string
      # print "eternal_box.encoded_sequence_index : ", eternal_box.encoded_sequence_index 
    return decoded_string

  def __generateCharHash(self, input_str):
    char_hash = {}
    for c in input_str:
      char_hash[c] = (char_hash[c] + 1) if (c in char_hash) else 1
    return Counter(char_hash).most_common()[::-1]  # sort the hash in ascending order by value
    
  def __populateCharTree(self, char_node_queue, eternal_box):
    left_node = char_node_queue[0]
    right_node = char_node_queue[1]

    parent_node = CCharNode()
    parent_node.left_child = left_node
    parent_node.right_child = right_node
    parent_node.frequency = left_node.frequency + right_node.frequency
    left_node.parent = parent_node
    left_node.node_code = '0'
    right_node.parent = parent_node
    right_node.node_code = '1'

    char_node_queue = char_node_queue[2:len(char_node_queue)]
    char_node_queue.append(parent_node)

    if(len(char_node_queue) > 1):
      self.__populateCharTree(char_node_queue, eternal_box)
    if(len(char_node_queue) == 1):
      eternal_box.char_node = char_node_queue[0]  

  def __generateCharTree(self, input_str):
    char_hash = self.__generateCharHash(input_str) # technically, an array of tuples
    char_node_queue = []
    for member in char_hash:
      temp_node = CCharNode()
      temp_node.character = member[0]
      temp_node.frequency = member[1]
      char_node_queue.append(temp_node)

    eternal_box = CEternalBox()
    self.__populateCharTree(char_node_queue, eternal_box)
    self.__root = eternal_box.char_node

  def __locateCharNode(self, input_char, tree_traveller, eternal_box):
    char_found = False
    if(tree_traveller.character == input_char):
      eternal_box.char_node = tree_traveller
      char_found = True;
      
    if(tree_traveller.character != input_char and not char_found):
      if(tree_traveller.left_child != None):
        char_found = self.__locateCharNode(input_char, tree_traveller.left_child, eternal_box)
      if(tree_traveller.right_child != None and not char_found):
        self.__locateCharNode(input_char, tree_traveller.right_child, eternal_box)
    return char_found  

  def __encodeChar(self, char_node, eternal_box):
    if(char_node != self.__root):
      eternal_box.encoded_sequence += char_node.node_code
      self.__encodeChar(char_node.parent, eternal_box)
    else:
      eternal_box.encoded_sequence = eternal_box.encoded_sequence[::-1]

  def __decodeChar(self, curr_char_node, eternal_box):
    if(curr_char_node.left_child == None and curr_char_node.right_child == None):
      eternal_box.decoded_char = curr_char_node.character
      return True

    char_found = False
    next_node = eternal_box.encoded_sequence[eternal_box.encoded_sequence_index]
    # print "next_node: ", next_node
    if(next_node == '0' and curr_char_node.left_child != None and not char_found):
      eternal_box.encoded_sequence_index += 1
      char_found = self.__decodeChar(curr_char_node.left_child, eternal_box)

    if(next_node == '1' and curr_char_node.right_child != None and not char_found):
  	  eternal_box.encoded_sequence_index += 1
  	  char_found = self.__decodeChar(curr_char_node.right_child, eternal_box)
      
    return char_found    

  def __printTree(self, char_node_queue):
    if(len(char_node_queue) <= 0):
      return False
    new_node_queue = []  
    for n in char_node_queue:
      n.printNodeCompact()
      if(n.left_child != None):
        new_node_queue.append(n.left_child)
      if(n.right_child != None):
        new_node_queue.append(n.right_child)
    print

    if(len(new_node_queue) > 0):
      self.__printTree(new_node_queue)







