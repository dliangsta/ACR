#/bin/bash
export IMAGE_DIRECTORY="${PWD}/images"
docker run --runtime=nvidia --rm -v $IMAGE_DIRECTORY:/tmp/images dliangsta/laterality_marker python /tmp/marker.py