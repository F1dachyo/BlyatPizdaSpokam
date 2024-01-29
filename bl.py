class Enemy_s(pygame.sprite.Sprite):
    image = load_image("enemy/m_type_s.png")
    speed = 1

    def __init__(self, pos2, elem,  *group):
        super().__init__(*group)
        self.image = load_image("enemy/m_type_s.png")
        self.speed = Enemy_s.speed
        self.name = elem
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 1920)
        self.rect.y = random.randint(0, 1080)
        self.string_rendered = font.render(elem, False, (0, 0, 0))
        self.textrect = self.string_rendered.get_rect(center=(self.image.get_rect().center[0], self.image.get_rect().center[1] + 30))
        self.image.blit(self.string_rendered, self.textrect)
        self.distance = ((self.rect.x - pos2[0]) ** 2 + (self.rect.y - pos2[0]) ** 2) ** 0.5

    def update(self, pos2, act_word):
        pos1 = (self.rect.x, self.rect.y)
        if abs(pos1[0] - pos2[0]) > 50 or abs(pos1[1] - pos2[1]) > 50:
            koefx = abs(pos1[0] - pos2[0]) / ((abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])) / 2)
            koefy = abs(pos1[1] - pos2[1]) / ((abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])) / 2)
            if pos1[0] > pos2[0] and pos1[1] > pos2[1]:
                self.rect.x -= self.speed * koefx
                self.rect.y -= self.speed * koefy
            elif pos1[0] > pos2[0] and pos1[1] < pos2[1]:
                self.rect.x -= self.speed * koefx
                self.rect.y += self.speed * koefy
            elif pos1[0] < pos2[0] and pos1[1] > pos2[1]:
                self.rect.x += self.speed * koefx
                self.rect.y -= self.speed * koefy
            else:
                self.rect.x += self.speed * koefx
                self.rect.y += self.speed * koefy
            self.distance = ((self.rect.x - pos2[0]) ** 2 + (self.rect.y - pos2[0]) ** 2) ** 0.5
        if act_word == self.name:
            self.kill()
            change_score(30)
            change_money(15)


class Enemy_m(pygame.sprite.Sprite):
    image = load_image("enemy/m_type_m.png")
    speed = 0.75

    def __init__(self, pos2,  elem,  *group):
        super().__init__(*group)
        self.image = load_image("enemy/m_type_m.png")
        self.speed = Enemy_m.speed
        self.name = elem
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 1920)
        self.rect.y = random.randint(0, 1080)
        self.string_rendered = font.render(elem, False, (0, 0, 0))
        self.textrect = self.string_rendered.get_rect(center=(self.image.get_rect().center[0], self.image.get_rect().center[1] + 30))
        self.image.blit(self.string_rendered, self.textrect)
        self.distance = ((self.rect.x - pos2[0]) ** 2 + (self.rect.y - pos2[0]) ** 2) ** 0.5

    def update(self, pos2, act_word):
        pos1 = (self.rect.x, self.rect.y)
        if abs(pos1[0] - pos2[0]) > 50 or abs(pos1[1] - pos2[1]) > 50:
            koefx = abs(pos1[0] - pos2[0]) / ((abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])) / 2)
            koefy = abs(pos1[1] - pos2[1]) / ((abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])) / 2)
            if pos1[0] > pos2[0] and pos1[1] > pos2[1]:
                self.rect.x -= self.speed * koefx
                self.rect.y -= self.speed * koefy
            elif pos1[0] > pos2[0] and pos1[1] < pos2[1]:
                self.rect.x -= self.speed * koefx
                self.rect.y += self.speed * koefy
            elif pos1[0] < pos2[0] and pos1[1] > pos2[1]:
                self.rect.x += self.speed * koefx
                self.rect.y -= self.speed * koefy
            else:
                self.rect.x += self.speed * koefx
                self.rect.y += self.speed * koefy
            self.distance = ((self.rect.x - pos2[0]) ** 2 + (self.rect.y - pos2[0]) ** 2) ** 0.5
        if act_word == self.name:
            self.kill()
            change_score(60)
            change_money(30)


class Enemy_l(pygame.sprite.Sprite):
    image = load_image("enemy/m_type_l.png")
    speed = 0.5

    def __init__(self, pos2, elem,  *group):
        super().__init__(*group)
        self.image = load_image("enemy/m_type_l.png")
        self.speed = Enemy_l.speed
        self.name = elem
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 1920)
        self.rect.y = random.randint(0, 1080)
        self.string_rendered = font.render(elem, False, (0, 0, 0))
        self.textrect = self.string_rendered.get_rect(center=(self.image.get_rect().center[0], self.image.get_rect().center[1] + 30))
        self.image.blit(self.string_rendered, self.textrect)
        self.distance = ((self.rect.x - pos2[0]) ** 2 + (self.rect.y - pos2[0]) ** 2) ** 0.5

    def update(self, pos2, act_word):
        pos1 = (self.rect.x, self.rect.y)
        if abs(pos1[0] - pos2[0]) > 50 or abs(pos1[1] - pos2[1]) > 50:
            koefx = abs(pos1[0] - pos2[0]) / ((abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])) / 2)
            koefy = abs(pos1[1] - pos2[1]) / ((abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])) / 2)
            if pos1[0] > pos2[0] and pos1[1] > pos2[1]:
                self.rect.x -= self.speed * koefx
                self.rect.y -= self.speed * koefy
            elif pos1[0] > pos2[0] and pos1[1] < pos2[1]:
                self.rect.x -= self.speed * koefx
                self.rect.y += self.speed * koefy
            elif pos1[0] < pos2[0] and pos1[1] > pos2[1]:
                self.rect.x += self.speed * koefx
                self.rect.y -= self.speed * koefy
            else:
                self.rect.x += self.speed * koefx
                self.rect.y += self.speed * koefy
            self.distance = ((self.rect.x - pos2[0]) ** 2 + (self.rect.y - pos2[0]) ** 2) ** 0.5
        if act_word == self.name:
            self.kill()
            change_score(100)
            change_money(50)