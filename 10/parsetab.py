
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'codeblockleftLROUNDleftRROUNDleftLSQUAREleftRSQUAREleftLANGLEleftRANGLEleftLCURLYleftRCURLYleftNEWLINELANGLE LCURLY LROUND LSQUARE NEWLINE RANGLE RCURLY RROUND RSQUAREcodeblock : linecodeblock : codeblock lineline : chunks NEWLINEchunks : chunkchunks : chunks chunkchunks : error chunk\n    chunk : LROUND RROUND\n             | LSQUARE RSQUARE\n             | LANGLE RANGLE\n             | LCURLY RCURLY\n    chunk : LROUND chunks RROUND\n             | LSQUARE chunks RSQUARE\n             | LANGLE chunks RANGLE\n             | LCURLY chunks RCURLY\n    '
    
_lr_action_items = {'error':([0,1,2,6,7,8,9,10,11,],[5,5,-1,5,5,5,5,-2,-3,]),'LROUND':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,],[6,6,-1,6,-4,6,6,6,6,6,-2,-3,-5,-6,-7,6,-8,6,-9,6,-10,6,-11,-12,-13,-14,]),'LSQUARE':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,],[7,7,-1,7,-4,7,7,7,7,7,-2,-3,-5,-6,-7,7,-8,7,-9,7,-10,7,-11,-12,-13,-14,]),'LANGLE':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,],[8,8,-1,8,-4,8,8,8,8,8,-2,-3,-5,-6,-7,8,-8,8,-9,8,-10,8,-11,-12,-13,-14,]),'LCURLY':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,],[9,9,-1,9,-4,9,9,9,9,9,-2,-3,-5,-6,-7,9,-8,9,-9,9,-10,9,-11,-12,-13,-14,]),'$end':([1,2,10,11,],[0,-1,-2,-3,]),'NEWLINE':([3,4,12,13,14,16,18,20,22,23,24,25,],[11,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,]),'RROUND':([4,6,12,13,14,15,16,18,20,22,23,24,25,],[-4,14,-5,-6,-7,22,-8,-9,-10,-11,-12,-13,-14,]),'RSQUARE':([4,7,12,13,14,16,17,18,20,22,23,24,25,],[-4,16,-5,-6,-7,-8,23,-9,-10,-11,-12,-13,-14,]),'RANGLE':([4,8,12,13,14,16,18,19,20,22,23,24,25,],[-4,18,-5,-6,-7,-8,-9,24,-10,-11,-12,-13,-14,]),'RCURLY':([4,9,12,13,14,16,18,20,21,22,23,24,25,],[-4,20,-5,-6,-7,-8,-9,-10,25,-11,-12,-13,-14,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'codeblock':([0,],[1,]),'line':([0,1,],[2,10,]),'chunks':([0,1,6,7,8,9,],[3,3,15,17,19,21,]),'chunk':([0,1,3,5,6,7,8,9,15,17,19,21,],[4,4,12,13,4,4,4,4,12,12,12,12,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> codeblock","S'",1,None,None,None),
  ('codeblock -> line','codeblock',1,'p_program1','b.py',75),
  ('codeblock -> codeblock line','codeblock',2,'p_program2','b.py',81),
  ('line -> chunks NEWLINE','line',2,'p_line','b.py',88),
  ('chunks -> chunk','chunks',1,'p_chunks','b.py',94),
  ('chunks -> chunks chunk','chunks',2,'p_chunks2','b.py',99),
  ('chunks -> error chunk','chunks',2,'p_chunk_error','b.py',104),
  ('chunk -> LROUND RROUND','chunk',2,'p_chunk1','b.py',111),
  ('chunk -> LSQUARE RSQUARE','chunk',2,'p_chunk1','b.py',112),
  ('chunk -> LANGLE RANGLE','chunk',2,'p_chunk1','b.py',113),
  ('chunk -> LCURLY RCURLY','chunk',2,'p_chunk1','b.py',114),
  ('chunk -> LROUND chunks RROUND','chunk',3,'p_chunk2','b.py',120),
  ('chunk -> LSQUARE chunks RSQUARE','chunk',3,'p_chunk2','b.py',121),
  ('chunk -> LANGLE chunks RANGLE','chunk',3,'p_chunk2','b.py',122),
  ('chunk -> LCURLY chunks RCURLY','chunk',3,'p_chunk2','b.py',123),
]
