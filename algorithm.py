
flag_book_set = set()
def score_list_sum(books):
    book_score = 0
    for book in books:
        book_score += book[1]
    return book_score
    
def get_book_order(books):
    remove_list = []
    for i in range(0, len(books)):
        if books[i] in flag_book_set:
            remove_list.append(books[i])
        
    return sorted(list(set(books)-set(remove_list)), key=lambda e: e[1], reverse=True)+remove_list 

def run_algo(scores, L, d):
         
  """
    scores: list of scores, where index is book id
    L: list of dicts, having properties of libraries
    d: int, deadline
  """
  # This is list of (id, score), whereas scores is list of score only
  #scores_sorted = sorted(enumerate(scores), key=lambda e: e[1], reverse=True)
  final_result = []
  global flag_book_set
  while d != 0:
      if len(L) == 0:
          break
      high_score = 0
      for i in range(0,len(L)):
          book_score =score_list_sum(L[i]["books"])
          score = book_score/L[i]["signup"]
          if score > high_score:
              L_index = i
              L_id = L[i]["id"]
              high_score = score
              book_list = L[i]["books"]
              signup_days = L[i]["signup"]
              
          
      L.pop(L_index)
      d -= signup_days
      
      book_sorted = get_book_order(book_list)
      flag_book_set.update(book_list)
      
      final_result.append({
            "lib_id": L_id,
            "books_order": [ book[0] for book in book_sorted ]
        })
      if d < 0:
          break
      
     
  return final_result