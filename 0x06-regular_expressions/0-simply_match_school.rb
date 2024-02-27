#!/usr/bin/env ruby

regex = /School/

string = ARGV[0]

puts string.match(regex) ? string.match(regex)[0] : ''
