#!/bin/bash

unset DX_WORKSPACE_ID
dx cd $DX_PROJECT_CONTEXT_ID

echo "{
   \"files\" : [],
   \"directories\" : [
      {
       \"proj_id\" : \"$DX_PROJECT_CONTEXT_ID\",
       \"folder\" : \"/\",
       \"dirname\" : \"/project\"
      }
   ]
 }" > .dxfuse_manifest.json

MOUNTDIR=/mnt2
mkdir -p $MOUNTDIR
/home/dnanexus/dxfuse -limitedWrite $MOUNTDIR .dxfuse_manifest.json
