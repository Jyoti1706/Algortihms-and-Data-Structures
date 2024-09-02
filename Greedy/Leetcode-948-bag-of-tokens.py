class Solution:
    def bagOfTokensScore(self, tokens, power):
        """
        Story:
        1. Sort the Power
        2. ith idx se score += 1, power reduce kar ke, if power >= tokens[i]
        3. jth index se power increase score gawakar, if score >= 1
        4. return max score
        :param tokens:
        :param power:
        :return:
        """
        tokens.sort()
        i = 0
        j = len(tokens)-1
        score = 0
        maxScore = 0
        while i <= j:
            if power >= tokens[i]:
                score += 1
                power -= tokens[i]
                i += 1
                maxScore = max(maxScore, score)
            elif score >= 1:
                power += tokens[j]
                score -= 1
                j -= 1
            else:
                return maxScore
        return maxScore


if __name__ == "__main__":
    obj = Solution()
    tokens = [100, 200]
    power = 150
    print(obj.bagOfTokensScore(tokens,power))
    tokens = [100, 200, 300, 400]
    power = 200
    print(obj.bagOfTokensScore(tokens,power))
    tokens = [100]
    power = 50
    print(obj.bagOfTokensScore(tokens,power))