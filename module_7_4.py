team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = score_1 + score_2
time_avg = 45.2
challenge_result = 'Победа команды Волшебники'

print('В команде Мастера кода участников: %(team1_num)s !' %
      {'team1_num': team1_num})
print('Итого сегодня в командах участников %(team1_num)s и %(team2_num)s !' %
      {'team1_num': team1_num, 'team2_num': team2_num})
print('Команда Волшебники данных решила задач: {score_2} !'.format(
    score_2=score_2))
print('Волшебники данных решили задачи за {team1_time} c !'.format(
    team1_time=team1_time))
print(f'Команды решили {score_1} и {score_2} задач.')
print(f'Результат битвы: {challenge_result}')
print(f'Сегодня было решено {tasks_total}  и среднее время {
      time_avg} секунд на задачу !')
