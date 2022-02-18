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
#Write a function that takes a single movie and returns True if its IMDB score is above 5.5
def func1(movies, film):
    isValid = False
    for f in movies: 
        if f["name"] == film and f["imdb"] > 5.5:
            isValid = True
    return isValid
#Write a function that returns a sublist of movies with an IMDB score above 5.5.
def func2(movies): 
    movies_list = []
    for f in movies: 
        if f["imdb"] > 5.5: 
            movies_list.append(f) 
    return movies_list

#Write a function that takes a category name and returns just those movies under that category.
def func3(movies, category): 
    movies_list = []
    for f in movies: 
        if f["category"] == category: 
            movies_list.append(f)
    return movies_list

#Write a function that takes a list of movies and computes the average IMDB score.
def func4(movies): 
    movies_score_list = []
    imbd_sum_score = 0.0
    for f in movies: 
        imbd_score = f["imdb"]
        movies_score_list.append(imbd_score)
        imbd_sum_score += imbd_score
    return (imbd_sum_score / len(movies_score_list))

#Write a function that takes a category and computes the average IMDB score.
def func5(movies, category): 
    movies_list = []
    imbd_sum_score = 0.0
    for f in movies: 
        if f["category"] == category: 
            movies_list.append(f)
            imbd_sum_score += f["imdb"]
    return (imbd_sum_score / len (movies_list))

print(func1(movies,"The Choice"))
print(func3(movies, "Romance"))
print(func2(movies)) 
print(func4(movies))
print(func5(movies, "Romance"))

