####### Problem 3 #######

test_cases = [('book', 'back'), ('kookaburra', 'kookybird'),
              ('elephant', 'relevant'), ('AAAGAATTCA', 'AAATCA')]
alignments = [('book', 'back'), ('kookaburra', 'kookybird-'),
              ('relev-ant', '-elephant'), ('AAAGAATTCA', 'AAA---T-CA')]


def MED(S, T):
  # TO DO - modify to account for insertions, deletions and substitutions
  if (S == ""):
    return (len(T))
  elif (T == ""):
    return (len(S))
  else:
    if (S[0] == T[0]):
      return (MED(S[1:], T[1:]))
    else:
      return (1 + min(MED(S, T[1:]), MED(S[1:], T)))


#just use insertion and deletion. count len of element, make table, for loop to build off of previous data, nums in table is # of total elements
def fast_MED(S, T,MED={}):
  MED={}
  def fast_MED_helper(i, j, MED):
    
    if (i, j) in MED:
        return MED[(i, j)]
    
    if i == len(S):
        return len(T) - j
    
    if j == len(T):
        return len(S) - i
   
    if S[i] == T[j]:
        MED[(i, j)] = fast_MED_helper(i+1, j+1, MED)
    
    else:
        insert = fast_MED_helper(i, j+1, MED)
        delete = fast_MED_helper(i+1, j, MED)
        MED[(i, j)] = 1 + min(insert, delete)
    
    return MED[(i, j)]
  return fast_MED_helper(0, 0, MED)


def fast_align_MED(S, T, MED={}):
  # TODO - keep track of alignment
  
  pass

  


def test_MED():
  for S, T in test_cases:
    assert fast_MED(S, T) == MED(S, T)


def test_align():
  for i in range(len(test_cases)):
    S, T = test_cases[i]
    align_S, align_T = fast_align_MED(S, T)
    assert (align_S == alignments[i][0] and align_T == alignments[i][1])


# for S, T in test_cases:
#   print(MED(S, T))



for S, T in test_cases:
  print(fast_MED(S, T))
