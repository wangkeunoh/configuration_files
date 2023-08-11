#include <iostream>
#include <fstream>
#include <string>

int main() {
  std::ifstream input_file("input.txt");  // 입력 파일 열기
  std::string line, filename;
  
  while (std::getline(input_file, line)) {  // 파일에서 각 줄을 읽어옴
    // 파일경로와 파일명 분리
    size_t last_slash = line.find_last_of("/\\");
    if (last_slash != std::string::npos) {  // 파일경로가 있는 경우
      filename = line.substr(last_slash + 1);  // 파일명 저장
    } else {  // 파일경로가 없는 경우
      filename = line;  // 전체 문자열을 파일명으로 저장
    }
    std::cout << filename << std::endl;  // 파일명 출력
  }
  
  
  return 0;
}
