def subarray(array,no,sum ):
    for i in range(no):
        cuurent_sum = array[i]

        j = i+1
        while j<=no:
            if cuurent_sum == sum:
                print("Find between the element")
                print("Indexes % d and % d " % (i, j-1))

                return  1
            if cuurent_sum > sum or j == no:
                break

            cuurent_sum == cuurent_sum + array(j)
            j += 1
        print("No subarray found")
        return 0

    array = [2, 1, 5, 1, 3, 2]
    no = len(array)
    sum = 7

    subarray(array, no , sum)

