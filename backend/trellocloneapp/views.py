from . import models as md
from django.http import HttpResponse, HttpRequest, JsonResponse

#still need to add error handling

#for testing purposes only
def register_account(request: HttpRequest) -> HttpResponse:
    username: str = request.GET["username"]
    password: str = request.GET["password"]
    email: str = request.GET["email"]
    account: md.Account = md.Account(username = username, password = password, email = email)
    account.save()
    return HttpResponse(200)

#add authentication and error handling
def create_board(request: HttpRequest) -> HttpResponse:
    board_name: str = request.GET["name"]
    account_id: str = request.GET["accountId"]
    account: md.Account = md.Account.objects.get(id = account_id)
    board: md.Board = account.create_board(board_name)
    board.save()
    return HttpResponse(200)

#add authentication and error handling
def create_card(request: HttpRequest) -> HttpResponse:
    card_name: str = request.GET["name"]
    board_id: str = request.GET["boardId"]
    board: md.Board = md.Board.objects.get(id = board_id)
    card: md.Card = board.create_card(card_name)
    card.save()
    return HttpResponse(200)

#add authentication and error handling
def add_color_tag(request: HttpRequest) -> HttpResponse:
    color: str = "#" + request.GET["color"]
    card_id: str = request.GET["cardId"]
    card = md.Card.objects.get(id = card_id)
    color_tag: md.ColorTag = card.create_color_tag(color)
    color_tag.save()
    return HttpResponse(200)

def move_card(request: HttpRequest) -> HttpResponse:
    card_id: str = request.GET["cardId"]
    new_board_id: str = request.GET["boardId"]
    card: md.Card = md.Card.objects.get(id = card_id)
    board: md.Board = md.Board.objects.get(id = new_board_id)
    card.board = board
    card.save()
    return HttpResponse(200)

#add authentication and error handling
def get_boards(request: HttpRequest) -> JsonResponse:
    account_id: str = request.GET["accountId"]
    account: md.Account = md.Account.objects.get(id = account_id)
    boards = md.Board.objects.filter(account = account)
    json_response: list = []
    for board in boards:
        #get cards for this board
        cards = md.Card.objects.filter(board = board)
        cards_list: list = []
        for card in cards:
            #get color tags for each card
            color_tags = md.ColorTag.objects.filter(card = card)
            #build the card json entry
            card_entry: dict = {
                "id": card.id,
                "name": card.name,
                "status": card.status,
                "colorTags": [{"color": tag.color, "id": tag.id} for tag in color_tags]
            }
            cards_list.append(card_entry)
        #build the board json entry
        entry = {
            "id": board.id,
            "name": board.name,
            "status": board.status,
            "cards": cards_list
        }
        json_response.append(entry)
    return JsonResponse(json_response, safe = False)