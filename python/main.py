import turtle
import random
import time

# Ekranı ayarla
screen = turtle.Screen()
screen.title("Kaplumbağa Oyunu")
screen.bgcolor("lightblue")
screen.setup(width=600, height=600)

# Skor ve süre
score = 0
time_limit = 30  # oyun süresi saniye
start_time = time.time()

# Son tıklama zamanı (başlangıçta oyun başladı)
last_click_time = time.time()

# Skor gösterici
score_writer = turtle.Turtle()
score_writer.hideturtle()
score_writer.penup()
score_writer.goto(-250, 260)
score_writer.write(f"Skor: {score}", font=("Arial", 16, "bold"))

# Zaman gösterici
timer_writer = turtle.Turtle()
timer_writer.hideturtle()
timer_writer.penup()
timer_writer.goto(150, 260)
timer_writer.write(f"Süre: {time_limit}", font=("Arial", 16, "bold"))

# Kaplumbağa karakteri
kaplumbaga = turtle.Turtle()
kaplumbaga.shape("turtle")
kaplumbaga.color("green")
kaplumbaga.penup()
kaplumbaga.speed(0)

def move_turtle():
    """Kaplumbağayı rastgele bir yere ışınla"""
    x = random.randint(-250, 250)
    y = random.randint(-250, 250)
    kaplumbaga.goto(x, y)

def update_score_and_move(x, y):
    """Kaplumbağaya tıklanınca skor artır ve kaplumbağayı hareket ettir"""
    global score, last_click_time
    if time.time() - start_time < time_limit:
        score += 1
        score_writer.clear()
        score_writer.write(f"Skor: {score}", font=("Arial", 16, "bold"))
        move_turtle()
        last_click_time = time.time()  # Son tıklama zamanını güncelle

def check_idle_move():
    """Eğer 2 saniyeden uzun tıklama yoksa kaplumbağa hareket eder"""
    global last_click_time
    if time.time() - last_click_time > 2 and time.time() - start_time < time_limit:
        move_turtle()
        last_click_time = time.time()  # Hareketten sonra zamanı güncelle
    # 500 ms sonra tekrar kontrol et
    screen.ontimer(check_idle_move, 500)

def update_timer():
    elapsed = time.time() - start_time
    remaining = int(time_limit - elapsed)
    if remaining >= 0:
        timer_writer.clear()
        timer_writer.write(f"Süre: {remaining}", font=("Arial", 16, "bold"))
        screen.ontimer(update_timer, 1000)
    else:
        kaplumbaga.hideturtle()
        timer_writer.clear()
        timer_writer.write("Süre doldu!", font=("Arial", 18, "bold"))
        score_writer.goto(-50, 0)
        score_writer.clear()
        if score >= 50:
            score_writer.color("green")
            score_writer.write(f"Tebrikler! Skorun: {score}", font=("Arial", 24, "bold"))
        else:
            score_writer.color("red")
            score_writer.write(f"Yenildin! Skorun: {score}", font=("Arial", 24, "bold"))


# Olay dinleyici ata
kaplumbaga.onclick(update_score_and_move)

# Oyunu başlat
move_turtle()
update_timer()
check_idle_move()
screen.mainloop()
