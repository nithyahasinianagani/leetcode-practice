
def person_lister(f):
    def inner(people):
        people.sort(key=lambda person: int(person[2]))
        return [f(person) for person in people]
    return inner

@person_lister
def name_format(person):
    title = "Mr." if person[3] == "M" else "Ms."
    return f"{title} {person[0]} {person[1]}"

people = [input().split() for _ in range(int(input()))]

print(*name_format(people), sep="\n")
