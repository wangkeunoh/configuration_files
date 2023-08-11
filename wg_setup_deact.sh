#!/bin/bash

archive_file=$(find . -maxdepth 1 -type f -name "*.zip")

if [ -z "$archive_file" ]; then
    echo "현재 폴더에 압축 파일이 존재하지 않습니다."
    exit 1
fi

# 7z 명령어로 압축 풀기
7z x "$archive_file"

echo "압축 풀기 성공 했습니다."

rg SETUP_DATA_CALL\|DEACTIVATE_DATA_CALL > pdn_open_close.wg

echo "pdn_open_close.wg 작성완료"

sed 's/.*\([0-9][0-9]-[0-9][0-9] [0-9][0-9]:[0-9][0-9]:[0-9][0-9]\)\(.*\)/\1\2/' pdn_open_close.wg > pdn_open_close_report.wg

sort -o pdn_open_close_report.wg -t ' ' -k 1,1 -k 2,2 pdn_open_close_report.wg

# < SETUP_DATA_CALL 포함된 문자열 이면 linkStatus포함 뒤다 지우되 10글자 남기는
process_lines() {
    while IFS= read -r line; do
        if [[ $line == *"< SETUP_DATA_CALL"* ]]; then
            processed_line=$(echo "$line" | sed 's/linkStatus=.*\(.\{10\}\)/\1/')
            echo "$processed_line" >> pdn_open_close_report2.wg
        elif [[ $line == *"> SETUP_DATA_CALL"* ]]; then
            processed_line=$(echo "$line" | sed 's/\(.*DataProfile=.\(.\{30\}\)\).*\(.\{10\}$\)/\1\3/')
            echo "$processed_line" >> pdn_open_close_report2.wg
        else
            echo "$line" >> pdn_open_close_report2.wg
        fi
    done < pdn_open_close_report.wg
}

process_lines
echo "File pdn_open_close_report.wg processed and result aved to pdn_open_close_report2.wg"


