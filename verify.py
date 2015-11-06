# coding=UTF-8
import re

def occour(pattern, content):
    if str(content).find(pattern) == -1:
        return  False
    return True

def equal(a, b):
    return a==b

# this is generator function
def re_search(pattern, expression, content):
    m = re.search(expression, content)
    if m is None:
        yield False

    ms = m.groups()
    for target in ms:
        # print '{0}'.format(target)
        if pattern == target:
            yield True

def re_search_all_equal(pattern, expression, content):
    for result in re_search(pattern, expression, content):
        if not result:
            return False
    return True
    
def re_match(expression, content):
    m = re.match(expression, content)

    if m is None:
        return False

    return True

# Test
def main():
    for result in re_search("24", r"(\d+)\.(\d+)", "24.1632"):
        print result

    print re_match( r"(\d+)\.(\d+)", "24.1632")

if __name__ == '__main__':
    main()