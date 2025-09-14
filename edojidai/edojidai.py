import pygame
import sys

# Инициализация Pygame
pygame.init()

# Размеры окна
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("edojidai- Главное Меню")

# Цвета
BACKGROUND_COLOR = (30, 30, 50)
BUTTON_COLOR = (70, 130, 180)
BUTTON_HOVER_COLOR = (100, 160, 210)
TEXT_COLOR = (255, 255, 255)
TITLE_COLOR = (255, 215, 0)

# Шрифты
title_font = pygame.font.SysFont("Arial", 64, bold=True)
button_font = pygame.font.SysFont("Arial", 32)
copyright_font = pygame.font.SysFont("Arial", 16)

# Загрузка фонового изображения (если есть)
try:
    background_image = pygame.image.load("menu.jpg")
    background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
    has_background = True
except:
    has_background = False

# Музыка и звуки
try:
    pygame.mixer.music.load("menu_music.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)  # -1 означает повторение
except:
    print("Файл музыки не найден")

# Класс для кнопок
class Button:
    def __init__(self, x, y, width, height, text, action=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.action = action
        self.is_hovered = False
        
    def draw(self, surface):
        color = BUTTON_HOVER_COLOR if self.is_hovered else BUTTON_COLOR
        pygame.draw.rect(surface, color, self.rect, border_radius=10)
        pygame.draw.rect(surface, (255, 255, 255), self.rect, 2, border_radius=10)
        
        text_surface = button_font.render(self.text, True, TEXT_COLOR)
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)
        
    def check_hover(self, pos):
        self.is_hovered = self.rect.collidepoint(pos)
        return self.is_hovered
        
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.is_hovered and self.action:
                return self.action()
        return False
    
# Отрисовка кнопок
button_width, button_height = 250, 60
button_x = WIDTH // 2 - button_width // 2

# Функции действий для кнопок
def start_game():
    print("Запуск игры!")
    # Здесь будет переход к игровому экрану
    return True

def open_settings():
    print("Открытие настроек")
    # Здесь будет переход к экрану настроек
    return True

def exit_game():
    pygame.quit()
    sys.exit()

# Создание кнопок
button_width, button_height = 250, 60
button_x = WIDTH // 2 - button_width // 2

buttons = [
    Button(button_x, 250, button_width, button_height, "Начать игру", start_game),
    Button(button_x, 330, button_width, button_height, "Настройки", open_settings),
    Button(button_x, 410, button_width, button_height, "Выход", exit_game)
]

# Главный цикл меню
def main_menu():
    clock = pygame.time.Clock()
    running = True
    
    while running:
        mouse_pos = pygame.mouse.get_pos()
        
        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game()
                
            for button in buttons:
                if button.handle_event(event):
                    return
                    
        # Обновление
        for button in buttons:
            button.check_hover(mouse_pos)
        
        # Отрисовка
        if has_background:
            screen.blit(background_image, (0, 0))
        else:
            screen.fill(BACKGROUND_COLOR)
        
        # Заголовок
        title_text = title_font.render("Edojidai", True, TITLE_COLOR)
        title_rect = title_text.get_rect(center=(WIDTH//2, 120))
        screen.blit(title_text, title_rect)
        
        # Подзаголовок
        subtitle_text = button_font.render("Главное меню", True, TEXT_COLOR)
        subtitle_rect = subtitle_text.get_rect(center=(WIDTH//2, 180))
        screen.blit(subtitle_text, subtitle_rect)
        
        # Кнопки
        for button in buttons:
            button.draw(screen)
        
        # Копирайт
        copyright_text = copyright_font.render("© 2024  Игра сделана DeKocoDeerSnake и iroslav-rik. Все права защищены.", True, TEXT_COLOR)
        screen.blit(copyright_text, (WIDTH - copyright_text.get_width() - 20, HEIGHT - 30))
        
        # Версия игры
        version_text = copyright_font.render("Версия 1.0", True, TEXT_COLOR)
        screen.blit(version_text, (20, HEIGHT - 30))
        
        pygame.display.flip()
        clock.tick(60)

# Запуск меню
if __name__ == "__main__":
    main_menu()
