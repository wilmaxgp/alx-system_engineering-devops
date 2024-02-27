#!/usr/bin/env ruby
regex = /hbt+n/
string = ARGV[0]
puts string.match(regex) ? string.match(regex)[0] : ''
