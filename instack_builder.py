#!$(which python)
import json
import fileinput
from copy import copy

"""
simple script that takes text lines with <ipmi IP> <provisionin interface mac address> 
and sends a json instackenv style file to stdout  
"""

_node = {
      "mac":[
        ""
      ],
      "cpu":"1",
      "memory":"1024",
      "disk":"10",
      "arch":"x86_64",
      "pm_type":"pxe_ilo",
      "pm_user":"hp",
      "pm_password":"password",
      "pm_addr":"",
      "name":""
    }
_result = { "nodes": [] }

def main():
  _id = 1
  _tupples = [ line.split() for line in fileinput.input() ]
  for _tup in _tupples:
    _ipmi = _tup[0].strip()
    _mac = _tup[1].strip()
    _cur_node = copy(_node)
    _cur_node["mac"] = [_mac]
    _cur_node["pm_addr"] = _ipmi
    _cur_node["name"] = "miko" + str(_id)
    _result["nodes"].append(_cur_node)
    _id += 1
  print json.dumps(_result, indent=2)

if __name__ == "__main__":
  main()

