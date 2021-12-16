
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'package0 1package : version type_lv literalvalue\n    version : bit bit bittype_lv : 1 0 0type_op : bit bit bitlv_value : bit bit bit bitlv_ne : 1 lv_valuelv_e : 0 lv_valuelvs_ne : lv_ne\n              | lvs_ne lv_ne\n    lvs : lv_e\n           | lvs_ne lv_e\n    literalvalue : lvsbit : 0\n           | 1\n    '
    
_lr_action_items = {'0':([0,3,4,5,6,7,8,12,13,14,15,16,19,21,22,23,24,25,26,],[4,4,-13,-14,13,16,4,13,4,-8,4,23,-9,4,-6,-3,4,4,-5,]),'1':([0,2,3,4,5,6,8,12,13,14,15,17,19,21,22,23,24,25,26,],[5,7,5,-13,-14,15,5,15,5,-8,5,-2,-9,5,-6,-3,5,5,-5,]),'$end':([1,4,5,9,10,11,18,20,26,],[0,-13,-14,-1,-12,-10,-11,-7,-5,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'package':([0,],[1,]),'version':([0,],[2,]),'bit':([0,3,8,13,15,21,24,25,],[3,8,17,21,21,24,25,26,]),'type_lv':([2,],[6,]),'literalvalue':([6,],[9,]),'lvs':([6,],[10,]),'lv_e':([6,12,],[11,18,]),'lvs_ne':([6,],[12,]),'lv_ne':([6,12,],[14,19,]),'lv_value':([13,15,],[20,22,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> package","S'",1,None,None,None),
  ('package -> version type_lv literalvalue','package',3,'p_package','a.py',28),
  ('version -> bit bit bit','version',3,'p_version','a.py',34),
  ('type_lv -> 1 0 0','type_lv',3,'p_typeid_lv','a.py',40),
  ('type_op -> bit bit bit','type_op',3,'p_typeid_op','a.py',46),
  ('lv_value -> bit bit bit bit','lv_value',4,'p_lv_value','a.py',52),
  ('lv_ne -> 1 lv_value','lv_ne',2,'p_lv_not_end','a.py',58),
  ('lv_e -> 0 lv_value','lv_e',2,'p_lv_end','a.py',63),
  ('lvs_ne -> lv_ne','lvs_ne',1,'p_lvs_ne1','a.py',68),
  ('lvs_ne -> lvs_ne lv_ne','lvs_ne',2,'p_lvs_ne1','a.py',69),
  ('lvs -> lv_e','lvs',1,'p_lvs','a.py',78),
  ('lvs -> lvs_ne lv_e','lvs',2,'p_lvs','a.py',79),
  ('literalvalue -> lvs','literalvalue',1,'p_literalvalue','a.py',85),
  ('bit -> 0','bit',1,'p_bit','a.py',90),
  ('bit -> 1','bit',1,'p_bit','a.py',91),
]
