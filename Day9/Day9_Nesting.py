#리스트와 딕셔너리를 중첩시키자.
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again."
}


capitals = {
  "France": "Paris",
  "Germany": "Berlin",
}

#딕셔너리 안에 리스트를 넣어보자
travel_log = {
  "France": ["Paris", "Lille", "Dijon"],
  "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

#딕셔너리 안에 딕셔너리를 중첩시켜보자
travel_log = {
    "France": {"CitiesVisited":["Paris", "Lille", "Dijon"], "TotalVisits": 12},
    "Germany": {"CItiesVisited": ["Berlin", "Hamburg", "Stuttgart"], "TotalVisits": 4}
}

#리스트 안에 딕셔너리를 중첩시켜보자
travel_log = [
    {
        "country": "France", 
        "CitiesVisited":["Paris", "Lille", "Dijon"], 
        "TotalVisits": 12
    },
    {
        "country": "Germany", 
        "CItiesVisited": ["Berlin", "Hamburg", "Stuttgart"], 
        "TotalVisits": 4
    }
]
 