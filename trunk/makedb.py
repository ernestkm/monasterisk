#!/usr/bin/env python

import rrdtool

rrdtool.create("asterisk.rrd","--step","300","--start","0","DS:calls:GAUGE:400:U:U","RRA:LAST:0.5:1:525600")
