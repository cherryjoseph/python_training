#leetcode 1523
def count_odds (low: int ,high: int) -> int:
    cnt=0
    #odd_arr = list(filter( lambda x:True if x>0 else False , list(map(lambda x:x if x%2>0 else 0,range(low,high+1) ) ) ) )
    return len(list(filter( lambda x:True if x%2>0 else False   , range(low, high+1) )) )
    



print(count_odds(10,11))