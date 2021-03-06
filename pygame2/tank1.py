import pygame
# 石头墙
class Brick(pygame.sprite.Sprite):
 def __init__(self):
  pygame.sprite.Sprite.__init__(self)
  self.brick = pygame.image.load('images/scene/brick.png')
  self.rect = self.brick.get_rect()
  self.being = False

# 钢墙
class Iron(pygame.sprite.Sprite):
 def __init__(self):
  pygame.sprite.Sprite.__init__(self)
  self.iron = pygame.image.load('images/scene/iron.png')
  self.rect = self.iron.get_rect()
  self.being = False

# 冰
class Ice(pygame.sprite.Sprite):
 def __init__(self):
  pygame.sprite.Sprite.__init__(self)
  self.ice = pygame.image.load('images/scene/ice.png')
  self.rect = self.ice.get_rect()
  self.being = False

# 河流
class River(pygame.sprite.Sprite):
 def __init__(self, kind=None):
  pygame.sprite.Sprite.__init__(self)
  if kind is None:
   self.kind = random.randint(0, 1)
  self.rivers = ['images/scene/river1.png', 'images/scene/river2.png']
  self.river = pygame.image.load(self.rivers[self.kind])
  self.rect = self.river.get_rect()
  self.being = False

# 树
class Tree(pygame.sprite.Sprite):
 def __init__(self):
  pygame.sprite.Sprite.__init__(self)
  self.tree = pygame.image.load('images/scene/tree.png')
  self.rect = self.tree.get_rect()
  self.being = False

# 地图
class Map():
 def __init__(self, stage):
  self.brickGroup = pygame.sprite.Group()
  self.ironGroup  = pygame.sprite.Group()
  self.iceGroup = pygame.sprite.Group()
  self.riverGroup = pygame.sprite.Group()
  self.treeGroup = pygame.sprite.Group()
  if stage == 1:
   self.stage1()
  elif stage == 2:
   self.stage2()
 # 关卡一
 def stage1(self):
  for x in [2, 3, 6, 7, 18, 19, 22, 23]:
   for y in [2, 3, 4, 5, 6, 7, 8, 9, 10, 17, 18, 19, 20, 21, 22, 23]:
    self.brick = Brick()
    self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24
    self.brick.being = True
    self.brickGroup.add(self.brick)
  for x in [10, 11, 14, 15]:
   for y in [2, 3, 4, 5, 6, 7, 8, 11, 12, 15, 16, 17, 18, 19, 20]:
    self.brick = Brick()
    self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24
    self.brick.being = True
    self.brickGroup.add(self.brick)
  for x in [4, 5, 6, 7, 18, 19, 20, 21]:
   for y in [13, 14]:
    self.brick = Brick()
    self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24
    self.brick.being = True
    self.brickGroup.add(self.brick)
  for x in [12, 13]:
   for y in [16, 17]:
    self.brick = Brick()
    self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24
    self.brick.being = True
    self.brickGroup.add(self.brick)
  for x, y in [(11, 23), (12, 23), (13, 23), (14, 23), (11, 24), (14, 24), (11, 25), (14, 25)]:
   self.brick = Brick()
   self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24
   self.brick.being = True
   self.brickGroup.add(self.brick)
  for x, y in [(0, 14), (1, 14), (12, 6), (13, 6), (12, 7), (13, 7), (24, 14), (25, 14)]:
   self.iron = Iron()
   self.iron.rect.left, self.iron.rect.top = 3 + x * 24, 3 + y * 24
   self.iron.being = True
   self.ironGroup.add(self.iron)
 # 关卡二
 def stage2(self):
  for x in [2, 3, 6, 7, 18, 19, 22, 23]:
   for y in [2, 3, 4, 5, 6, 7, 8, 9, 10, 17, 18, 19, 20, 21, 22, 23]:
    self.brick = Brick()
    self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24
    self.brick.being = True
    self.brickGroup.add(self.brick)
  for x in [10, 11, 14, 15]:
   for y in [2, 3, 4, 5, 6, 7, 8, 11, 12, 15, 16, 17, 18, 19, 20]:
    self.brick = Brick()
    self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24
    self.brick.being = True
    self.brickGroup.add(self.brick)
  for x in [4, 5, 6, 7, 18, 19, 20, 21]:
   for y in [13, 14]:
    self.brick = Brick()
    self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24
    self.brick.being = True
    self.brickGroup.add(self.brick)
  for x in [12, 13]:
   for y in [16, 17]:
    self.brick = Brick()
    self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24
    self.brick.being = True
    self.brickGroup.add(self.brick)
  for x, y in [(11, 23), (12, 23), (13, 23), (14, 23), (11, 24), (14, 24), (11, 25), (14, 25)]:
   self.brick = Brick()
   self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24
   self.brick.being = True
   self.brickGroup.add(self.brick)
  for x, y in [(0, 14), (1, 14), (12, 6), (13, 6), (12, 7), (13, 7), (24, 14), (25, 14)]:
   self.iron = Iron()
   self.iron.rect.left, self.iron.rect.top = 3 + x * 24, 3 + y * 24
   self.iron.being = True
   self.ironGroup.add(self.iron)
 def protect_home(self):
  for x, y in [(11, 23), (12, 23), (13, 23), (14, 23), (11, 24), (14, 24), (11, 25), (14, 25)]:
   self.iron = Iron()
   self.iron.rect.left, self.iron.rect.top = 3 + x * 24, 3 + y * 24
   self.iron.being = True
   self.ironGroup.add(self.iron)
class Home(pygame.sprite.Sprite):
 def __init__(self):
  pygame.sprite.Sprite.__init__(self)
  self.homes = ['images/home/home1.png', 'images/home/home2.png', 'images/home/home_destroyed.png']
  self.home = pygame.image.load(self.homes[0])
  self.rect = self.home.get_rect()
  self.rect.left, self.rect.top = (3 + 12 * 24, 3 + 24 * 24)
  self.alive = True
 # 大本营置为摧毁状态
 def set_dead(self):
  self.home = pygame.image.load(self.homes[-1])
  self.alive = False
# 食物类
class Food(pygame.sprite.Sprite):
 def __init__(self):
  pygame.sprite.Sprite.__init__(self)
  # 消灭当前所有敌人
  self.food_boom = 'images/food/food_boom.png'
  # 当前所有敌人静止一段时间
  self.food_clock = 'images/food/food_clock.png'
  # 使得坦克子弹可碎钢板
  self.food_gun = 'images/food/food_gun.png'
  # 使得大本营的墙变为钢板
  self.food_iron = 'images/food/food_gun.png'
  # 坦克获得一段时间的保护罩
  self.food_protect = 'images/food/food_protect.png'
  # 坦克升级
  self.food_star = 'images/food/food_star.png'
  # 坦克生命 + 1
  self.food_tank = 'images/food/food_tank.png'
  # 所有食物
  self.foods = [self.food_boom, self.food_clock, self.food_gun, self.food_iron, self.food_protect, self.food_star, self.food_tank]
  self.kind = None
  self.food = None
  self.rect = None
  # 是否存在
  self.being = False
  # 存在时间
  self.time = 1000
 # 生成食物
 def generate(self):
  self.kind = random.randint(0, 6)
  self.food = pygame.image.load(self.foods[self.kind]).convert_alpha()
  self.rect = self.food.get_rect()
  self.rect.left, self.rect.top = random.randint(100, 500), random.randint(100, 500)
  self.being = True
# 我方坦克类
class myTank(pygame.sprite.Sprite):
 def __init__(self, player):
  pygame.sprite.Sprite.__init__(self)
  # 玩家编号(1/2)
  self.player = player
  # 不同玩家用不同的坦克(不同等级对应不同的图)
  if player == 1:
   self.tanks = ['images/myTank/tank_T1_0.png', 'images/myTank/tank_T1_1.png', 'images/myTank/tank_T1_2.png']
  elif player == 2:
   self.tanks = ['images/myTank/tank_T2_0.png', 'images/myTank/tank_T2_1.png', 'images/myTank/tank_T2_2.png']
  else:
   raise ValueError('myTank class -> player value error.')
  # 坦克等级(初始0)
  self.level = 0
  # 载入(两个tank是为了轮子特效)
  self.tank = pygame.image.load(self.tanks[self.level]).convert_alpha()
  self.tank_0 = self.tank.subsurface((0, 0), (48, 48))
  self.tank_1 = self.tank.subsurface((48, 0), (48, 48))
  self.rect = self.tank_0.get_rect()
  # 保护罩
  self.protected_mask = pygame.image.load('images/others/protect.png').convert_alpha()
  self.protected_mask1 = self.protected_mask.subsurface((0, 0), (48, 48))
  self.protected_mask2 = self.protected_mask.subsurface((48, 0), (48, 48))
  # 坦克方向
  self.direction_x, self.direction_y = 0, -1
  # 不同玩家的出生位置不同
  if player == 1:
   self.rect.left, self.rect.top = 3 + 24 * 8, 3 + 24 * 24
  elif player == 2:
   self.rect.left, self.rect.top = 3 + 24 * 16, 3 + 24 * 24
  else:
   raise ValueError('myTank class -> player value error.')
  # 坦克速度
  self.speed = 3
  # 是否存活
  self.being = True
  # 有几条命
  self.life = 3
  # 是否处于保护状态
  self.protected = False
  # 子弹
  self.bullet = Bullet()
 # 射击
 def shoot(self):
  self.bullet.being = True
  self.bullet.turn(self.direction_x, self.direction_y)
  if self.direction_x == 0 and self.direction_y == -1:
   self.bullet.rect.left = self.rect.left + 20
   self.bullet.rect.bottom = self.rect.top - 1
  elif self.direction_x == 0 and self.direction_y == 1:
   self.bullet.rect.left = self.rect.left + 20
   self.bullet.rect.top = self.rect.bottom + 1
  elif self.direction_x == -1 and self.direction_y == 0:
   self.bullet.rect.right = self.rect.left - 1
   self.bullet.rect.top = self.rect.top + 20
  elif self.direction_x == 1 and self.direction_y == 0:
   self.bullet.rect.left = self.rect.right + 1
   self.bullet.rect.top = self.rect.top + 20
  else:
   raise ValueError('myTank class -> direction value error.')
  if self.level == 0:
   self.bullet.speed = 8
   self.bullet.stronger = False
  elif self.level == 1:
   self.bullet.speed = 12
   self.bullet.stronger = False
  elif self.level == 2:
   self.bullet.speed = 12
   self.bullet.stronger = True
  elif self.level == 3:
   self.bullet.speed = 16
   self.bullet.stronger = True
  else:
   raise ValueError('myTank class -> level value error.')
 # 等级提升
 def up_level(self):
  if self.level < 3:
   self.level += 1
  try:
   self.tank = pygame.image.load(self.tanks[self.level]).convert_alpha()
  except:
   self.tank = pygame.image.load(self.tanks[-1]).convert_alpha()
 # 等级降低
 def down_level(self):
  if self.level > 0:
   self.level -= 1
  self.tank = pygame.image.load(self.tanks[self.level]).convert_alpha()
 # 向上
 def move_up(self, tankGroup, brickGroup, ironGroup, myhome):
  self.direction_x, self.direction_y = 0, -1
  # 先移动后判断
  self.rect = self.rect.move(self.speed*self.direction_x, self.speed*self.direction_y)
  self.tank_0 = self.tank.subsurface((0, 0), (48, 48))
  self.tank_1 = self.tank.subsurface((48, 0), (48, 48))
  # 是否可以移动
  is_move = True
  # 地图顶端
  if self.rect.top < 3:
   self.rect = self.rect.move(self.speed*-self.direction_x, self.speed*-self.direction_y)
   is_move = False
  # 撞石头/钢墙
  if pygame.sprite.spritecollide(self, brickGroup, False, None) or \
   pygame.sprite.spritecollide(self, ironGroup, False, None):
   self.rect = self.rect.move(self.speed*-self.direction_x, self.speed*-self.direction_y)
   is_move = False
  # 撞其他坦克
  if pygame.sprite.spritecollide(self, tankGroup, False, None):
   self.rect = self.rect.move(self.speed*-self.direction_x, self.speed*-self.direction_y)
   is_move = False
  # 大本营
  if pygame.sprite.collide_rect(self, myhome):
   self.rect = self.rect.move(self.speed*-self.direction_x, self.speed*-self.direction_y)
   is_move = False
  return is_move
 # 向下
 def move_down(self, tankGroup, brickGroup, ironGroup, myhome):
  self.direction_x, self.direction_y = 0, 1
  # 先移动后判断
  self.rect = self.rect.move(self.speed*self.direction_x, self.speed*self.direction_y)
  self.tank_0 = self.tank.subsurface((0, 48), (48, 48))
  self.tank_1 = self.tank.subsurface((48, 48), (48, 48))
  # 是否可以移动
  is_move = True
  # 地图底端
  if self.rect.bottom > 630 - 3:
   self.rect = self.rect.move(self.speed*-self.direction_x, self.speed*-self.direction_y)
   is_move = False
  # 撞石头/钢墙
  if pygame.sprite.spritecollide(self, brickGroup, False, None) or \
   pygame.sprite.spritecollide(self, ironGroup, False, None):
   self.rect = self.rect.move(self.speed*-self.direction_x, self.speed*-self.direction_y)
   is_move = False
  # 撞其他坦克
  if pygame.sprite.spritecollide(self, tankGroup, False, None):
   self.rect = self.rect.move(self.speed*-self.direction_x, self.speed*-self.direction_y)
   is_move = False
  # 大本营
  if pygame.sprite.collide_rect(self, myhome):
   self.rect = self.rect.move(self.speed*-self.direction_x, self.speed*-self.direction_y)
   is_move = False
  return is_move
 # 向左
 def move_left(self, tankGroup, brickGroup, ironGroup, myhome):
  self.direction_x, self.direction_y = -1, 0
  # 先移动后判断
  self.rect = self.rect.move(self.speed*self.direction_x, self.speed*self.direction_y)
  self.tank_0 = self.tank.subsurface((0, 96), (48, 48))
  self.tank_1 = self.tank.subsurface((48, 96), (48, 48))
  # 是否可以移动
  is_move = True
  # 地图左端
  if self.rect.left < 3:
   self.rect = self.rect.move(self.speed*-self.direction_x, self.speed*-self.direction_y)
   is_move = False
  # 撞石头/钢墙
  if pygame.sprite.spritecollide(self, brickGroup, False, None) or \
   pygame.sprite.spritecollide(self, ironGroup, False, None):
   self.rect = self.rect.move(self.speed*-self.direction_x, self.speed*-self.direction_y)
   is_move = False
  # 撞其他坦克
  if pygame.sprite.spritecollide(self, tankGroup, False, None):
   self.rect = self.rect.move(self.speed*-self.direction_x, self.speed*-self.direction_y)
   is_move = False  
  # 大本营
  if pygame.sprite.collide_rect(self, myhome):
   self.rect = self.rect.move(self.speed*-self.direction_x, self.speed*-self.direction_y)
   is_move = False
  return is_move
 # 向右
 def move_right(self, tankGroup, brickGroup, ironGroup, myhome):
  self.direction_x, self.direction_y = 1, 0
  # 先移动后判断
  self.rect = self.rect.move(self.speed*self.direction_x, self.speed*self.direction_y)
  self.tank_0 = self.tank.subsurface((0, 144), (48, 48))
  self.tank_1 = self.tank.subsurface((48, 144), (48, 48))
  # 是否可以移动
  is_move = True
  # 地图右端
  if self.rect.right > 630 - 3:
   self.rect = self.rect.move(self.speed*-self.direction_x, self.speed*-self.direction_y)
   is_move = False
  # 撞石头/钢墙
  if pygame.sprite.spritecollide(self, brickGroup, False, None) or \
   pygame.sprite.spritecollide(self, ironGroup, False, None):
   self.rect = self.rect.move(self.speed*-self.direction_x, self.speed*-self.direction_y)
   is_move = False
  # 撞其他坦克
  if pygame.sprite.spritecollide(self, tankGroup, False, None):
   self.rect = self.rect.move(self.speed*-self.direction_x, self.speed*-self.direction_y)
   is_move = False
  # 大本营
  if pygame.sprite.collide_rect(self, myhome):
   self.rect = self.rect.move(self.speed*-self.direction_x, self.speed*-self.direction_y)
   is_move = False
  return is_move
 # 死后重置
 def reset(self):
  self.level = 0
  self.protected = False
  self.tank = pygame.image.load(self.tanks[self.level]).convert_alpha()
  self.tank_0 = self.tank.subsurface((0, 0), (48, 48))
  self.tank_1 = self.tank.subsurface((48, 0), (48, 48))
  self.rect = self.tank_0.get_rect()
  self.direction_x, self.direction_y = 0, -1
  if self.player == 1:
   self.rect.left, self.rect.top = 3 + 24 * 8, 3 + 24 * 24
  elif self.player == 2:
   self.rect.left, self.rect.top = 3 + 24 * 16, 3 + 24 * 24
  else:
   raise ValueError('myTank class -> player value error.')
  self.speed = 3

# 敌方坦克类
class enemyTank(pygame.sprite.Sprite):
 def __init__(self, x=None, kind=None, is_red=None):
  pygame.sprite.Sprite.__init__(self)
  # 用于给刚生成的坦克播放出生特效
  self.born = True
  self.times = 90
  # 坦克的种类编号
  if kind is None:
   self.kind = random.randint(0, 3)
  else:
   self.kind = kind
  # 所有坦克
  self.tanks1 = ['images/enemyTank/enemy_1_0.png', 'images/enemyTank/enemy_1_1.png', 'images/enemyTank/enemy_1_2.png', 'images/enemyTank/enemy_1_3.png']
  self.tanks2 = ['images/enemyTank/enemy_2_0.png', 'images/enemyTank/enemy_2_1.png', 'images/enemyTank/enemy_2_2.png', 'images/enemyTank/enemy_2_3.png']
  self.tanks3 = ['images/enemyTank/enemy_3_0.png', 'images/enemyTank/enemy_3_1.png', 'images/enemyTank/enemy_3_2.png', 'images/enemyTank/enemy_3_3.png']
  self.tanks4 = ['images/enemyTank/enemy_4_0.png', 'images/enemyTank/enemy_4_1.png', 'images/enemyTank/enemy_4_2.png', 'images/enemyTank/enemy_4_3.png']
  self.tanks = [self.tanks1, self.tanks2, self.tanks3, self.tanks4]
  # 是否携带食物(红色的坦克携带食物)
  if is_red is None:
   self.is_red = random.choice((True, False, False, False, False))
  else:
   self.is_red = is_red
  # 同一种类的坦克具有不同的颜色, 红色的坦克比同类坦克多一点血量
  if self.is_red:
   self.color = 3
  else:
   self.color = random.randint(0, 2)
  # 血量
  self.blood = self.color
  # 载入(两个tank是为了轮子特效)
  self.tank = pygame.image.load(self.tanks[self.kind][self.color]).convert_alpha()
  self.tank_0 = self.tank.subsurface((0, 48), (48, 48))
  self.tank_1 = self.tank.subsurface((48, 48), (48, 48))
  self.rect = self.tank_0.get_rect()
  # 坦克位置
  if x is None:
   self.x = random.randint(0, 2)
  else:
   self.x = x
  self.rect.left, self.rect.top = 3 + self.x * 12 * 24, 3
  # 坦克是否可以行动
  self.can_move = True
  # 坦克速度
  self.speed = max(3 - self.kind, 1)
  # 方向
  self.direction_x, self.direction_y = 0, 1
  # 是否存活
  self.being = True
  # 子弹
  self.bullet = Bullet()
 # 射击
 def shoot(self):
  self.bullet.being = True
  self.bullet.turn(self.direction_x, self.direction_y)
  if self.direction_x == 0 and self.direction_y == -1:
   self.bullet.rect.left = self.rect.left + 20
   self.bullet.rect.bottom = self.rect.top - 1
  elif self.direction_x == 0 and self.direction_y == 1:
   self.bullet.rect.left = self.rect.left + 20
   self.bullet.rect.top = self.rect.bottom + 1
  elif self.direction_x == -1 and self.direction_y == 0:
   self.bullet.rect.right = self.rect.left - 1
   self.bullet.rect.top = self.rect.top + 20
  elif self.direction_x == 1 and self.direction_y == 0:
   self.bullet.rect.left = self.rect.right + 1
   self.bullet.rect.top = self.rect.top + 20
  else:
   raise ValueError('enemyTank class -> direction value error.')
 # 随机移动
 def move(self, tankGroup, brickGroup, ironGroup, myhome):
  self.rect = self.rect.move(self.speed*self.direction_x, self.speed*self.direction_y)
  is_move = True
  if self.direction_x == 0 and self.direction_y == -1:
   self.tank_0 = self.tank.subsurface((0, 0), (48, 48))
   self.tank_1 = self.tank.subsurface((48, 0), (48, 48))
   if self.rect.top < 3:
    self.rect = self.rect.move(self.speed*-self.direction_x, self.speed*-self.direction_y)
    self.direction_x, self.direction_y = random.choice(([0, 1], [0, -1], [1, 0], [-1, 0]))
    is_move = False
  elif self.direction_x == 0 and self.direction_y == 1:
   self.tank_0 = self.tank.subsurface((0, 48), (48, 48))
   self.tank_1 = self.tank.subsurface((48, 48), (48, 48))
   if self.rect.bottom > 630 - 3:
    self.rect = self.rect.move(self.speed*-self.direction_x, self.speed*-self.direction_y)
    self.direction_x, self.direction_y = random.choice(([0, 1], [0, -1], [1, 0], [-1, 0]))
    is_move = False
  elif self.direction_x == -1 and self.direction_y == 0:
   self.tank_0 = self.tank.subsurface((0, 96), (48, 48))
   self.tank_1 = self.tank.subsurface((48, 96), (48, 48))
   if self.rect.left < 3:
    self.rect = self.rect.move(self.speed*-self.direction_x, self.speed*-self.direction_y)
    self.direction_x, self.direction_y = random.choice(([0, 1], [0, -1], [1, 0], [-1, 0]))
    is_move = False
  elif self.direction_x == 1 and self.direction_y == 0:
   self.tank_0 = self.tank.subsurface((0, 144), (48, 48))
   self.tank_1 = self.tank.subsurface((48, 144), (48, 48))
   if self.rect.right > 630 - 3:
    self.rect = self.rect.move(self.speed*-self.direction_x, self.speed*-self.direction_y)
    self.direction_x, self.direction_y = random.choice(([0, 1], [0, -1], [1, 0], [-1, 0]))
    is_move = False
  else:
   raise ValueError('enemyTank class -> direction value error.')
  if pygame.sprite.spritecollide(self, brickGroup, False, None) \
   or pygame.sprite.spritecollide(self, ironGroup, False, None) \
   or pygame.sprite.spritecollide(self, tankGroup, False, None):
   self.rect = self.rect.move(self.speed*-self.direction_x, self.speed*-self.direction_y)
   self.direction_x, self.direction_y = random.choice(([0, 1], [0, -1], [1, 0], [-1, 0]))
   is_move = False
  if pygame.sprite.collide_rect(self, myhome):
   self.rect = self.rect.move(self.speed*-self.direction_x, self.speed*-self.direction_y)
   self.direction_x, self.direction_y = random.choice(([0, 1], [0, -1], [1, 0], [-1, 0]))
   is_move = False
  return is_move
 # 重新载入坦克
 def reload(self):
  self.tank = pygame.image.load(self.tanks[self.kind][self.color]).convert_alpha()
  self.tank_0 = self.tank.subsurface((0, 48), (48, 48))
  self.tank_1 = self.tank.subsurface((48, 48), (48, 48))
# 子弹类
class Bullet(pygame.sprite.Sprite):
 def __init__(self):
  pygame.sprite.Sprite.__init__(self)
  # 子弹四个方向(上下左右)
  self.bullets = ['images/bullet/bullet_up.png', 'images/bullet/bullet_down.png', 'images/bullet/bullet_left.png', 'images/bullet/bullet_right.png']
  # 子弹方向(默认向上)
  self.direction_x, self.direction_y = 0, -1
  self.bullet = pygame.image.load(self.bullets[0])
  self.rect = self.bullet.get_rect()
  # 在坦克类中再赋实际值
  self.rect.left, self.rect.right = 0, 0
  # 速度
  self.speed = 6
  # 是否存活
  self.being = False
  # 是否为加强版子弹(可碎钢板)
  self.stronger = False
 # 改变子弹方向
 def turn(self, direction_x, direction_y):
  self.direction_x, self.direction_y = direction_x, direction_y
  if self.direction_x == 0 and self.direction_y == -1:
   self.bullet = pygame.image.load(self.bullets[0])
  elif self.direction_x == 0 and self.direction_y == 1:
   self.bullet = pygame.image.load(self.bullets[1])
  elif self.direction_x == -1 and self.direction_y == 0:
   self.bullet = pygame.image.load(self.bullets[2])
  elif self.direction_x == 1 and self.direction_y == 0:
   self.bullet = pygame.image.load(self.bullets[3])
  else:
   raise ValueError('Bullet class -> direction value error.')
 # 移动
 def move(self):
  self.rect = self.rect.move(self.speed*self.direction_x, self.speed*self.direction_y)
  # 到地图边缘后消失
  if (self.rect.top < 3) or (self.rect.bottom > 630 - 3) or (self.rect.left < 3) or (self.rect.right > 630 - 3):
   self.being = False
# 初始化
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((630, 630))
pygame.display.set_caption("TANK")
# 加载图片
bg_img = pygame.image.load("images/others/background.png")
# 加载音效
add_sound = pygame.mixer.Sound("audios/add.wav")
add_sound.set_volume(1)
bang_sound = pygame.mixer.Sound("audios/bang.wav")
bang_sound.set_volume(1)
blast_sound = pygame.mixer.Sound("audios/blast.wav")
blast_sound.set_volume(1)
fire_sound = pygame.mixer.Sound("audios/fire.wav")
fire_sound.set_volume(1)
Gunfire_sound = pygame.mixer.Sound("audios/Gunfire.wav")
Gunfire_sound.set_volume(1)
hit_sound = pygame.mixer.Sound("audios/hit.wav")
hit_sound.set_volume(1)
start_sound = pygame.mixer.Sound("audios/start.wav")
start_sound.set_volume(1)
# 开始界面
num_player = show_start_interface(screen, 630, 630)
# 播放游戏开始的音乐
start_sound.play()
# 关卡
stage = 0
num_stage = 2
# 游戏是否结束
is_gameover = False
# 时钟
clock = pygame.time.Clock()