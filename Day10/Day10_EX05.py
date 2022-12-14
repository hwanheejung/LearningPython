"""
배열 arr가 주어집니다. 배열 arr의 각 원소는 숫자 0부터 9까지로 이루어져 있습니다. 이때, 배열 arr에서 연속적으로 나타나는 숫자는 하나만 남기고 전부 제거하려고 합니다. 단, 제거된 후 남은 수들을 반환할 때는 배열 arr의 원소들의 순서를 유지해야 합니다. 예를 들면,

arr = [1, 1, 3, 3, 0, 1, 1] 이면 [1, 3, 0, 1] 을 return 합니다.
arr = [4, 4, 4, 3, 3] 이면 [4, 3] 을 return 합니다.
배열 arr에서 연속적으로 나타나는 숫자는 제거하고 남은 수들을 return 하는 solution 함수를 완성해 주세요.

def solution(arr):
    answer = []
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')
    return answer
"""

def solution(arr):
    answer = []
    idx = 0

    while idx < len(arr) - 1:
        num = 1     # 비교해야할 개수
        n = 1       # 같은거
        while num <= len(arr) - idx - 1:
            if arr[idx] == arr[idx + num]:
                n += 1
            else:
                break
            num += 1
        answer.append(arr[idx])
        idx += n

    if arr[-2] != arr[-1]:
        answer.append(arr[-1])

    return answer


arr = [1, 1, 3, 3, 0, 1, 1]
print(solution(arr))






