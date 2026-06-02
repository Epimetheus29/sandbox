from fastapi import FastAPI

app = FastAPI(title="sandbox")


@app.get("/")
async def root():
    return {"message": "Welcome to Sandbox"}

@app.post("/string_changer/{text}")
async def string_changer(text:str):
    text = text.swapcase()
    return {"message": text}

@app.post("/bubble_sort/{numbers}")
async def bubble_sort(numbers:str):
    nums= string_parser_numbers(numbers)
    print(nums)
    n = len(nums)
    for i in range(0,n):
        for j in range(0,n-i-1):
            if (nums[j] > nums[j+1]):
                nums[j], nums[j+1] = nums[j+1], nums[j]
    
    return {"message":nums}

@app.post("/selection_sort/{numbers}")
async def selection_sort(numbers:str):
    nums = string_parser_numbers(numbers)
    print(nums)

    n = len(nums)
    for i in range(0,n):
        min_idx = i
        for j in range(i+1,n):
            if (nums[j]<nums[min_idx]):
                min_idx = j
        nums[i],nums[min_idx] = nums[min_idx],nums[i]
    return{"message":nums}


def string_parser_numbers(input: str) -> list|dict:
    nums = input.split(sep=',')
    try:
        parsed_nums = []
        for i in nums:
            try:
                parsed_nums.append(int(i))
            except ValueError:
                parsed_nums.append(float(i))
        return(parsed_nums)
    except ValueError:
        return {"message": "Found unsupported types in the Input"}