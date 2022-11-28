# GUI Caculator

One Paragraph of project description goes here

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development purpose.

### Prerequisites

To execute the calculator, PyQt5 must be installed.

```
python -m pip install pyqt5
```
```
파이참 사용시 file -> settings -> project:파일 명 -> python interpreter -> + 버튼 -> pyqt5 설치
또는 run 설정 시 interpreter에서 설정
```

## Built With

* [PyQt5](https://pypi.org/project/PyQt5/) - The GUI framework used

## Contributing

Please read [CONTRIBUTING.md](https://github.com/shyoo17/gui_calculator/blob/main/CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Authors

* **studyingrabbit** - *Initial work* - [studyingrabbit](https://studyingrabbit.tistory.com/)
* **Seungho Yoo** - *Init repository* - this repository

See also the list of [contributors](https://github.com/shyoo17/gui_calculator/blob/main/CONTRIBUTORS.md) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## 개선된 기능

기준 - Windoews 계산기
- 기준에서 결과, CE 연산 이후 결과 연산을 할 때 entry로 추가 연산되는 기능
- exec 사용을 하지 않은 연산 기능
- 사칙연산 시 같은 연산을 취할 시 바로 연산되는 기능
- %는 나머지가 아닌 기준과 같이 설정. x,/ 연산시 퍼센테이지, +,- 연산시 피연산자간 곱의 퍼센테이지 연산 기능
- 그 외 negate, reverse, sqrt, sqr기능
- CE연산, 결과 연산 이후 숫자를 눌렀을 시 기록창이 초기화되고 피연산자 하나만 입력 후 결과를 출력 시 entry와 연산되는 기능
- 결과 연산 여러번 기능
- 소수, 정수 구별 기능
- 연산자 선택 이후 피연산자를 입력하지 않고 이전에 입력된 피연산자로 연산되는 기능
- etc

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
