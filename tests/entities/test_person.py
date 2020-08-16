from receipt_tracker.entities import person as p


def test_person_init():
    person = p.Person(id=1, fname="James", lname="Trew")

    assert person.id == 1
    assert person.fname == "James"
    assert person.lname == "Trew"


def test_person_from_dict():
    person = p.Person.from_dict(
        {
            'id': 1,
            'fname': "James",
            'lname': "Trew"
        }
    )


def test_person_to_dict():
    person_dict = {
        'id': 1,
        'fname': "James",
        'lname': "Trew"
    }

    person = p.Person.from_dict(person_dict)
    assert person.to_dict() == person_dict
