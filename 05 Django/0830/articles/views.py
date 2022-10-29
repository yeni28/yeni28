import random
from django.shortcuts import render

# Create your views here.
def index(request):
    #request : 사용자의 요청 정보가 담겨있다.abs(
    # render는 화면을 만들어주는 함수
    # 사용자에게 보여줄 화면 html 함수이름
    return render(request, 'articles/index.html')

def greeting(request):
    foods = ['사과', '바나나','코코넛']
    info = {'name':'김예은'}
    # 각 데이터들을 다시 context 라는 큰 딕셔너리로 묶은 다음
    context = {
        'foods' : foods,
        'info' : info
    }
    # 큰 딕셔너리인 context를 return해준다
    return render(request, 'articles/greeting.html', context)
    #name은 변수 이름이 되는 것, 오른쪽의 값이 자리에 오게됨


def dinner(request):
    foods =['족발', '햄버거', '치킨', '초밥']
    pick = random.choice(foods)
    intro = "어떤 메뉴를 먹어야 잘 먹었다고 소문이 날까요?"
    my_number = random.choice(range(1,101))
    context = {'pick' : pick,'foods' : foods, 'texts' : intro, 'number': my_number}
    return render(request, 'articles/dinner.html', context)

def throw(request):
    return render(request, 'articles/throw.html')

def catch(request):
    print(request)
    print(type(request))
    print(request.GET)
    print(request.GET.get('message'))

    message = request.GET.get('message')
    context = {'message' : message}

    return render(request, 'articles/catch.html', context)

def hello(request, name):
    context = {
        'name' : name,
    }
    return render(request, 'articles/hello.html', context)