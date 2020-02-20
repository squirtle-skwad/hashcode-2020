

def score_list_sum(books):
    book_score = 0
    book_id_list = []
    for book in books:
        book_score += book[1]
        book_id_list.append(book[0])
    return book_score, book_id_list
    

def run_algo(scores, L, d):
         
  """
    scores: list of scores, where index is book id
    L: list of dicts, having properties of libraries
    d: int, deadline
  """
  
  # This is list of (id, score), whereas scores is list of score only
  #scores_sorted = sorted(enumerate(scores), key=lambda e: e[1], reverse=True)
  final_result = []
  while d != 0:
      if len(L) == 0:
          break
      L_list = []
      for library in L:
          #book_list = get_flagged_books(library["books"])
          book_score, book_id_list =score_list_sum(library["books"])
          score = book_score*library["rate"]/library["signup"]
          L_list.append([score, library["id"],  book_id_list, library["signup"]])
      
      L_sorted = sorted(L_list, key=lambda e: e[0], reverse=True)
      selected_library = L_sorted[0]  
      
      for i in range(0, len(L)):
          if L[i]["id"] == selected_library[1]:
              remove_index= i
              break
      L.pop(remove_index)
      d -= selected_library[3]
      
      if d < 0:
          break
      final_result.append({
            "lib_id": selected_library[1],
            "books_order": selected_library[2]
        })
     
  return final_result
        
"""        
  
  


"""
  #print(f"scores = {scores}")
  #print(f"scores_sorted = {scores_sorted}")
  #print(f"deadline d = {d}")

  #import json
  #print(f"libraries L = {json.dumps(L, indent=2)}")


