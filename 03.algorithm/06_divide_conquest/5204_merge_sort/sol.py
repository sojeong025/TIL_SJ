import sys
sys.stdin = open('input.txt')

def divide(number):
    if len(number) == 1:
        return number

    mid = len(number)//2

    left = divide(number[:mid])
    right = divide(number[mid:])
    return merge(left, right)


def merge(left, right):
    global cnt
    result = []

    if left[-1] > right[-1]:
        cnt += 1

    left_index = 0
    right_index = 0

    while len(left) > left_index or len(right) > right_index:
        if len(left) > left_index and len(right) > right_index:
            if left[left_index] <= right[right_index]:
                result.append(left[left_index])
                left_index += 1
            else:
                result.append(right[right_index])
                right_index += 1

        elif len(left) > left_index:
            result.append(left[left_index])
            left_index += 1

        elif len(right) > right_index:
            result.append(right[right_index])
            right_index += 1
    return result


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    number = list(map(int, input().split()))
    cnt = 0
    answer = divide(number)
    print(f'#{tc} {answer[n//2]} {cnt}')


