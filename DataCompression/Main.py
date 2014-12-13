# =======================================================================================
# DataCompression - Python Code Samples
# Main.py
#
# Written by Tuan Anh Nguyen - Software Engineer
#                              www.MyAIvisions.com
# CopyRight - Dec 11, 2014
#
# =======================================================================================

from CharNode   import CCharNode
from Codec      import CCodec
from EternalBox import CEternalBox

input_str = "Jingle Bell Jingle Bell Jingle all the way... Oh what fun it is to be laughing all the way..."
print input_str

codec_mgr = CCodec()
encoded_str = codec_mgr.encodeString(input_str)
print encoded_str

decoded_str = codec_mgr.decodeString(encoded_str)
print decoded_str
 



