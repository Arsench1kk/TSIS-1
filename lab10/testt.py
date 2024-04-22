import pygame
import sys

pygame.init()

# Установка размеров окна и цветов
width = 800
height = 600
background_color = (230, 230, 230)
input_box_color = (255, 255, 255)
text_color = (70, 70, 70)
active_color = pygame.Color('dodgerblue2')
inactive_color = pygame.Color('lightskyblue3')

# Создание окна
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Консольный ввод данных в Pygame")

# Функция для рисования текста на экране
def draw_text(surface, text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_surface, text_rect)

# Основной игровой цикл
def main():
    font = pygame.font.Font(None, 36)  # Загрузка шрифта
    user_input = ""  # Переменная для хранения ввода пользователя
    input_box = pygame.Rect(100, 200, 600, 50)  # Область для ввода данных
    active = False  # Флаг, указывающий на активность области ввода

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):  # Если область ввода была кликнута
                    active = not active
                else:
                    active = False
            elif event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:  # Если нажата клавиша Enter
                        print("Пользователь ввел:", user_input)
                        user_input = ""  # Очищаем строку ввода
                    elif event.key == pygame.K_BACKSPACE:  # Если нажата клавиша Backspace
                        user_input = user_input[:-1]  # Удаляем последний символ из строки ввода
                    else:
                        user_input += event.unicode  # Добавляем символы в строку ввода

        screen.fill(background_color)  # Заливка экрана цветом фона

        # Рисуем область для ввода данных
        pygame.draw.rect(screen, active_color if active else inactive_color, input_box)
        draw_text(screen, user_input, font, text_color, input_box.x + 10, input_box.y + 10)

        # Рисуем подсказку
        draw_text(screen, "Введите данные и нажмите Enter:", font, text_color, 100, 150)

        pygame.display.flip()

if __name__ == "__main__":
    main()
