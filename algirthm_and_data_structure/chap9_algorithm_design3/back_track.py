from typing import List, Union


def backtrack(x: List[Union[float, int]], s: Union[float, int]) -> bool:
    """
    return True if there is an answer ,else return False

    Parameters
    ----------
    x : List[Union[float, int]]
        [description]
    s : Union[float, int]
        [description]

    Returns
    -------
    bool
        [description]
    """    
    n = len(x)
    y = [0]*n

    def bt_subset_sum(level: int) -> bool:
        if level >= n:
            sum = 0
            for i in range(n):
                sum += y[i]*x[i]
            if sum == s:
                print(sum)
                return True
        else:
            y[level] = 0
            if bt_subset_sum(level+1):
                return True
            y[level] = 1
            if bt_subset_sum(level+1):
                return True

            if level == 0:
                print("there is no answer")
                return False
    res=bt_subset_sum(level=0)
    if res:
        print("finished!")
        return True
    else:

        return False

if __name__ == "__main__":
    backtrack([3, 14, 6, 9], 12)
    
    backtrack([3, 14, 6, 9], 2)

