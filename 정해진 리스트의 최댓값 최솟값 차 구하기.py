def gap_score(score_list):

    def max(score_list):

        maxvalue = score_list[0]

        for i in range(1, len(score_list)):

            if maxvalue < score_list[i]:
                maxvalue = score_list[i]

        return maxvalue

    def min(score_list):

        minvalue = score_list[0]

        for i in range(1, len(score_list)):

            if minvalue > score_list[i]:
                minvalue = score_list[i]
        return minvalue

    return max(score_list) - min(score_list)

math_list = [30, 25, 60, 40, 80, 90, 10, 20, 73]

print(gap_score(math_list))
