#!/usr/bin/env bash
git remote set-url origin https://$2@github.com/sy3c4ll/noahs-capsule.git
cd dismanet
./dismanet_enable.sh && ./dismanet_connect.sh &
cd ..
while [ : ];do
  echo "{\"time\":\"$(date)\",\"land\":$(cat land),\"water\":$(cat water)}">sensor_data.json
  git add sensor_data.json && git commit -m "$(date)" && git push origin master
  sleep 3600
done

