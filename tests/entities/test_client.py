from receipt_tracker.entities import client as c


def test_person_init():
    client = c.Client(id=1, fname="James", lname="Trew")

    assert client.id == 1
    assert client.fname == "James"
    assert client.lname == "Trew"


def test_person_from_dict():
    client = c.Client.from_dict(
        {
            'id': 1,
            'fname': "James",
            'lname': "Trew"
        }
    )

    assert client.id == 1
    assert client.fname == "James"
    assert client.lname == "Trew"


def test_client_to_dict():
    client_dict = {
        'id': 1,
        'fname': "James",
        'lname': "Trew"
    }

    client = c.Client.from_dict(client_dict)
    assert client.to_dict() == client_dict
