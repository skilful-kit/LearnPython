import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Алхимия")
clock = pygame.time.Clock()

BG_COLOR = (30, 30, 40)
PANEL_COLOR = (45, 45, 60)
TEXT_COLOR = (240, 240, 240)
WHITE = (255, 255, 255)

FONT = pygame.font.SysFont("Arial", 16)
TITLE_FONT = pygame.font.SysFont("Arial", 20, bold=True)

RECIPES = {
    frozenset(["Вода", "Огонь"]): "Пар",
    frozenset(["Земля", "Вода"]): "Грязь",
    frozenset(["Воздух", "Огонь"]): "Энергия",
    frozenset(["Земля", "Огонь"]): "Лава",
    frozenset(["Лава", "Вода"]): "Камень",
    frozenset(["Воздух", "Камень"]): "Песок",
    frozenset(["Песок", "Пар"]): "Бурмалда"
}

ELEMENT_COLORS = {
    "Вода": (50, 150, 255),
    "Огонь": (255, 80, 50),
    "Земля": (139, 69, 19),
    "Воздух": (173, 216, 230),
    "Пар": (220, 220, 220),
    "Грязь": (101, 67, 33),
    "Энергия": (255, 215, 0),
    "Лава": (207, 16, 32),
    "Камень": (128, 128, 128),
    "Песок": (244, 164, 96),
    "Бурмалда": (139, 0, 255)
}

opened_elements = ["Вода", "Огонь", "Земля", "Воздух"]

class Element:
    def __init__(self, name, x, y):
        self.name = name
        self.color = ELEMENT_COLORS.get(name, (200, 200, 200))
        self.rect = pygame.Rect(x, y, 90, 40)
        self.dragging = False

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect, border_radius=5)
        pygame.draw.rect(surface, WHITE, self.rect, width=1, border_radius=5)
        
        text_surf = FONT.render(self.name, True, (0, 0, 0) if self.color[0] > 200 and self.color[1] > 200 else WHITE)
        text_rect = text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf, text_rect)

active_elements = []
selected_element = None
offset_x = 0
offset_y = 0

def check_combination(el1, el2):
    pair = frozenset([el1.name, el2.name])
    if pair in RECIPES:
        new_name = RECIPES[pair]
        if new_name not in opened_elements:
            opened_elements.append(new_name)
        new_el = Element(new_name, el2.rect.x, el2.rect.y)
        active_elements.remove(el1)
        active_elements.remove(el2)
        active_elements.append(new_el)
        return True
    return False

running = True
while running:
    mouse_pos = pygame.mouse.get_pos()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                active_elements.clear()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for el in reversed(active_elements):
                    if el.rect.collidepoint(mouse_pos):
                        selected_element = el
                        el.dragging = True
                        offset_x = el.rect.x - mouse_pos[0]
                        offset_y = el.rect.y - mouse_pos[1]
                        break
                
                if not selected_element and mouse_pos[0] > 700:
                    y_offset = 50
                    for name in opened_elements:
                        item_rect = pygame.Rect(710, y_offset, 170, 35)
                        if item_rect.collidepoint(mouse_pos):
                            new_el = Element(name, mouse_pos[0] - 45, mouse_pos[1] - 20)
                            new_el.dragging = True
                            selected_element = new_el
                            offset_x = new_el.rect.x - mouse_pos[0]
                            offset_y = new_el.rect.y - mouse_pos[1]
                            active_elements.append(new_el)
                            break
                        y_offset += 45

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 and selected_element:
                selected_element.dragging = False
                
                combined = False
                for el in active_elements:
                    if el != selected_element and selected_element.rect.colliderect(el.rect):
                        if check_combination(selected_element, el):
                            combined = True
                            break
                
                if not combined and selected_element.rect.x > 680:
                    active_elements.remove(selected_element)
                    
                selected_element = None

        elif event.type == pygame.MOUSEMOTION:
            if selected_element and selected_element.dragging:
                selected_element.rect.x = mouse_pos[0] + offset_x
                selected_element.rect.y = mouse_pos[1] + offset_y

    screen.fill(BG_COLOR)
    
    hint_text = FONT.render("[R] - Очистить поле  |  Перетаскивайте элементы друг на друга", True, (100, 100, 120))
    screen.blit(hint_text, (20, 15))

    for el in active_elements:
        if el != selected_element:
            el.draw(screen)
    if selected_element:
        selected_element.draw(screen)

    pygame.draw.rect(screen, PANEL_COLOR, (700, 0, 200, HEIGHT))
    pygame.draw.line(screen, WHITE, (700, 0), (700, HEIGHT), 2)
    
    title_surf = TITLE_FONT.render("Элементы:", True, TEXT_COLOR)
    screen.blit(title_surf, (710, 15))
    
    y_offset = 50
    for name in opened_elements:
        item_rect = pygame.Rect(710, y_offset, 170, 35)
        color = ELEMENT_COLORS.get(name, (200, 200, 200))
        
        pygame.draw.rect(screen, color, item_rect, border_radius=3)
        pygame.draw.rect(screen, WHITE, item_rect, width=1, border_radius=3)
        
        text_surf = FONT.render(name, True, (0, 0, 0) if color[0] > 200 and color[1] > 200 else WHITE)
        text_rect = text_surf.get_rect(center=item_rect.center)
        screen.blit(text_surf, text_rect)
        
        y_offset += 45

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
