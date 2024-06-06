from person import Person


class PersonData:
    def __init__(self, data):
        self.people = [Person(person) for person in data]

    def total_people(self):
        return len(self.people)

    def longest_name(self):
        person = max(self.people, key=lambda p: len(p.name))
        return person.name, len(person.name)

    def oldest_living_person(self):
        living_people = [p for p in self.people if p.is_alive()]
        person = max(living_people, key=lambda p: p.age())
        return person.name, person.age()

    def oldest_deceased_person(self):
        deceased_people = [p for p in self.people if not p.is_alive()]
        person = max(deceased_people, key=lambda p: p.death_age())
        return person.name, person.death_age()

    def total_actors(self):
        return sum(1 for p in self.people if p.occupation == "näitleja")

    def born_in_year(self, year):
        return sum(1 for p in self.people if datetime.strptime(p.birth_date, "%Y-%m-%d").year == year)

    def unique_occupations(self):
        return len(set(p.occupation for p in self.people))

    def names_with_more_than_two_parts(self):
        return sum(1 for p in self.people if len(p.name.split()) > 2)

    def birth_death_same_except_year(self):
        return sum(1 for p in self.people if p.birth_date[5:] == p.death_date[5:])

    def living_and_deceased_count(self):
        living = sum(1 for p in self.people if p.is_alive())
        deceased = self.total_people() - living
        return living, deceased
