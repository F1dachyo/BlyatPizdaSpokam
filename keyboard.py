from pynput.keyboard import Listener


def str_key(key):
    return str(key)[1]


class Keyboard:
    current_word = ()
    completed_length = 0
    active_words = []

    def __init__(self):
        self.reset_word()
        self.start_listener()

    def start_listener(self):
        listener = Listener(on_press=self.on_press)
        listener.start()

    def choose_active_word(self, key):
        for pair in self.active_words:
            word = pair[0]
            if word[0] == str_key(key):
                self.current_word = pair
                self.completed_length = 0
                print(f'{word} was chosen')
                return word

    def on_press(self, key):
        word = self.current_word[0]
        if not word:
            word = self.choose_active_word(key)
            if not word:
                return

        if str_key(key) == word[self.completed_length]:
            self.completed_length += 1
            print(f"{word[:self.completed_length]}")
            if self.completed_length == len(word):
                print("complete")
                self.current_word[-1](word)
                self.reset_word()

    def reset_word(self):
        if self.current_word:
            self.active_words.remove(self.current_word)
        self.current_word = ('', 0, None)
        self.completed_length = 0

    def set_active_words(self, words_and_distance):
        # (word, distance_from_player_to_enemy, event)
        self.active_words = sorted(words_and_distance, key=lambda a: a[1])


def x(q):
    print(q)


keyboard = Keyboard()
data = [("дом", 1, x), ("самосвал", 2, x)]
keyboard.set_active_words(data)
while True:
    pass
