# Working with APIs

Here, we will learn how to write a self-contained program that generates a visualization based on data it retrieves. We will use an _application programming interface_ (__API__) to automatically request specific information from a website and then use that information to generate a visualization.

## Using an API

An API is a part of a website designed to interact with programs. Those programs use very specific URLs to request certain information. This kind of request is called an __API call__

The requested data will be returned in an easily processed format, such as JSON or CSV. Most apps that use external data sources, such as apps that integrate with social media sites, rely on API calls.

### Git and GitHub

For this case, we will use GitHub's API to request information about Python projects on the site, and then generate an interactive visualization of the relative popularity of these projects using Plotly.

GitHub takes its name from Git, a distributed version control system created by __Linus Torvalds__, the creator of Linux. Git allows multiple developers to work on the same codebase simultaneously without interfering with each other's changes. 

GitHub is a web-based platform that hosts Git repositories and provides additional features such as issue tracking, project management, and collaboration tools.

### Requesting Data Using an API Call

GitHub's API allows users to request a wide range of information through API calls.

We can explore how an API call looks like by entering the following code into our browser's address bar and pressing ENTER:

```
https://api.github.com/search/repositories?q=language:python+sort=stars
```

This call returns the number of Python projects currently hosted on GitHub, as well as information about the most popular Python repositories.

`https://api.github.com/` is the base URL for GitHub's API and works to direct the request to the part of GitHub that responds to API calls. The next part, `search/repositories`, tells the API to conduct a search through all the repositories on GitHub. 

The question mark (`?`) after `repositories` signals that we are about to pass an argument. The `q` stands for __query__, and the equal sign (`=`) lets us begin specifying a query (`q=`). In this case, we are querying for repositories that use the Python programming language (`language:python`). The plus sign (`+`) acts as a logical AND operator, allowing us to add another condition to our query. The second condition specifies that we want the results sorted by the number of stars (`sort=stars`).

When we enter this URL into our browser, we receive a JSON response containing information about Python repositories on GitHub, including their names, descriptions, star counts, and more.

```json
{
  "total_count": 25743069,
  "incomplete_results": false,
  "items": [
    {
      "id": 54346799,
      "node_id": "MDEwOlJlcG9zaXRvcnk1NDM0Njc5OQ==",
      "name": "public-apis",
      "full_name": "public-apis/public-apis",
      "private": false,
      "owner": {
        --- more data here ---
```

### Installing Requests and Processing an API Response

The `requests` package allows a Python program to easily request information from a website and examine the response. 

Now, we can write a program to automatically issue an API call and process the results:

```python

import requests

# Make an API call and check the response
url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort=stars+stars:>10000"

headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Convert the response object to a dictionary
response_dict = r.json()

# Process results
print(response_dict.keys())

```

In the previous code, we ask GitHub to only look for repositories with more than 10,000 stars. 

We get a status code of `200` which indicates a successful response. We then ask the API to return the information in JSON format, so we use the `json()` method to convert the information to a Python dictionary. 

```
Status code: 200
dict_keys(['total_count', 'incomplete_results', 'items'])
```

### Working with the Response Dictionary

Since we have the information needed, we can work with the data stored there. 

```python

import requests

# Make an API call and check the response
url = "https://api.github.com/search/repositories"
url += "?q=language:python+stars:>10000&sort=stars"

headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Convert the response object to a dictionary
response_dict = r.json()

print(f"Total repositories: {response_dict['total_count']}")
print(f"Complete results: {not response_dict['incomplete_results']}")

# Explore information about the repositories
repo_dicts = response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")

# Examine the first repository
repo_dict = repo_dicts[0]
print(f"\nKeys: {len(repo_dict)}")

for key in sorted(repo_dict.keys()):
    print(key)