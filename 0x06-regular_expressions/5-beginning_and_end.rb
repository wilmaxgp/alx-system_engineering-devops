#!/usr/bin/env ruby
regex = /^h.n$/
string = ARGV[0]
puts string.match(regex) ? string.match(regex)[0] : ''
