#!/usr/bin/env python
#_*_coding:utf-8_*_
import json
import sys

for line in sys.stdin:
  #print line
  line = json.loads(line)
  if line['coordinates']:
    print '%s\t%s' %(line['id'],line['coordinates']['coordinates'])
  else:
    print '%s\t%s' %(line['id'],line['coordinates'])
