

def score_list_sum(books, flag_book_id):
    book_score = 0
    for book in books:
        if book[0] in flag_book_id:
            pass
        else:
            book_score += book[1]
    return book_score
    
def get_flagged_books(books, flag_book_id):
    flag_list_id = []
    flag_list_books = []
    for i in range(0,len(books)):
        if books[i][0] in flag_book_id:
            flag_list_id.append(i)
    for index in flag_list_id:
        flag_list_books.append(books[index])
        books.pop(index)
    books_sorted = sorted(books, key=lambda e: e[1], reverse=True)
    #print(books_sorted)
    return score_list_sum(books_sorted+flag_list_books, flag_book_id), books_sorted+flag_list_books 

def run_algo(scores, L, d):
         
  """
    scores: list of scores, where index is book id
    L: list of dicts, having properties of libraries
    d: int, deadline
  """
  flag_book_id = []
  
  # This is list of (id, score), whereas scores is list of score only
  #scores_sorted = sorted(enumerate(scores), key=lambda e: e[1], reverse=True)
  for i in range(0,2):
      L_list = []
      for library in L:
          #book_list = get_flagged_books(library["books"])
          book_score, book_list = get_flagged_books(library["books"], flag_book_id)
          library["books"] = book_list
          score = book_score*library["rate"]/library["signup"]
          L_list.append([score, library["id"],  book_list, library["signup"]])
      
      L_sorted = sorted(L_list, key=lambda e: e[0], reverse=True)
      selected_library = L_sorted[0]  
      
      
      for book in selected_library[2]:
          if book[0] in flag_book_id:
              pass
          else:
              flag_book_id.append(book[0])
    
      print(selected_library[3])
        
"""        
  
  
  for i in range(0, len(L)):
      if L[i]["id"] == selected_library[1]:
          remove_index= i
          break
  L.pop(remove_index)
  

"""
  #print(f"scores = {scores}")
  #print(f"scores_sorted = {scores_sorted}")
  #print(f"deadline d = {d}")

  #import json
  #print(f"libraries L = {json.dumps(L, indent=2)}")


