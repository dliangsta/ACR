#/bin/bash
sudo docker run --runtime=nvidia --rm -v "${PWD}/images":/tmp/images dliangsta/medstar python /tmp/marker.py