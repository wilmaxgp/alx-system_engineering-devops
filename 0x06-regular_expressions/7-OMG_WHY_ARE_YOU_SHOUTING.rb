#!/usr/bin/env ruby
regex = /[A-Z]+/
string = ARGV[0]
matched = string.scan(regex).join
puts matched
