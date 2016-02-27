import json
import urllib, urllib2

def run_query(search_terms):



    # Specify the base
    root_url = 'http://www.omdbapi.com/'
    source = 'Web'

    # Wrap quotes around our query terms as required by the Bing API.
    # The query we will then use is stored within variable query.
    query = "'{0}'".format(search_terms)
    query = urllib.quote(query)

    # Construct the latter part of our request's URL.
    # Sets the format of the response to JSON and sets other properties.
    search_url = "{0}?s={1}".format(root_url,
        query)

    # Create our results list which we'll populate.
    results = []

    try:
        #connect to the server and read the response
        response = urllib2.urlopen(search_url).read()

        # Convert the string response to a Python dictionary object.
        json_response = json.loads(response)

        # Loop through each page returned, populating out results list.
        for result in json_response['Search']:
            results.append({
            'title': result['Title']})

    # Catch a URLError exception - something went wrong when connecting!
    except urllib2.URLError as e:
        print "Error when querying the OMDB API: ", e

    # Return the list of results to the calling function.
    return results

def main():
	# Query, get the results and create a variable to store rank.
	query = raw_input("Please enter a query: ")
	results = run_query(query)

	# Loop through our results.
	for result in results:
		# Print details.
		print result['title']
		print


if __name__ == '__main__':
	main()
