movies = [ 
{ 
"name": "Usual Suspects",  
"imdb": 7.0, 
"category": "Thriller" 
}, 
{ 
"name": "Hitman", 
"imdb": 6.3, 
"category": "Action" 
}, 
{ 
"name": "Dark Knight", 
"imdb": 9.0, 
"category": "Adventure" 
}, 
{ 
"name": "The Help", 
"imdb": 8.0, 
"category": "Drama" 
}, 
{ 
"name": "The Choice", 
"imdb": 6.2, 
"category": "Romance" 
}, 
{ 
"name": "Colonia", 
"imdb": 7.4, 
"category": "Romance" 
}, 
{ 
"name": "Love", 
"imdb": 6.0, 
"category": "Romance" 
}, 
{ 
"name": "Bride Wars", 
"imdb": 5.4, 
"category": "Romance" 
}, 
{ 
"name": "AlphaJet", 
"imdb": 3.2, 
"category": "War" 
}, 
{ 
"name": "Ringing Crime", 
"imdb": 4.0, 
"category": "Crime" 
}, 
{ 
"name": "Joking muck", 
"imdb": 7.2, 
"category": "Comedy" 
}, 
{ 
"name": "What is the name", 
"imdb": 9.2, 
"category": "Suspense" 
}, 
{ 
"name": "Detective", 
"imdb": 7.0, 
"category": "Suspense" 
}, 
{ 
"name": "Exam", 
"imdb": 4.2, 
"category": "Thriller" 
}, 
{ 
"name": "We Two", 
"imdb": 7.2, 
"category": "Romance" 
} 
] 
#ex1 
def movie_55(name): 
    for movie in movies: 
        if movie['name'] == name: 
            return movie['imdb'] > 5.5 
    return False 
 
print(movie_55("Usual Suspects")) 
 
#ex2 
def movie55_list(): 
    list_55_movies = [] 
    for movie in movies: 
        if movie['imdb'] > 5.5: 
            list_55_movies.append(movie['name']) 
    return list_55_movies 
 
print(movie55_list()) 
 
#ex3 
def movies_category(category): 
    filtered_movies = [] 
    for movie in movies: 
        if movie['category'] == category: 
            filtered_movies.append(movie) 
    return filtered_movies 
 
print(movies_category("Suspense")) 
 
#ex4 
def avarage_imdb(): 
    avarage = 0 
    for movie in movies: 
        avarage = avarage + movie['imdb'] 
    return (avarage / len(movies)) 
 
print(avarage_imdb()) 
 
#ex5 
def avarage_category(category): 
    avarage = 0 
    count = 0 
    for movie in movies: 
        if movie['category'] == category: 
            avarage = avarage + movie['imdb'] 
            count = count + 1 
    return (avarage / count) 
print(avarage_category("Romance"))