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

<br><br>


# two wrappers
Django REST Framework provides two wrappers we can use to write API Views
1. *@api_view* decorator  
    - for working with Function Based API Views
    - request instance를 수신하고, 적절한 response를 제공
    - request.data에 access할 때 발생하는 ParseError같은 예외에 대해 핸들링
    
2. *APIView* class
    - for working with Class Based API Views
 
<br><br>

# validation
how to specify custom validation checks for our models
모델에 대한 사용자 지정 유효성 검사 지정 방법
serializers using both Field-Level Validation and Object-Level Validation

- Object level validation
    - 여러 필드를 사용하여 유효성 검사
- Field level validation
    - 개체 내의 단일 필드에 대해 수행하는 검사
    - 예를들어 한 필드에 특정 단어가 사용되지 않았는지 확인하고 싶을 때가 있는데, 이때 사용된 경우 validation error 일으킬 수 있다.를
   
<br><br>

 
# ModelSerializer 
- ModelSerializer를 사용하면 정의한 모델을 기반으로 한 Serializer의 생성 속도를 높일 수 있다.
- ModelSerializer class는 models.py에서 생성한 모델을 기반으로 Serializer를 생성
- 이전 사례에서 Serializer를 만들 때, 각 필드를 하나하나 정의해 주었다. 마치 모델을 다시 한 번 작성하는 것 같은 불편함이 있었다. 이 문제를 해결해 주는 것이 ModelSerializer이다.
- ModelSerializer는 크게 아래와 같은 3가지 기능을 제공한다. 주는 편리함이 워낙 크기에 Base Serializer보다 훨씬 생산성을 높일 수 있다.
    - (의존하고 있는 모델에 기반해서) Serializer 필드를 자동으로 만들어 줌
    - Serializer를 위한 validator 제공 : ex) unique_together_validators
    - .create(), .update() 함수 기본으로 제공하여 다시 만들 필요 없음
    - 추가하고 싶은 필드가 있을 경우, serializer.SerializerMethodField()로 정의해 줌
    
<br><br>

# Nested Relationships
- ForeignKey필드를 사용하고자 할 때, 아무런 설정이 없으면 기본적으로 참조하고 있는 pk를 가져온다.
- 만약 pk값 외의 다른 값을 가져오고 싶다면
    1. `serializers.StringRelatedField()`
    2. 참조할 모델의 Serializer를 가져와서 사용
    3. `serializers.HyperlinkedRelatedField()`
