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
 
[각 랩의 학점 평균 차이가 나지 않게 하기 위한 로직]