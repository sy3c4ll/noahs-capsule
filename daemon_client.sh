#!/usr/bin/env bash
cd dismanet
./dismanet_enable && ./dismanet_connect &
cd ..
while [ : ];do
  print "0">land
  print "0">water
  cd dismanet
  ./dismanet_send ../land
  ./dismanet_send ../water
  cd ..
  sleep 3600
done

