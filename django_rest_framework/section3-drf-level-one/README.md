# Serializer
Serializer는 Queryset과 model instance같은 복잡한 데이터를 native Python 데이터 형식으로 변환하여 JSON과 같은 유용한 형식으로 쉽게 렌더링할 수 있도록 한다.
이 프로세스를 데이터의 직렬화라고 한다.

Serializer는 Serializer와 ModelSerializer 클래스를 사용하여 쉽게 사용할 수 있는 DRF의 매우 중요한 구성요소이다.

Serializer는 또한 deserialization를 제공하며, 먼저 들어오는 데이터의 유효성을 검사한 후 구문 분석된 데이터를 복잡한 유형으로 다시 변환할 수 있다.

Parser
- 나머지 API가 다른 종류의 요청을 수용하고 이해할 수 있도록 하는 클래스 
- DRF는 JSONParser 뿐만 아니라 이미지나 다른 종류의 파일을 보내고 받는데 사용할 수 있는 파서들도 제공한다.
- DRF는 header의 content-type를 기반으로 어떤 종류의 parser가 최적인지 자동으로 결정한다.

Renderer
- 다른 종류의 응답을 제공하거나 이를 개인화할 수 있다.
- Json Renderer, HTML Renderer 등등
