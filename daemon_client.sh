#!/usr/bin/env bash
cd dismanet
./dismanet_enable && ./dismanet_connect &
cd ..
while [ : ];do
  python scripts/gy521.py land
  python scripts/hcsr04.py water
  cd dismanet
  ./dismanet_send ../land
  ./dismanet_send ../water
  cd ..
  sleep 3600
done

