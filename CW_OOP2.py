# class User:
#     def __init__(self, password):
#         self.__password = None
#         self.password = password

#     @property
#     def password(self):
#         return self.__password
    
#     @password.setter
#     def password(self, value):
#         if not isinstance(value, str):
#             raise TypeError ('TYPE ERROR')
#         if len(str(value)) < 8:
#             raise TypeError ('ERROR')
#         self.__password = value

# user1 = User('mohammad202000')
# user2 = User('moha2000')
# user3 = User('moha20')
# # user1.password = '55552211'
# # user1.password = 555522
# # user1.password = '55551110000'











# class Book:
#     def __init__(self, id, title, price):
#         self.id= id
#         self.title=title
#         self.price=price
#         self.authors=[]

#     def add_author(self, author):
#         self.authors.append(author)

    
#     def show_authors(self):
#         self.show_info()
#         for author in self.authors:
#             print(author.name)

    
#     def show_info(self):
#         print( f"{self.title}, {self.id}, {self.price}")

# class PrintedBook(Book):
#     def __init__(self, id, title, price, page_count):
#         super().__init__(id,title, price)
#         self.page_count=page_count

   

# class EBook(Book):
#     def __init__(self, id, title, price, file_size):
#         super().__init__(id, title, price)
#         self.file_size = file_size



# class Author:
#     def __init__(self, name, email):
#         self.name=name
#         self.email=email


# a1=Author("J.K.Rolling", "rolling@.com")
# b1=Book(456, "harry potter", 1000)
# a2=Author("ali", "ali@.com")
# a3=Author("reza", "reza@.com")

# b1.add_author(a2)
# b1.add_author(a3)
# b1.add_author(a1)
# b1.show_authors()











class Post:
    def __init__(self, content, post_id, like=0, share=0):
        self.content = content
        self.post_id = post_id
        self.like = like
        self.share = share

    def show_full_info(self):
        return f"ID: {self.post_id} Content: {self.content}, Likes: {self.like}, Shares: {self.share}"

    def show_limited_info(self):
        return f"Content: {self.content}"


class Profile:
    def __init__(self, name, email, join_date,type):
        self.name = name
        self.email = email
        self.join_date = join_date
        self.type = type
        self.posts = []

    def create_post(self, post_id, content, like=0, share=0):
        post = Post(content, post_id, like, share)
        self.posts.append(post)

    def show_posts(self):
        raise NotImplementedError("Subclasses must implement this method")


class PremiumUser(Profile):
    def show_posts(self):
        return [post.show_full_info() for post in self.posts]

    def total_likes(self):
        return sum(post.like for post in self.posts)

    def total_shares(self):
        return sum(post.share for post in self.posts)

    def del_post(self, post_id):
        for post in self.posts:
            if post.post_id == post_id:
                self.posts.remove(post)
                return f"Post {post_id} deleted."
        return "Post not found."

    def edit(self, id, value):
        for post in self.posts:
            if post.post_id == id:
                post.content = value


class StandardUser(Profile):
    def show_posts(self):
        return [post.show_limited_info() for post in self.posts]



user1 =PremiumUser("name","email",2024,"permium")
user1.create_post(103,"hello world",20,25)
user1.create_post(104,"hello hell",20,25)

# print(user1.show_posts())
# print(user1.total_likes())
# print(user1.total_shares())
# print(user1.del_post(104))
print(user1.edit(103,"made in heaven"))
print(user1.show_posts())











class SchoolStaff:
    def __init__(self,name,role):
        self.name=name
        self.role=role

    def set_grade(self,student,grade):
        if self.role =="teacher" and 0<=grade<=20:
            student.grade=grade
        else:
            if self.role!="teacher":
                raise PermissionError
            if grade<0 or grade>20:
                raise ValueError()

class Student:
    def __init__(self,name,grade=None):
        self.name=name
        self.grade=grade
try:

    staff1=SchoolStaff("ali","cleaner")
    staff2=SchoolStaff("amir","teacher")
    student1=Student("mohamad")
    student2=Student("mahdi")
    staff2.set_grade(student1,12)
    print(student1.grade)

except Exception as e:
    print(f"error{e}")