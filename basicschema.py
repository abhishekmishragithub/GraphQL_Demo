import graphene
import extraction
import requests


def extractdata(url):
    html = requests.get(url).text
    extracted = extraction.Extractor().extract(html, source_url=url)
    return extracted


class Website(graphene.ObjectType):
    url = graphene.String(required=True, description="simple web page url")
    title = graphene.String()
    description = graphene.String()
    image = graphene.String()
    feed = graphene.String()


class Query(graphene.ObjectType):
    website = graphene.Field(Website, url=graphene.String())

    def resolve_website(self, info, url='https://pycon.id/'):
        extracted = extractdata(url)
        print(extracted)
        return Website(url=url,
                       title=extracted.title,
                       description=extracted.description,
                       image=extracted.image,
                       feed=extracted.feed)


schema = graphene.Schema(query=Query)
