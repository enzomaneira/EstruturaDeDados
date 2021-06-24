from collections import deque

you = ("enzo", "miguel", "alexandre", "michelle", "lourdes")
enzo = ("joao", "maria")


def search(name):
    search_queue = deque()
    search_queue += deque[name]
    searched = []
    while search_queue:
        person = search_queue.pop()
        if person not in searched:
            person_is_seller(person)
            if person_is_seller(person):
                print(f'{person} is a mango seller!')
                return True
            else:
                search_queue += deque[person]
                searched.append(person)
                return False


def person_is_seller(name):
    return name[-1] == "maria"


print(search(you))
