import requests


q = """
{
  website(url: "https://in.pycon.org") {
    title
    image
    description
  }
}
"""

resp = requests.post("http://localhost:5000/graphql", params={'query': q})
print(resp.text)
