#!/usr/bin/env ruby

regex = /School/
string = ARGV[0]

matches = string.scan(regex)
output = matches.join

puts output
