#!/bin/bash
set +x
ffmpeg -i /Users/rca/nltl/lvg-bucket/mp3/first-principles/04.mp3 -i /Users/rca/nltl/lvg-bucket/mp3/first-principles/02.mp3 -i /Users/rca/nltl/lvg-bucket/mp3/first-principles/03.mp3 \
  -filter_complex "[0:a]volume=0.9[a1]; [1:a]volume=0.9[a2]; [2:a]volume=0.5[a3]; [a1][a2][a3]amix=inputs=3:duration=longest" \
  -c:a libmp3lame -q:a 2 output3.mp3
