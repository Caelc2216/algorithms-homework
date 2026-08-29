# Cael Church
# SE-4230
# Aug 28 2026

import pytest
import random
import time
import statistics

def built_in_sorted(a):
   a[:] = sorted(a)

def in_place_sort(a):
   a.sort()

# bad
def do_nothing(a):
   pass

def make_two_copies(a):
   return list(a) * 2

def quadratic_garbage(a):
   for i in range(len(a)):
      for j in range(len(a)):
            a[i], a[j] = a[j], a[i]

def reverse_sorted(a):
   return list(reversed(sorted(a)))

def unchanged(a):
   return a

def bubble_sort(l):
   swaped = False
   for i in range(len(l)):
      for j in range(i+1, len(l)):
         if l[j] < l[i]:
            l[i], l[j] = l[j], l[i]
            swaped = True
   if swaped == True:
      bubble_sort(l)

def selection_sort(l, index_to_start = 0):
   if len(l) != 0:
      smallest_num_index = index_to_start
      for i in range(index_to_start, len(l)):
         if l[i] < l[smallest_num_index]:
            smallest_num_index = i
      l[smallest_num_index], l[index_to_start] = l[index_to_start], l[smallest_num_index]
      if index_to_start!=len(l)-1:
         selection_sort(l, index_to_start = index_to_start + 1)

def insertion_sort(l):
   sorted = []
   for i in range(len(l)):
      sorted.append(l[i])
      index = i
      for j in reversed(range(len(sorted))):
         if j-1 >= 0:
            if sorted[j] < sorted[j-1]:
               sorted[j], sorted[j-1] = sorted[j-1], sorted[j]
               l[index], l[index-1] = l[index-1], l[index]
               index = index-1

def merge_sort_rec(l):
   return l

def quick_sort_rec(l):
   return l

def counting_sort(l):
   return l




@pytest.mark.parametrize("original", [
   [],
   [1],
   [1,2],
   [2,1],
   [1,2,3],
   [1,3,2],
   [2,1,3],
   [2,3,1],
   [3,1,2],
   [3,2,1]
])
def test_all(original):
   for sort in sorts:
      a = list(original)
      sort(a)
      assert a == sorted(original), f"failed to sort {original} with {sort.__name__}."

def time_sort(original, prep, sort):
   a = prep(list(original))
   start = time.perf_counter()
   sort(a)
   end = time.perf_counter()
   return end - start

def aggregated_time_sort(lists, length, prep, sort, repetitions, timeout):
   return statistics.median(
      [time_sort(a[:length], prep, sort, timeout)
            for a in lists
            for _ in range(repetitions)])

import pandas as pd

sorts = [bubble_sort, selection_sort, insertion_sort]
if __name__ == '__main__':
   random.seed(4567)
   preps = [sorted, reverse_sorted, unchanged]
   num_lengths = 7
   length_base = 10
   max_value = 2 ** 10
   max_length = length_base ** (num_lengths - 1)
   random_lists = [[random.randint(0, max_value) for _ in range(max_length)] for _ in range(3)]
   lengths = [length_base**k for k in range(num_lengths)]
   repetitions = 3
   timeout = 0.01
   results = []
   for prep in preps:
      print(f'\n{prep.__name__}')
      for sort in sorts:
            print(f'\n\t{sort.__name__}', end='')
            for length in lengths:
               median_time = aggregated_time_sort(lists=random_lists, length=length,
                                             prep=prep, sort=sort, repetitions=repetitions,
                                             timeout=timeout)
               print('.',end='')
               results.append(dict(
                  sort=sort.__name__,
                  prep=prep.__name__,
                  length=length,
                  time=median_time))
               if median_time > timeout:
                  # don't consider longer lists if it already was too long on this one
                  break
   print()
   print(results)
   pd.DataFrame(results).to_csv("sort_times.csv")

   import seaborn as sns
   import pandas as pd

   sns.set_theme()
   data = pd.read_csv("sort_times.csv")
   plot = sns.relplot(data=data, kind='line', x='length', y='time', style='prep', hue='sort')
   plot.savefig("sort_times.png")
