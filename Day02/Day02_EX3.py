# check


print("비가 오나요? 오면 1, 안오면 0을 입력하세요")
rain = input()
print(type(rain))   # check

print("눈은 오나요? 오면 1, 안오면 0을 입력하세요")
snow = input()
print(snow)     # check


if rain == "1" or snow == "1":
    print("약속을 취소하고 집에서 넷플릭스 볼게요")
else:
    print("날씨가 좋으니, 나가자")

