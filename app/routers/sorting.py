from fastapi import APIRouter, HTTPException

from app.algorithms.parser import string_parser_numbers
from app.algorithms.sorting.bubble import bubble_sort
from app.algorithms.sorting.selection import selection_sort

router = APIRouter()


@router.post("/bubble_sort/{numbers}")
async def bubble_sort_route(numbers: str):
    try:
        nums = string_parser_numbers(numbers)
        return {"message": bubble_sort(nums)}

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.post("/selection_sort/{numbers}")
async def selection_sort_route(numbers: str):
    try:
        nums = string_parser_numbers(numbers)
        return {"message": selection_sort(nums)}

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )