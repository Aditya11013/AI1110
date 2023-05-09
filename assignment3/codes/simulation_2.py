import random
def sim(k, N):
  trial_count = 0
  for i in range(N):
    # simulate a 5 question test
    test_count = 0
    for j in range(5):
      # we'll say you got it right if you get a 1, else it's wrong
      c = random.randint(1,3)
      if c == 1:
        test_count += 1
    # after the test see how many they got right, if it's k
    if test_count == k:
      trial_count += 1
  # after all the trials return the probability
  return trial_count/N
# getting 4 and 5 answers correct on a 5 Questions test
print(sim(4, 1_000_000),sim(5,1_000_000))
#probability of getting  k answers correct by guessing
four=sim(4,1_000_000)
five=sim(5,1_000_000)
#probability of getting four or more answers correct by guessing
greaterthanfour=four+five
print(greaterthanfour)
