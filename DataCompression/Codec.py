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

  def decodeString(self, encoded_sequence):
    print encoded_sequence

  def __generateCharHash(self, input_str):
    char_hash = {}
    for c in input_str:
      char_hash[c] = (char_hash[c] + 1) if (c in char_hash) else 1
    return Counter(char_hash).most_common()[::-1]  # sort the hash in ascending order by value
    
  def __populateCharTree(self, char_node_queue, eternal_box):
    first_node, second_node = char_node_queue[0:1]
    # second_node = char_node_queue[1]
    print first_node
    print second_node

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



