#!/usr/bin/env ruby

def extract_info(log)
  sender = log.match(/\[from:(.+?)\]/)[1]
  receiver = log.match(/\[to:(.+?)\]/)[1]
  flags = log.match(/\[flags:(.+?)\]/)[1]
  [sender, receiver, flags]
end

log = ARGV[0]
sender, receiver, flags = extract_info(log)

puts "#{sender},#{receiver},#{flags}"
