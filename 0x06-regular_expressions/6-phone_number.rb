#!/usr/bin/env ruby
regex = /^\d{10}$/
string = ARGV[0]
puts string.match(regex) ? string.match(regex)[0] : ''
