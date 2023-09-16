from aiohttp import ClientSession
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


# Create your views here.
class DictionaryView(View):
    async def fetch_data(self, word):
        baseurl = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
        # try:
        async with ClientSession() as session:
            async with session.get(baseurl) as response:
                if response.status == 200:
                    data = await response.json()
                    return render(self.request, "dict/define.html", {
                        "data": data[0]
                    })
                    # return JsonResponse(data[0])
                else:
                    return HttpResponse("Can't find the meaning of this", status=404)
        # except Exception as e:
        #     return HttpResponse("An error occurred: " + str(e), status=500)

    async def get(self, word):
        data = await self.fetch_data(word)
        return data


def sample(request):
    return render(request, "dict/sample.html", {
        "data": {
            "word": "data",
            "phonetic": "/ˈdaetə/",
            "phonetics": [
                {
                    "text": "/ˈdaetə/",
                    "audio": "https://api.dictionaryapi.dev/media/pronunciations/en/data-au-nz.mp3",
                    "sourceUrl": "https://commons.wikimedia.org/w/index.php?curid=35316551",
                    "license": {
                        "name": "BY-SA 4.0",
                        "url": "https://creativecommons.org/licenses/by-sa/4.0"
                    }
                },
                {
                    "text": "/ˈdætə/",
                    "audio": "https://api.dictionaryapi.dev/media/pronunciations/en/data-ca-ie-us.mp3",
                    "sourceUrl": "https://commons.wikimedia.org/w/index.php?curid=197143",
                    "license": {
                        "name": "BY-SA 3.0",
                        "url": "https://creativecommons.org/licenses/by-sa/3.0"
                    }
                },
                {
                    "text": "/ˈdeɪtə/",
                    "audio": "https://api.dictionaryapi.dev/media/pronunciations/en/data-ie-uk-us.mp3",
                    "sourceUrl": "https://commons.wikimedia.org/w/index.php?curid=197144",
                    "license": {
                        "name": "BY-SA 3.0",
                        "url": "https://creativecommons.org/licenses/by-sa/3.0"
                    }
                },
                {
                    "text": "/ˈdaetə/",
                    "audio": "https://api.dictionaryapi.dev/media/pronunciations/en/data-au-nz.mp3",
                    "sourceUrl": "https://commons.wikimedia.org/w/index.php?curid=35316551",
                    "license": {
                        "name": "BY-SA 4.0",
                        "url": "https://creativecommons.org/licenses/by-sa/4.0"
                    }
                },
                {
                    "text": "/ˈdeɪtə/",
                    "audio": "https://api.dictionaryapi.dev/media/pronunciations/en/data-ie-uk-us.mp3",
                    "sourceUrl": "https://commons.wikimedia.org/w/index.php?curid=197144",
                    "license": {
                        "name": "BY-SA 3.0",
                        "url": "https://creativecommons.org/licenses/by-sa/3.0"
                    }
                },
                {
                    "text": "/ˈdeɪtə/",
                    "audio": "https://api.dictionaryapi.dev/media/pronunciations/en/data-ie-uk-us.mp3",
                    "sourceUrl": "https://commons.wikimedia.org/w/index.php?curid=197144",
                    "license": {
                        "name": "BY-SA 3.0",
                        "url": "https://creativecommons.org/licenses/by-sa/3.0"
                    }
                }
            ],
            "meanings": [
                {
                    "partOfSpeech": "noun",
                    "definitions": [
                        {
                            "definition": "(plural: data) A measurement of something on a scale understood by both the recorder (a person or device) and the reader (another person or device). The scale is arbitrarily defined, such as from 1 to 10 by ones, 1 to 100 by 0.1, or simply true or false, on or off, yes, no, or maybe, etc.",
                            "synonyms": [],
                            "antonyms": []
                        },
                        {
                            "definition": "(plural: data) A fact known from direct observation.",
                            "synonyms": [],
                            "antonyms": []
                        },
                        {
                            "definition": "(plural: data) A premise from which conclusions are drawn.",
                            "synonyms": [],
                            "antonyms": []
                        },
                        {
                            "definition": "(plural: datums) A fixed reference point, or a coordinate system.",
                            "synonyms": [],
                            "antonyms": []
                        }
                    ],
                    "synonyms": [],
                    "antonyms": []
                }
            ],
            "license": {
                "name": "CC BY-SA 3.0",
                "url": "https://creativecommons.org/licenses/by-sa/3.0"
            },
            "sourceUrls": [
                "https://en.wiktionary.org/wiki/data",
                "https://en.wiktionary.org/wiki/datum"
            ]
        }
    })
