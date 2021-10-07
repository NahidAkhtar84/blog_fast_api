# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
#
# from fastapi import FastAPI
# from typing import Optional
# from pydantic import BaseModel
#
# app = FastAPI()
#
# @app.get('/')
# def index():
#     return {'data': {
#             'name': 'nahid'
#         }
#     }
#
# @app.get('/about')
# def about():
#     return {
#         'data': 'about page'
#     }
#
# @app.get('/blogs')
# def blogs(limit=10, published: bool=True, sort: Optional[str]=None):
#     if published:
#         return {'data': {
#                 f'{limit} published blogs are showing!'
#             }
#         }
#
#     else:
#         return {'data': {
#                 f'{limit} blogs are showing!'
#             }
#         }
#
#
# @app.get('/blog/unpublished')
# def unpublished():
#     return {
#         'data': 'All unpublished blogs'
#     }
#
# @app.get('/blog/{id}')
# def show(id: int):
#     return {
#         'blog id': id
#     }
#
# @app.get('/blog/{id}/comments')
# def comments(id, limit=10):
#     return {
#         'comments': {'1', '2'}
#     }
#
#
# # Blog creation
# class Blog(BaseModel):
#     title: str
#     body: str
#     published: Optional[bool]
#
# @app.post('/blog')
# def create_blog(blog: Blog):
#     return blog