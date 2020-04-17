#!/bin/bash
export DICOM_DIRECTORY="${PWD}/dicoms"
docker run -v $DICOM_DIRECTORY:/tmp/dicoms dliangsta/chest_xray_triager python /tmp/chest_xray_triager.py