#!/usr/bin/env ruby
# The sender phone number or name (including country code if present)
# The receiver phone number or name (including country code if present)
# The flags that were used
puts ARGV[0].scan(/\[from:(\+?\d+|[A-Za-z]+)\] \[to:(\+?\d+|[A-Za-z]+)\] \[flags:(-?\d+:-?\d+:-?\d+:-?\d+:-?\d+)\]/).join
