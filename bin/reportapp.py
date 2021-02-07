import requests


def main():

    choice = input("[R]eport weather or [s]ee reports? ")
    while choice:
        if choice.lower().strip() == 'r':
            report_events()
        elif choice.lower().strip() == 's':
            see_events()
        else:
            print(f"Don't know what to do with {choice}.")

        choice = input("[R]eport weather or [s]ee reports? ")


def report_events():
    desc = input("What is happening? ")
    city = input("What city ")
    data = {
        "description": desc,
        "location": {
            "city": city,
        }
    }

    url = "http://127.0.0.1:8081/api/reports"
    resp = requests.post(url, json=data)
    resp.raise_for_status()

    result = resp.json()
    print(f"Reported new event: {result.get('id')} ")


def see_events():
    url = "http://127.0.0.1:8081/api/reports"
    resp = requests.get(url)
    resp.raise_for_status()

    data = resp.json()

    for r in data:
        print(f"{r.get('location').get('city')} has {r.get('description')}")


if __name__ == '__main__':
    main()

    """
    {
        "description": "dffefefefeffef",
        "location": {
            "city": "LA",
            "state": "OR",
            "country": "US"
        },
        "id": "3d3014e0-d85d-44bd-a7ac-25424bb5a1e8",
        "created_date": "2021-02-07T18:57:51.608526"
    },
    {
        "description": "454545545",
        "location": {
            "city": "Portland",
            "state": "OR",
            "country": "US"
        },
        "id": "56b3f7ab-e60f-4124-9de3-47dd9540417a",
        "created_date": "2021-02-07T18:57:31.136185"
    }
    """