def load_data(filename):
  with open(filename) as f:
    l = f.readline()
    # Number of books, Number of libraries, Deadline
    nB, nL, d = map(int, l.split())

    l = f.readline()
    # List of book scores
    scores = list(map(int, l.split()))

    # List of libraries, dictionaries
    L = list()
    for _ in range(nL):
      l = f.readline()
      # Number of books, Signup process days, Rate of shipping
      LnB, sD, r = map(int, l.split())

      l = f.readline()
      # Book indices
      bs = list(map(int, l.split()))

      # Sorted books
      bs_sorted = list(sorted(enumerate(bs), key=lambda e: e[1], reverse=True))

      L.append({
        "num_books": LnB,
        "books": bs_sorted,
        "signup": sD,
        "rate": r,
      })

  return scores, L, d
