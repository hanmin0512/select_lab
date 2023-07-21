### 랩 배정 프로그램
- 학과에서 랩 배정을 자동으로 해주는 프로그램을 짜달라는 요청에 만든 스크립트이다.

## Rule
- 1. 랩 신청서를 작성한 학생들이 있다.
  2. 랩 신청서를 작성하지 않은 학생들이 있다.
  3. 1 지망을 A랩을 신청한 할생들 중에 60%만 신청한 랩에 배정이 된다.
  4. 1 지망을 B랩을 신청한 학생들 중에 60%만 신청한 랩에 배정이 된다.
  5. 1 지망을 C랩을 신청한 학생들 중에 60%만 신청한 랩에 배정이 된다.
  6. 1 지망에 탈락한 할생들은 2 지망 후보에 넣어진다.
  7. 2 지망 후보들도 각 랩에 후보자들 중 60%만 2지망에 배정된다.
  8. 2지망에 탈락한 학생들은 3 지망 후보에 넣어진다.
  9. 3 지망 후보들도 각 랩에 후보자들 중 60%만 2지망에 배정된다.
  10. 3지망에 탈락한 학생들은 4 지망에 배정된다.
  11. 신청 안한 학생들은 학점이 높은 순으로 정렬된다.
  12. 순차적으로 A,B,C,D 랩에 배정된다.
  13. 총인원은 80 명 각 랩당 20명씩 배정
 
[각 랩의 학점 평균 차이가 나지 않게 하기 위한 로직]

## 사전 준비
- 학과 조교는 신청한 학생과 신청 안한 학생들을 한 액셀에 정리한다.
- 신청 안한 학생드은 1지망 2지망 3지망에 0 을 기입한다.


## 프로그램 테스트
- 테스트를 위해 예시 엑셀파일을 만들어주는 write.py 실행
- example.xlsx 생성된다.
- read.py 실행
- A.xlsx, B.xlsx, C.xlsx 생성
- 편차 확인

## 테스트 화면
- write.py read.py 실행 및 편차 출력 <Br>
![1](https://github.com/hanmin0512/select_lab/assets/37041208/6ed2fd13-824f-491c-bac2-cb490f3d61e3)

- example.xlsx
<img width="282" alt="스크린샷 2023-07-22 오전 1 01 55" src="https://github.com/hanmin0512/select_lab/assets/37041208/01da4862-357b-40ec-9881-0cf8de7d4ffc">

- A.xlsx B.xlsx C.xlsx D.xlsx 자동 배정된 랩
<img width="1256" alt="스크린샷 2023-07-22 오전 1 03 59" src="https://github.com/hanmin0512/select_lab/assets/37041208/2a2e5d08-6c11-4850-a4b5-6bade5ed6842">

