books=[]
def add_book():
    title=input("Enter The Name Of The Book:")
    author=input("Author's Name:")
    year=input("Enter The Year That Published:")
    status=input("Read/Want To Read:")
    book={
        "title":title,
        "author":author,
        "year":year,
        "status":status
    }
    books.append(book)
def view_all_books():
    if not books:
        print("No Data Collected")
        return
    print("--All Books--\n")
    for i in books:
        print(f"{i['title']}|{i['author']}|{i['year']}|{i['status']}")
        print()
def filter_by_status():
    if not books:
        print("No Data Collected")
        return
    status=input("Status(Read or Want To Read):").lower().strip()
    flag=False
    for i in books:
        if i['status'].lower()==status:
            print(f"{i['title']}|{i['author']}|{i['year']}")
            flag=True
    if not flag:
        print(f"No Book with the  status:{status}")
def search_by_title():
    if not books:
        print("No Data Collected")
        return
    title=input("Enter The Name Of The Book:").lower().strip()
    flag=False
    for i in books:
        if i['title'].lower()==title:
            print(f"{i['author']}|{i['year']}|{i['status']}")
            flag=True
    if not flag:
        print(f"No Book with the  name:{title}")
def delete_book():
    if not books:
        print("No Recorded Books Yet")
        return
    delete=input(f"Enter the book to remove:").lower().strip()
    flag=False
    for book in books:
        if book['title'].lower()==delete:
            books.remove(book)
            print("Deleted The Book Successfully!")
            flag=True
            break
    if not flag:
        print("No Such book in the list")

while True:
    print("\n===Book Tracker===\n1.Add A Book\n2.View All Books\n3.Filter By Status\n4.Search By Title\n5.Delete A Book\n6.Exit")
    choice=input("Choose an option from 1-6:")
    if choice=='1':
        add_book()
    elif choice=='2':
        view_all_books()
    elif choice=='3':
        filter_by_status()    
    elif choice=='4':
        search_by_title()
    elif choice=='5':
        delete_book()
    elif choice=='6':
        print("Goodbye👋")
        break
    else:
        print("There is no such option you fool!!")
        
    


    


