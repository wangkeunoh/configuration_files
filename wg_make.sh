#! /bin/bash
#splm.sec.samsung.net/wl/tqm/defect/defectreg/goDefectDetail.do?isPopUp=Y&defectCode=P210916-03741
echo "What is the PLM Number":
read os
read filename
if [ $os = "ros" ]
then
    mkdir -p /home-mc/wangkeun.oh/plmLog/ros/$filename
    cd /home-mc/wangkeun.oh/plmLog/ros/$filename
elif [ $os = "sos" ]
then
    mkdir -p /home-mc/wangkeun.oh/plmLog/sos/$filename
    cd /home-mc/wangkeun.oh/plmLog/sos/$filename
elif [ $os = "tos" ]
then
    mkdir -p /home-mc/wangkeun.oh/plmLog/tos/$filename
    cd /home-mc/wangkeun.oh/plmLog/tos/$filename
elif [ $os = "uos" ]
then
    mkdir -p /home-mc/wangkeun.oh/plmLog/uos/$filename
    cd /home-mc/wangkeun.oh/plmLog/uos/$filename
fi
#firefox -new-tab 'splm.sec.samsung.net/wl/tqm/defect/defectreg/goDefectDetail.do?isPopUp=Y&defectCode='$filename 
google-chrome -new-tab 'splm.sec.samsung.net/wl/tqm/defect/defectreg/goDefectDetail.do?isPopUp=Y&defectCode='$filename
echo "make directory, opel url done":

# 파일 경로
file_path="/home-mc/wangkeun.oh/git_workspace/sec_repo/KinGoodWiki/plms.md"

# "END" 문자열이 있는 라인의 번호를 찾습니다.
line_number=$(grep -n -w -- "END" "$file_path" | cut -d: -f1)

# '|' 문자열을 생성합니다.
new_string="$filename"

pipe_string="| [$new_string]($new_string) | | | | | | | | | "

echo $line_number
echo $file_path
sed -i "$((line_number-1))s/|.\{0,\}$/&\n${pipe_string}/" "$file_path"
echo 'done'

exec bash #???, 이거 없으면 안되는군 이게 마지막에 있어야함.


#echo $filename >> /home-mc/wangkeun.oh/git_workspace/KinGoodWiki/plms.md
