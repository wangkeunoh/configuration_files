#! /bin/bash
#splm.sec.samsung.net/wl/tqm/defect/defectreg/goDefectDetail.do?isPopUp=Y&defectCode=P210916-03741
echo "What is the build Number":
read num

google-chrome -new-tab 'https://android.qb.sec.samsung.net/build/'$num
echo "make directory, opel url done":

exec bash #???, 이거 없으면 안되는군 이게 마지막에 있어야함.
#echo $filename >> /home-mc/wangkeun.oh/git_workspace/KinGoodWiki/plms.md
