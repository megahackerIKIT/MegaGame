#Спасибо за скачивание
#Связаться со мной megahackerIKIT@mailforspam.com

import random


def get_number_with_protection_from_Lev_Pavlovich():
	while 1:
		x = input()
		if(x.isdigit() and int(x) != 0):
			x = int(x)
			break
		else:
			print("Некоректный ввод")
	return x


class Game():
	def __init__(self, n, m):
		self.mx = n
		self.my = m
		self.dx = [-1, 0, 1, 1, 1, 0, -1, -1]
		self.dy = [1, 1, 1, 0, -1, -1, -1, 0, 1]
		self.map = []
		for i in range(n + 2):
			self.map.append([])
			for j in range(m + 2):
				self.map[i].append(' ')
		self.visible = []
		for i in range(n):
			self.visible.append([])
			for j in range(m):
				self.visible[i].append('#')

	def spawn_mines(self, count_mines):
		while(1):
			rand_x = random.randint(1, self.mx)
			rand_y = random.randint(1, self.my)
			if(self.map[rand_x][rand_y] == ' '):
				self.map[rand_x][rand_y] = '*'
				count_mines -= 1
				if(not count_mines):
					return 0

	def check_neighbour(self, now_x, now_y):
		ans = 0
		for i in range(8):
			if(self.map[now_x + self.dx[i]][now_y + self.dy[i]] == '*'):
				ans += 1
		return ans;

	def fill_num(self):
		for i in range(1, len(self.map) - 1):
			for j in range(1, len(self.map[i]) - 1):
				if self.map[i][j] == ' ':
					self.map[i][j] = self.check_neighbour(i, j)

	def draw_visible(self):
		for i in self.visible:
			for j in i:
				print(j, end = ' ')
			print()

	def you_lose(self):
		print("Прости, ты проиграл")
		for i in range(1, len(self.map) - 1):
			for j in range(1, len(self.map[i]) - 1):
				print(self.map[i][j], end = ' ')
			print()
		return 1

	def win_check(self, mines):
		reshotki = 0
		for i in self.visible:
			for j in i:
				if(j == '#'):
					reshotki += 1
		if(reshotki == mines):
			print("Ты победил!!!")
			for i in range(1, len(self.map) - 1):
				for j in range(1, len(self.map[i]) - 1):
					print(self.map[i][j], end=' ')
				print()
			return 1
		return 0

	def open_zero(self, x, y):
		self.visible[x - 1][y - 1] = 0
		for i in range(8):
			if self.map[x + self.dx[i]][y + self.dy[i]] == ' ':
				continue
			elif self.map[x + self.dx[i]][y + self.dy[i]] == 0 and self.visible[x + self.dx[i] - 1][y + self.dy[i] - 1] == '#':
				self.open_zero(x + self.dx[i], y + self.dy[i])
			else:
				self.visible[x + self.dx[i] - 1][y + self.dy[i] - 1] = self.map[x + self.dx[i]][y + self.dy[i]]

	def open_cell(self, x, y):
		#while 1:
			#if(self.visible[x][y] == "#"):

			#else:
				#print("Эта клетка уже открыта")
		if(self.map[x][y] == 0):
			self.open_zero(x, y)
		elif(str(self.map[x][y]).isdigit()):
			self.visible[x - 1][y - 1] = self.map[x][y]
		else:
			self.you_lose()
			return 1

	def run(self):
		while 1:
			print('Введите количество мин:')
			cm = get_number_with_protection_from_Lev_Pavlovich()
			if cm < m_x * m_y:
				break
			else:
				print("Слишком большое число, попробуй меньше")
		self.spawn_mines(cm)
		self.fill_num()
		print('Левая верхняя клетка имеет координаты 1 1')
		print('→ X')
		print('↓ Y')
		while 1:
		#	for i in range(1, len(self.map) - 1):
		#		for j in range(1, len(self.map[i]) - 1):
		#			print(self.map[i][j], end = ' ')
		#		print()
			print()
			self.draw_visible()
			print("Введите координату по X:")
			inp_y = get_number_with_protection_from_Lev_Pavlovich()
			while 1:
				if inp_y <= m_x:
					break
				else:
					print("Введи координату поменьше")
					inp_y = get_number_with_protection_from_Lev_Pavlovich()
			print("Введите координату по Y")
			inp_x = get_number_with_protection_from_Lev_Pavlovich()
			while 1:
				if inp_x <= m_y:
					break
				else:
					print("Введи координату поменьше")
					inp_x = get_number_with_protection_from_Lev_Pavlovich()
			if(self.open_cell(inp_x, inp_y)):
				break
			if(self.win_check(cm)):
				break
		print()
choice = 1
print("Добро пожаловать в игру сапер")
print()
while 1:
	print("1-играть в сапера")
	print("2-выйти из игры")
	choice = get_number_with_protection_from_Lev_Pavlovich()
	if choice != 1 and choice != 2:
		print("Некоректный ввод")
	if choice == 2:
		break
	if choice == 1:
		print("Введите высоту поля не более 30 клеток:")
		m_x = get_number_with_protection_from_Lev_Pavlovich()
		while 1:
			if (m_x <= 30):
				break
			else:
				print("Введите количество клеток не более 30")
				m_x = get_number_with_protection_from_Lev_Pavlovich()
		print("Введите ширину поля не более 30 клеток:")
		m_y = get_number_with_protection_from_Lev_Pavlovich()
		while 1:
			if (m_y <= 30):
				break
			else:
				print("Введите количество клеток не более 30")
				m_y = get_number_with_protection_from_Lev_Pavlovich()
		Game(m_x, m_y).run()
