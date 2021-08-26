#!/usr/bin/env bash
git clone https://github.com/sy3c4ll/dismanet.git && cd dismanet
./dismanet_enable && ./dismanet_connect &
while [ : ];do
  print "0">../land
  print "0">../water
  ./dismanet_send ../land
  ./dismanet_send ../water
  sleep 3600
done

