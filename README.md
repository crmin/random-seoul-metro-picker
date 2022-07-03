<h1 style="text-align: center">🚇 Random Seoul Metro Picker 🚇</h1>

수도권 지하철역을 랜덤하게 추출합니다.

# Scrap
수도권 지하철 데이터는 [Wikipedia](https://ko.wikipedia.org/wiki/수도권_전철역_목록)에서 가져옵니다.

* `scrap.py`에는 데이터 추출 관련 함수가 정의되어 있습니다.
* 해당 파일을 실행하면 wikipedia에서 데이터를 다운로드해서 `stations.csv`로 저장합니다. (필수는 아닙니다)

# Pick
* `stations.csv`를 shuffle한 후 n개를 추출합니다.
* 데이터 파일이 없다면 자동으로 다운로드해서 생성합니다.
* 실행 방법은 아래와 같습니다.
    ```
    python pick.py <뽑을 개수>
    ```
* `pick_stations()`를 직접 사용할 수 있습니다.
    * `pick_num`: 추출할 역 개수
    * `only_seoul`: 서울 지하철만 사용할지 여부

# License
* 코드는 [MIT License](https://github.com/crmin/random-seoul-metro-picker/blob/master/LICENSE)에 따라 사용할 수 있습니다.
* 추출된 wiki 데이터는 [크리에이티브 커먼즈 저작자표시-동일조건변경허락 3.0](https://ko.wikipedia.org/wiki/%EC%9C%84%ED%82%A4%EB%B0%B1%EA%B3%BC:Creative_Commons_Attribution-ShareAlike_3.0_Unported_License)로 사용할 수 있습니다. 이 코드에는 해당 데이터가 포함되지 않습니다.