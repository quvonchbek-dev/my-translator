import googletrans
from rest_framework.decorators import api_view
from rest_framework.response import Response


def translate_text(dist, src, text):
    return googletrans.Translator().translate(text=text, dest=dist, src=src).text


@api_view(['GET', 'POST'])
def getdata(request):
    data = request.data
    if data.get('dist'):
        resp = {
            "state": "ok",
            "text": translate_text(data["dist"], data["src"], data["text"]) if len(data["text"]) else ""
        }
    else:
        resp = {
            "dist": "en",
            "src": "uz",
            "text": "Salom! Ishlar qalay?"
        }

    return Response(resp)


@api_view(['POST'])
def post(request):
    data = request.data
    resp = {
        "state": "ok",
        "text": translate_text(data["dist"], data["src"], data["text"])
    }
    return Response(resp)
