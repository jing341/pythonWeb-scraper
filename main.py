#자세한 내용은 https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range 에서 찾아보길 바란다.

"""
    python 에서 list는 값을 적고 다음 값을 적을 때는 , 를 적고 다음 값을 적는다.
        예
         days = ["Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun"]
"""

days = ["Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun"]
#days를 print 하면["Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun"] 라고 나온다.
print(days)

#그리고 [] 로 묶어주면 리스트가 되기 때문에 type을 확인해보면 days는 string이 아니라 list다.
print(type(days))

"""
    리스트에 값이 존재하는지 확인을 할 수도 있다. 그 값이 있으면 True로 없으면 False로 나온다.
    확인은 이렇게 한다. '값 in 리스트 이름'
      예
        "Mon" in days
        이렇게 하면 Mon 이라는 값이 days라는 리스트 안에 있는지 확인 할 수 있다.
        하지만 그 것이 True 인지 False 인지 알 수 없기 때문에 이렇게 해보겠다.
         예
            print("Mon" in days)
            이것은 사실이니 True가 나올 것이다.
    주의: 대소문자가 다르면 python은 다른 값으로 인식한다.
"""
print("Mon" in days)

"""
  리스트 이름[얻으려는 값의 순서] 라고 입력하면 그 리스트의 찾으려고자 하는 값을 얻을 수 있다.
  days 리스트 안에 Sat 이라는 값을 얻고 싶으면 이렇게 입력하면 된다.
    days[5]
    하지만 보이지 않을 것이기 때문에 이렇게 해보겠다.
    print(days[5])
     라고 입력하면 콘솔 창에 Sat 이라고 출력될 것이다.
     
  주의: 컴퓨터는 0부터 숫자를 센다. 그렇기 때문에 Mon 은 0 Tue는 1 이렇게 원래 순서에서 1을 빼주면 된다.
"""
print(days[5])

"""
리스트의 길이를 얻고 싶으면 이렇게 하면 된다.
len(리스트 이름)
이렇게 하면 리스트의 길이를 얻을 수 있다.
하지만 보이지 않기 때문에 이렇게 해보겠다.
  print(len(리스트 이름))
  let은 리스트의 값을 1부터 세고 길이를 출력한다.
"""

print(len(days))

"""
  리스트 이름.append(추가할 데이터) 라고 입력하면 선택한 이름을 가진 리스트에 () 안에 입력한 값이 추가된다.
  리스트는 수정할 수 있다.
"""

days.append(13948792837498)

print(days)

#리스트의 순서를 거꾸러 바꾼다.
days.reverse()
print(days)

#리스트 이름.clear() 이라고 입력하면 해당 리스트의 모든 아이템을 지운다.
days.clear()
print(days)