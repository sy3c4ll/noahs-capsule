#!/usr/bin/env bash
git remote set-url origin https://$2@github.com/sy3c4ll/noahs-capsule.git
while [ : ];do
  python scripts/gy521.py land
  echo "{\"time\":\"$(date)\",\"land\":$(cat land)}">sensor_data.json
  git add sensor_data.json && git commit -m "$(date)" && git push origin master
done

