def get_test_scores():
    #  Empty dictionary
    scores_dict = dict()
    #  Empty list
    num_scores = []
    #  User input for number of each test scores
    num_of_scores = int(input('Please input the number of each test scores, enter 999 if no more test scores: '))
    while num_of_scores == 999:
        print('Good bye!')
        #  User input for all the scores
        test_scores = int(input('Please input test scores: '))
        scores_dict[num_of_scores] = test_scores
        print(scores_dict)

if __name__ == '__main__':
    get_test_scores()

