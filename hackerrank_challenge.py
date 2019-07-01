from statistics import mean
from collections import deque
import re
import email.utils
import numpy as np

from custom_lib.SortAgorithm import *
from custom_lib.utilities import *

DEQUE_METHODS = ["append"]

def find_runner_up_score(self):
    winner_score = max(self)
    max_score_occurences = self.count(winner_score)
    if max_score_occurences > 1:
        exclude_max_score = [item for item in self if item is not winner_score]
        runner_up_score = max(exclude_max_score)
    else:
        self.remove(winner_score)
        runner_up_score = max(self)
    return runner_up_score

def find_second_lowest_in_dict(dictionary):
    keys = sorted(dictionary.keys())
    lowest_score = min(dictionary.values())
    exclude_min_score = [item for item in dictionary.values() if item != lowest_score]
    second_lowest_score = min(exclude_min_score)
    print(*[item for item in keys if dictionary.get(item) == second_lowest_score], sep='\n')
    # list(map(lambda y: print(y), list(filter(lambda x: dictionary.get(x) == second_lowest_score, keys))))

def input_dict():
    n = int(input())
    dictionary = {}
    for _ in range(n):
        dictionary.update({input(): float(input())})
    return dictionary

def input_students():
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *grades = input().split()
        scores = list(map(float, grades))
        student_marks[name] = scores
    query_name = input()
    return student_marks, query_name

def calculate_average_grade(student_marks, name):
    marks = student_marks[name]
    # return mean(marks)
    return sum(marks)/len(marks)

def count_word_appearance():
    n = int(input())
    dictionary = {}
    words = []
    for _ in range(n):
        word = input()
        if dictionary.get(word) is not None:
            dictionary.update({word: dictionary.get(word) + 1})
        else:
            dictionary.update({word: 1})
            words.append(word)
    '''
    Print according to the requirements
    '''
    # print(len(words))
    # list(map(lambda value: print(value, end=' '), list(map(lambda key: dictionary.get(key), words))))

def deque_from_input():
    n = int(input())
    d = deque()
    for _ in range(n):
        inp = input().split()
        if len(inp) > 1:
            getattr(d, inp[0])(inp[1])
            continue
        getattr(d, inp[0])()
    return d
# print(*deque_from_input(), end=' ')

def is_sorted(iterable):
    return all(iterable[i] <= iterable[i+1] for i in range(len(iterable)-1))

'''
There is a horizontal row of  cubes. The length of each cube is given. You need to create a new vertical pile of cubes. The new pile should follow these directions: if  is on top of  then .
When stacking the cubes, you can only pick up either the leftmost or the rightmost cube each time. Print "Yes" if it is possible to stack the cubes. Otherwise, print "No". Do not print the quotation marks.
'''
def piling_cubes():
    n = int(input())
    for _ in range(n):
        d = deque()
        times = int(input())
        list(map(lambda x: d.append(x), map(int, input().split())))
        min_index = d.index(min(d))
        desc_part = list(d)[0:min_index]
        asc_part = list(d)[min_index:]
        desc_part.reverse()
        if is_sorted(desc_part) and is_sorted(asc_part):
            print("Yes")
            continue
        print("No")

def count_letter_appearance():
    word = input()
    dictionary = {}
    top_three = {}
    for letter in word:
        if dictionary.get(letter) is not None:
            dictionary.update({letter: dictionary.get(letter) + 1})
        else:
            dictionary.update({letter: 1})
    sorted_key_dict = sorted(dictionary.items(), key=lambda dict: dict[0])
    sorted_value_dict = sorted(sorted_key_dict, key=lambda dict: dict[1], reverse=True)
    top_three = sorted_value_dict[0:3]
    return list(map(lambda x: print(*x, sep=' '), top_three))

def list_comprehension():
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    result = [ [i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n]
    return print(result)

def find_substr_indices():
    target = input()
    regexcc = '(?=('+ input() +'))'
    result = re.finditer(regexcc, target)
    target_result = list(map(lambda match: match.regs[1], result))
    if target_result == []:
        return print((-1, -1))
    else:
        return print(*[(a, b - 1) for (a,b) in target_result], sep='\n')

def re_sub_regex_subtitution():
    n = int(input())
    for i in range(n):
        print(re.sub(r'(?<= )(&&|\|\|)(?= )', lambda x: 'and' if x.group() == '&&' else 'or', input()))

def validate_roman_num(parameter_list):
    hundred = '(C[MD]|D?C{0,3})'
    ten = '(X[CL]|L?X{0,3})'
    digit = '(I[VX]|V?I{0,3})'
    thousand = 'M{0,3}'
    regex_pattern =thousand + hundred+ten+digit +'$'
    print(str(bool(re.match(regex_pattern, input()))))

def validate_phone_num():
    phone_regex = '^[789][0-9]{9}$'
    validation = []
    n = int(input())
    for _ in range(n):
        validation.append(bool(re.match(phone_regex, input())))
    print(*list(map(lambda x: 'YES' if x is True else 'NO', validation)), sep='\n')

def validate_parse_mail(line=None):
    email_regex_validator = '^[a-zA-Z](\w|\.|-)*@[a-zA-Z]+\.[a-zA-Z]+'
    print(email.utils.parseaddr('DOSHI <DOSHI@hackerrank.com>'))
    if line is None:
        pass

#  region Interview challenges
def matching_socks():
    n = int(input())
    socks_pair = {}
    pair = 0
    socks = input().split()
    for sock in socks:
        if socks_pair.get(sock) is not None:
            socks_pair.update({sock: socks_pair.get(sock) + 1})
        else:
            socks_pair.update({sock: 1})
    for kind in socks_pair.keys():
        pair += socks_pair.get(kind)//2
    print(pair)

# Complete the countingValleys function below.
def counting_hills_valleys():
    n = int(input())
    s = input()
    curr_spot = 0
    valleys = 0
    hills = 0
    for step in s:
        if step is 'U':
            curr_spot += 1
            if curr_spot == 0:
                valleys += 1
        elif step is 'D':
            curr_spot -= 1
            if curr_spot == 0:
                hills += 1
    print(valleys)
    print(hills)

def cloud_jumping():
    n = int(input())
    clouds = list(map(int, input().split()))
    # c = input().split()
    curr = 0
    jumps = 0
    while curr < n:
        if curr<n-2 and clouds[curr+2] is 0:
            curr += 2
            jumps += 1
        elif curr != n-1:
            curr += 1
            jumps += 1
        else:
            curr += 1
    print(jumps)

def repeated_string():
    s, n = input(), int(input())
    a_ocurrence = s.count("a") * (n // len(s)) + s[:n % len(s)].count("a")
    print(a_ocurrence)

def hourglass_sum():
    arr = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    max_sum_arr = []
    for i in range(1, 5):
        for j in range(1, 5):
            max_sum_arr.append(arr[i-1][j-1] + arr[i-1][j] + arr[i-1][j+1] + arr[i][j] + arr[i+1][j-1] + arr[i+1][j] + arr[i+1][j+1])
    print(max(max_sum_arr))

def recursive_digit_sum():
    # http://applet-magic.com/digitsummod9.htm
    n, k = map(int, input().split())
    x = n * k % 9
    print(x if x else 9)

def counting_inversion():
    n = int(input())
    result = []
    for _ in range(n):
        arr_len = int(input())
        arr = list(map(int, input().rstrip().split()))
        swaps, sorted_arr = MergeSort.mergeSort(arr)
        result.append(swaps)
    print(*result, sep ='\n')

def left_rotation():
    n, no_rotation = map(int, input().split())
    arr = list(map(int, input().rstrip().split()))
    print(*shift(arr, 'left', no_rotation))


#endregion

# print(f'{calculate_average_grade(student_marks, query_name):.2f}')
if __name__ == '__main__':
    left_rotation()