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
    nums = numbers.split(sep=',')
    try:
        parsed_nums = []
        for i in nums:
            try:
                parsed_nums.append(int(i))
            except ValueError:
                parsed_nums.append(float(i))
        nums = parsed_nums
    except ValueError:
        return {"message": "Found unsupported types in the Input"}
    print(nums)
    n = len(nums)
    for i in range(0,n):
        for j in range(0,n-i-1):
            if (nums[j] > nums[j+1]):
                nums[j], nums[j+1] = nums[j+1], nums[j]
    
    return {"message":nums}