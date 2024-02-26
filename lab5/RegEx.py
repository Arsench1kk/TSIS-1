#ex1
import re

l_str = 'cdfda'

x = re.search("ab*", l_str)
if x:
    print("Matched -", x.group())
else:
    print("Didn't match")

#ex2
import re

l_str = 'cdabbds'

x = re.search(r"ab{2,3}", l_str)
if x:
    print("Matched -", x.group())
else:
    print("Didn't match")

#ex3
import re
l_str = 'abdykhalyk_arsen45d_add'
x = re.findall("[a-z]+_[a-z]+", l_str)
if x:
    print("Matched, sequences:", x)
else:
    print("Didn't match")

#ex4
import re
l_str = "dsAbdukhalyk.;sdArsen8df"
x = re.findall("[A-Z][a-z]+", l_str)
if x:
    print("Sequences:", x)
else:
    print("Didn't match")

#ex5
import re
l_str = 'bdjaldsdb'
x = re.search("a.*b$", l_str)
if x:
    print("Sequences:", x.group())
else:
    print("Didn't match")

#ex6
import re

def test(pattern, text, testnum, result):
    res = re.sub(pattern, ':', text)
    print(res)
    if res == result:
        print(f'Test {testnum} passed!')
    else:
        print(f'Test {testnum} didn\'t pass')

pattern = r'[\s,.]'
test(pattern, 'my name, gl.,4', 1, 'my:name::gl::4')

#ex7
import re

def test(pattern, text, testnum, result):
    res = re.sub(pattern, lambda a: a.group('ch').upper(), text)
    print(res)
    if res == result:
        print(f'Test {testnum} passed!')
    else:
        print(f'Test {testnum} didn\'t pass')

pattern = r'_(?P<ch>.)'
test(pattern, 'l_str_fdew f_Re_ds_dop', 1, 'lStrFdew fReDsDop')

#ex8
import re

def test(pattern, text, testnum, result):
    res = re.split(pattern, text)
    print(res)
    if res == result:
        print(f'Test {testnum} passed!')
    else:
        print(f'Test {testnum} didn\'t pass')

pattern = '[A-Z]'
test(pattern, 'iDamAarsenFFsoFmy:R8thWex', 1, ['i', 'am', 'arsen', '', 'so', 'my:', '8th', 'ex'])

#ex9
import re

def test(pattern, text, testnum, result):
    res = re.sub(pattern, r'\1 \2', text)
    print(res)
    if res == result:
        print(f'Test {testnum} passed!')
    else:
        print(f'Test {testnum} didn\'t pass')

pattern = r'(?P<low>\w)(?P<upp>[A-Z])'
test(pattern, "MySuperTest", 1, "My Super Test")
test(pattern, " MySuperTest IAmRobot", 2, " My Super Test I Am Robot")

#ex10
import re

def test(pattern, func, text, testnum, result):
    res = re.sub(pattern, func, text)
    print(res)
    if res == result:
        print(f'Test {testnum} passed!')
    else:
        print(f'Test {testnum} didn\'t pass')

pattern = r'.[A-Z]'
change_to = lambda a: f'{a.group().lower()[0]}_{a.group().lower()[1]}'
test(pattern, change_to, 'YouTube, iPhone and eBay', 1, 'You_tube, i_phone and e_bay')