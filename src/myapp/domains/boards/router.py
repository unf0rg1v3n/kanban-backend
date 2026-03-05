from fastapi import APIRouter, Query, Path, Header, HTTPException, Depends
from myapp.db.core import SessionDep
from myapp.domains.boards.service import BoardService
from myapp.domains.boards.schemas import BoardRead, BoardCreate
from myapp.domains.boards.repositories import PostgresBoardRepository
from typing import List


def get_board_service(session: SessionDep) -> BoardService:
    return BoardService(PostgresBoardRepository(session))


router = APIRouter(prefix="/boards", tags=["boards"])

@router.post("/", response_model=BoardRead, summary="Create a new board")
async def create_board(board_create: BoardCreate, 
                       service: BoardService = Depends(get_board_service)):
    return await service.create_board(board_create)


@router.get("/", response_model=List[BoardRead])
async def get_board(service: BoardService = Depends(get_board_service)):
    return await service.get_all()


@router.get("/{board_id}", response_model=BoardRead)
async def get_board_by_id(board_id: int,
                          service: BoardService = Depends(get_board_service)):
    board = await service.get_by_id(board_id)
    if not board:
        raise HTTPException(status_code=404, detail="Board not found")
    return board



# @router.get("/search")
# def search(q: str = Query(..., min_length=2), limit: int = Query(default=10)):
#     """ Search boards by title """
    
#     return {"q": q, "limit": limit}


# @router.get("/meta")
# def get_meta(x_token: str | None = Header(default=None, alias="X-Token")):
#     """ Get custom header X-Token """

#     return {"X-Token": x_token}


# @router.get("", summary = "Get all books")
# def get_books(q: str = Query(default=None, min_length=2), limit: int = Query(default=10, ge=1, le=100)):
#     """ Get all books, with optional filtering by title """
    
#     if q is not None:
#         books_filtered = [book for book in books if q.lower() in book.title.lower()]
#     else:
#         books_filtered = books
#     return books_filtered[0:limit]


# @router.get("/{book_id}",
#          response_model=Book,
#          summary = "Get a book by its ID")
# def get_book(book_id: int = Path(..., gt=0)):
#     """ 
#     Docstring for get_book

#     :param book_id: Description
#     :type book_id: int
#     """

#     idx = book_id - 1
    
#     if idx > len(books) or idx < 0:
#         raise HTTPException(status_code=404, detail="Book not found")
    
#     return books[idx]


# @router.post("", summary="Add a new book")
# def create_book(book: BookCreate):
#     """
#     Docstring for create_book
    
#     :param book: Description
#     :type book: BookCreate
#     """
#     if any(_book.title == book.title and _book.author == book.author for _book in books):
#         raise HTTPException(status_code=409, detail="Book already exists")
    
#     new = Book(id=len(books)+1, title=book.title, author=book.author)
#     books.append(new)

#     return new