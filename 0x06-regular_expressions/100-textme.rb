#!/usr/bin/env ruby

# Regular expression pattern to match sender, receiver, and flags
pattern = /\[from:([^]]+)\] \[to:([^]]+)\] \[flags:([^]]+)\]/

# Read each line from the log file
ARGF.each do |line|
  # Match the pattern in the line
  match_data = line.match(pattern)

  # Extract sender, receiver, and flags
  sender = match_data[1]
  receiver = match_data[2]
  flags = match_data[3]

  # Output the result in the required format
  puts "#{sender},#{receiver},#{flags}"
end
