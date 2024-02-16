import requests
from advice import Todo
# api_url  = "https://api.adviceslip.com/advice"
# response =requests.get(api_url)

# print(response.status_code)
# if(response.status_code==200):
#     print(response.json())
#     print(response)
#     print(type(response.json()))
#     data=response.json()
#     # advice=data['slip']['advice']
#     advice=Advice(data)
#     print(advice)
#     print(type(advice))

#     def get_random_advice(url):
#         response =requests.get(url)
#         if(response.status_code==20):
#               data=response.json()
#               advice=data['slip']['advice']
#               print(advice)
#         else:
#             return None
        
# random_advice = get_random_advice(api_url)
# print(random_advice)

# api_url='https://catfact.ninja/fact'
# def get_advice(url):
#     response=requests.get(api_url)
#     if(response.status_code==200):
#         data=response.json()
#         fact=Fact(data)
#         return fact
#     else:
#         return None
    
# get_advice=get_advice(api_url)
# print(get_advice.facts)
# print(get_advice.length)

api_url='https://jsonplaceholder.typicode.com/todos/'
def get_todos(url):
    response=requests.get(api_url)
    if(response.status_code==200):
        data=response.json()
        todos = [Todo(item) for item in data]
        return todos    
    else:
        return None

todos = get_todos(api_url)

if todos is not None:
    for todo in todos:
        print(f"User ID: {todo.userId}, Title: {todo.title}")
else:
    print("Failed to retrieve todos.")