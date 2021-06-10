import urllib.request, json  # urlib.request help us create a connection to our api url and send a request, JSON format to dispaly api request
from .models import Movie

# We access the configuration objects by calling app.config['name_of_object']
# Getting api key
api_key = None

# Getting the movie base url
base_url = None


def configure_request(app):
    global api_key,base_url
    api_key = app.config['MOVIE_API_KEY']
    base_url = app.config['MOVIE_API_BASE_URL']

def get_movies(category):

    get_movies_url = base_url.format(
        category, api_key)  # fill the data respectivily
    # get_movies_url = 'https://api.themoviedb.org/3/movie/{}?api_key={}'.format(category, '6b2931ce73d6552995776353db108a22')
    with urllib.request.urlopen(get_movies_url) as url:

        get_movie_data = url.read()
        # change to dictonary using json load
        get_movie_response = json.loads(get_movie_data)

        movie_results = None

        if get_movie_response['results']:
            movie_results_list = get_movie_response['results']
            movie_results = process_results(movie_results_list)

    return movie_results

# returns a list from an array


def process_results(movie_list):
    '''
      transforms movie results to a list of objects
      returns a list of movie objects
    '''

    movie_results = []

    for movie_item in movie_list:
        id = movie_item.get('id')
        title = movie_item.get('title')
        overview = movie_item.get('overview')
        poster = movie_item.get('poster_path')
        vote_average = movie_item.get('vote_average')
        vote_count = movie_item.get('vote_count')

        if poster:
            movie_object = Movie(id, title, overview,
                                 poster, vote_average, vote_count)
            movie_results.append(movie_object)

    return movie_results


def get_movie(id):
    get_movie_details_url = base_url.format(id, api_key)

    with urllib.request.urlopen(get_movie_details_url) as url:
        movie_details_data = url.read()
        movie_details_response = json.loads(movie_details_data)

        movie_object = None

        if movie_details_response:
            id = movie_details_response.get('id')
            title = movie_details_response.get('original_title')
            overview = movie_details_response.get('overview')
            poster = movie_details_response.get('poster_path')
            vote_average = movie_details_response.get('vote_average')
            vote_count = movie_details_response.get('vote_count')

            movie_object = Movie(id, title, overview,
                                 poster, vote_average, vote_count)

    return movie_object  # returns the specific movie


def search_movie(movie_name):
    search_movie_url = 'https://api.themoviedb.org/3/search/movie?api_key={}&query={}'.format(
        api_key, movie_name)

    with urllib.request.urlopen(search_movie_url) as url:
        search_movie_data = url.read()
        search_movie_response = json.loads(search_movie_data)

        search_movie_results = None

        if search_movie_response['results']:
            search_movie_list = search_movie_response['results']
            search_movie_results = process_results(search_movie_list)

    return search_movie_results
