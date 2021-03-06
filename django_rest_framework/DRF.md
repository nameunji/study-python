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
    1. `serializers.StringRelatedField()` : ForgeignKey로 연결된 모델의 `__str__`메소드에서 정의한 string를 리턴
    2. 참조할 모델의 Serializer를 가져와서 사용
    3. `serializers.HyperlinkedRelatedField()`

<br><br>

# GenericAPIView & Mixins
- get, post 등 반복적으로 사용되는 view의 패턴을 파악하여 작성된 DRF의 GenericAPIView와 Mixin을 이용하면 쉽게 구현가능하다.

<br><br>

# Concrete View
- GenericAPIView와 Mixins을 이미 결합해 놓은 Concrete View 클래스를 하나만 상속해서 GenericAPIView & Mixins을 상속해서 작성한 코드와 동일한 기능을 수행하는 코드를 작성할 수 있다.
- Concrete View class는 이미 get, post, delete 등의 메소드를 내장하고 있기 때문에 get, post 함수 등을 작성할 필요가 없다.
- Customizing : ForeignKey로 연결된 데이터가 있을 때에는 `perform_create()`를 override해 줘야 한다.

<br><br>

# permission
- permission을 설정하지 않으면 누구나 접근할 수 있다.
```python
'DEFAULT_PERMISSION_CLASSES': [
    'rest_framework.permissions.AllowAny',
]
```
- 인증된 사용자만 접근하게 하려면,
```python
# settings.py
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ]
}
```
- 하지만 보통 서비스에선 특정 뷰 혹은 클래스 더 작은 단위로 쪼개서 인증을 요한다.

### No custom
- Views.py에서 permissions 모듈 임포트
- permission_classes에 사용할 permissions 클래스 명시
```python
class EbookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Ebook.objects.all()
    serializer_class = EbookSerializer
    permission_classes = [IsAdminUserOrReadOnly]
```
- IsAuthenticatedOrReadOnly
  - 누구나 Read는 가능하지만, CUD는 인증된 사용자만 접근가능하게 하는 클래스
  - 로그인한 유저가 해당 API에 접근하면 DRF API 웹화면에서 POST가 활성화되지만, 로그인 하지 않은 유저는 비활성화된다.

### Custom permission
- 액세스되어야할 경우 True를 리턴해야하고, 아닌 경우 False를 반환해야한다.
- request가 read인지, write인지 테스트해야하는 경우 'GET', 'OPTIONS' 및 'HEAD'를 포함하는 tuple형태의 'SAFE_METHODS'의 request method를 확인해야한다.

- has_permission(request, view)
  - APIView 접근시, 체크.
  - 거의 모든 Permission 클래스에서 구현되며 로직에 따라 True/False 반환
- has_object_permission(request, view, obj)
  - APIView의 get_object 함수를 통해 object 획득 시에 체크.
  - 브라우저를 통한 API 접근에서 CREATE/UPDATE Form 노출 시 체크
  - DjangoObjectPermissions에서 구현하며 로직에 따라 True/False 반환

```python
# permissions.py
from rest_framework import permissions

class IsAdminUserOrReadOnly(permissions.IsAdminUser):
    def has_permission(self, request, view):
        is_admin = super().has_permission(request, view)
        return request.method in permissions.SAFE_METHODS or is_admin

# views.py
class EbookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Ebook.objects.all()
    serializer_class = EbookSerializer
    permission_classes = [IsAdminUserOrReadOnly]
```
<br><br>

# Pagination
- permission을 설정한 것처럼 global 또는 local로도 설정가능하다.
