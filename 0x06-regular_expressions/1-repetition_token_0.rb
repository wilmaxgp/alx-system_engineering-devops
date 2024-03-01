#!/usr/bin/env ruby

regex = /hbt+n/
string = ARGV[0]
match = string.match(regex)

puts match ? match[0] : ''
