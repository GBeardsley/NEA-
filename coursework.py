#import modules
import pygame
from pygame import mixer

#initial setup of screen
pygame.init()
mixer.init()
FPS = 60
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Retro Racer")
sound_volume = 0.5
music_volume = 0.5
#timers
clock = pygame.time.Clock()
lapclock = pygame.time.Clock()
username = ''
pygame.mixer.set_num_channels(1)

#sounds
top_speed_sound = pygame.mixer.Sound('Top speed sound.mp3')
top_speed_sound.set_volume(sound_volume+0.5)
accelerate_sound = pygame.mixer.Sound('acceleration sound.mp3')
accelerate_sound.set_volume(sound_volume)
decelerate_sound = pygame.mixer.Sound('deceleration sound.mp3')
decelerate_sound.set_volume(sound_volume +0.5)
crash_sound = pygame.mixer.Sound('crash sound.mp3')
crash_sound.set_volume(sound_volume + 0.5)
pygame.mixer.music.load('background.mp3')
pygame.mixer.music.set_volume(music_volume)
#loops background sound
pygame.mixer.music.play(-1)

#grass animation images
grass_1 = pygame.image.load('grass 1.png')
grass_2 = pygame.image.load('grass 2.png')
grass_3 = pygame.image.load('grass 3.png')
grass_4 = pygame.image.load('grass 4.png')
grass_5 = pygame.image.load('grass 5.png')
grass_6 = pygame.image.load('grass 6.png')

#gravel animation images
gravel_1 = pygame.image.load('gravel 1.png')
gravel_2 = pygame.image.load('gravel 2.png')
gravel_3 = pygame.image.load('gravel 3.png')
gravel_4 = pygame.image.load('gravel 4.png')
gravel_5 = pygame.image.load('gravel 5.png')
gravel_6 = pygame.image.load('gravel 6.png')

#resizing animation images
grass_animation_imgs = [grass_1, grass_2, grass_3, grass_4, grass_5, grass_6]
gravel_animation_imgs = [gravel_1, gravel_2, gravel_3, gravel_4, gravel_5, gravel_6]
for i in range(len(grass_animation_imgs)):
    image = pygame.transform.scale(grass_animation_imgs[i], (50, 50))
    grass_animation_imgs[i] = image
for i in range(len(gravel_animation_imgs)):
    image = pygame.transform.scale(gravel_animation_imgs[i], (50,50))
    gravel_animation_imgs[i] = image

#function to draw text onto screen
def draw_text(x_pos, y_pos, size, color, surface, message=''):
    font = pygame.font.SysFont(None, size)
    text = font.render(message, True, color)
    surface.blit(text, (x_pos, y_pos))

#game
class Game:
    def __init__(self):
        #first screen it goes to
        self.start_screen()

    #start screen
    def start_screen(self):
        pygame.mixer.music.unpause()
        running = True
        user_input = False
        global username

        #game loop
        while running:
            font = pygame.font.Font(None, 50)

            screen.fill((105, 228, 146))
            draw_text(150, 100, 100, (61, 79, 31), screen, 'RETRO RACER')
            draw_text(260, 500, 50, (61, 79, 31), screen, 'Press Q to QUIT')

            #checking for events and key presses
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    #if enter key is pressed with a name in, then you can play the game
                    if event.key == pygame.K_RETURN:
                        #if there is no name in then, you cannot play the game
                        if username == '':
                            user_input = False
                        else:
                            user_input = True
                    elif event.key == pygame.K_BACKSPACE:
                        #if the backspace key is pressed, then it deletes the last character
                        username = username[:-1]
                    else:
                        #otherwise the characters should be added to the username
                        username = username + event.unicode

                #if the username is longer than twelve characters then no more should be added
                if len(username)> 12:
                    username = username[:-1]


            pygame.draw.rect(screen, (61,79,31), (250, 200, 300, 60))
            #before a letter is added, the screen displays the instruction - enter username
            if username == '':
                draw_text(250, 210, 50, (105, 228, 146), screen, 'Enter Username')
            username_box = font.render(username, True, (105, 228, 146))
            screen.blit(username_box, (250, 210))

            keys = pygame.key.get_pressed()

            #only if a username is entered, can you play the game
            if user_input:
                draw_text(260, 350, 50, (61, 79, 31), screen, 'Press P to PLAY')
                draw_text(230, 425, 50, (61, 79, 31), screen, 'Press M for the MENU')
                #for menu screen
                if keys[pygame.K_m]:
                    username = username[:-1]
                    self.menu_screen()
                #for game screen
                if keys[pygame.K_p]:
                    username = username[:-1]
                    self.playing_screen()
            #to leave the game
            if keys[pygame.K_q]:
                pygame.quit()

            #update screen
            pygame.display.flip()
            pygame.display.update()

    #game screen
    def playing_screen(self, running = True):
        pygame.mixer.music.pause()
        #images
        up_straight = pygame.image.load("straight 2.png")
        t_three = pygame.image.load("curve 3.png")
        t_two = pygame.image.load("curve 2.png")
        t_one = pygame.image.load("curve 1.png")
        t_four = pygame.image.load("curve 4.png")
        grass = pygame.image.load("grass.png")
        tyre_wall = pygame.image.load("tyre wall - straight green.png")
        tyre_wall = pygame.transform.scale(tyre_wall, (40, 600))
        gravel_trap = pygame.image.load("gravel trap.png")
        tyre_wall_hori = pygame.transform.rotate(tyre_wall, 90)
        tyre_wall_hori = pygame.transform.scale(tyre_wall_hori, (800, 40))
        finish = pygame.image.load("Finish line.png")
        finish = pygame.transform.scale(finish, (450, 30))
        car_one = pygame.image.load("pitstop_car_1.png")
        car_one = pygame.transform.scale(car_one, (40, 80))
        car_one = pygame.transform.rotate(car_one, 180)
        start1 = pygame.image.load("sem_1_red.png")
        start1 = pygame.transform.scale(start1, (300, 200))
        start2 = pygame.image.load("sem_2_red.png")
        start2 = pygame.transform.scale(start2, (300,200))
        start3 = pygame.image.load("sem_3_red.png")
        start3 = pygame.transform.scale(start3, (300, 200))
        start_go = pygame.image.load("sem_all_green.png")
        start_go = pygame.transform.scale(start_go, (300, 200))

        CONST_CAR_ONE = car_one

        global username

        # draw an image onto the screen in the desired position and scale it to fill the screen
        def draw_image(image, x_position, y_position):
            image = pygame.transform.scale(image, (screen_width, screen_height))
            screen.blit(image, (x + x_position, y + y_position))

        #function to draw the circuit onto the screen
        def draw_all():
            draw_image(up_straight, 0, 0)
            draw_image(t_three, 0, -600)
            draw_image(t_two, 800, -600)
            draw_image(t_three, 800, -1200)
            draw_image(t_one, 1600, -1200)
            draw_image(up_straight, 1600, -600)
            draw_image(up_straight, 1600, 0)
            draw_image(up_straight, 1600, 600)
            draw_image(up_straight, 1600, 1200)
            draw_image(t_two, 1600, 1800)
            draw_image(t_four, 800, 1800)
            draw_image(up_straight, 800, 1200)
            draw_image(t_one, 800, 600)
            draw_image(t_four, 0, 600)
            draw_image(grass, 800, 0)
            draw_image(gravel_trap, 0, -1200)
            draw_image(gravel_trap, 0, 1200)
            draw_image(gravel_trap, 0, 1800)
            screen.blit(tyre_wall, (x, y))
            screen.blit(tyre_wall, (x, y - 600))
            screen.blit(tyre_wall, (x, y - 1200))
            screen.blit(tyre_wall, (x, y + 600))
            screen.blit(tyre_wall, (x, y + 1200))
            screen.blit(tyre_wall, (x, y + 1800))
            screen.blit(tyre_wall, (x + 1600, y - 600))
            screen.blit(tyre_wall, (x + 1600, y))
            screen.blit(tyre_wall, (x + 1600, y + 600))
            screen.blit(tyre_wall, (x + 1600, y + 1200))
            screen.blit(tyre_wall, (x + 2360, y - 600))
            screen.blit(tyre_wall, (x + 2360, y - 1200))
            screen.blit(tyre_wall, (x + 2360, y))
            screen.blit(tyre_wall, (x + 2360, y + 600))
            screen.blit(tyre_wall, (x + 2360, y + 1200))
            screen.blit(tyre_wall, (x + 2360, y + 1800))
            screen.blit(tyre_wall_hori, (x + 40, y - 1200))
            screen.blit(tyre_wall_hori, (x + 800, y - 1200))
            screen.blit(tyre_wall_hori, (x + 1600, y - 1200))
            screen.blit(tyre_wall_hori, (x + 40, y + 2360))
            screen.blit(tyre_wall_hori, (x + 800, y + 2360))
            screen.blit(tyre_wall_hori, (x + 1600, y + 2360))
            screen.blit(finish, (x + 175, y + 100))


        #variables
        x = 0
        y = 0
        x_change = 0
        y_change = 0
        accel_x = 0
        accel_y = 0
        color_position = (x, y)
        direction = 0
        lap_counter = 1
        lapclock.tick()
        start_time = pygame.time.get_ticks()
        lap_times = []
        total_paused_time = 0
        crossed_start = 0
        image_time = 0
        prev_speed = 0
        iteration = 0
        starting = True

        #game loop
        while running:

            font = pygame.font.Font(None, 30)
            clock.tick(FPS)
            keys = pygame.key.get_pressed()
            start_direction = direction

            #code for key presses
            #line1 - where to read the colour of the pixel from
            #line2 - amending acceleration
            #line3 - the way it is facing
            #line4 - accelerate sound
            if keys[pygame.K_w]:
                color_position = (375, 340)
                accel_y = 0.2
                direction = 0

            if keys[pygame.K_s]:
                color_position = (375, 210)
                accel_y = -0.2
                direction = 180

            if keys[pygame.K_a]:
                color_position = (440, 275)
                accel_x = 0.2
                direction = 90

            if keys[pygame.K_d]:
                color_position = (310, 275)
                accel_x = -0.2
                direction = 270

            #two keys at once - going diagonally
            if keys[pygame.K_w] and keys[pygame.K_d]:
                direction = 315
                color_position = (355 - (25 * (2 ** (1 / 2))), 290 + (25 * (2 ** (1 / 2))))
                accel_x = -(0.2 * ((2 ** (1 / 2)) / 2))
                accel_y = 0.2 * ((2 ** (1 / 2)) / 2)

            if keys[pygame.K_s] and keys[pygame.K_d]:
                direction = 225
                color_position = (360 - (25 * (2 ** (1 / 2))), 260 - (25 * (2 ** (1 / 2))))
                accel_x = -(0.2 * ((2 ** (1 / 2)) / 2))
                accel_y = -(0.2 * ((2 ** (1 / 2)) / 2))

            if keys[pygame.K_s] and keys[pygame.K_a]:
                direction = 135
                color_position = (390 + (25 * (2 ** (1 / 2))), 260 - (25 * (2 ** (1 / 2))))
                accel_x = 0.2 * ((2 ** (1 / 2)) / 2)
                accel_y = -(0.2 * ((2 ** (1 / 2)) / 2))

            if keys[pygame.K_w] and keys[pygame.K_a]:
                direction = 45
                color_position = (390 + (25 * (2 ** (1 / 2))), 290 + (25 * (2 ** (1 / 2))))
                accel_x = 0.2 * ((2 ** (1 / 2)) / 2)
                accel_y = 0.2 * ((2 ** (1 / 2)) / 2)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                #when no button is pressed the car decelerates
                if event.type == pygame.KEYUP:
                    #makes x acceleration 0 if d or a are not pressed
                    if event.key in (pygame.K_d, pygame.K_a):
                        accel_x = 0
                    #makes y acceleration 0 if w or s are not pressed
                    elif event.key in (pygame.K_w, pygame.K_s):
                        accel_y = 0


            #car faces the correct direction
            direction_change = direction - start_direction
            if direction_change != 0:
                car_one = pygame.transform.rotate(CONST_CAR_ONE, direction)

            color_position = int(color_position[0]), int(color_position[1])
            pixel_color = screen.get_at(color_position)
            #changes the max speed depending on the colour of the pixel the car is on
            if pixel_color == (20, 160, 46, 255):
                max_speed = 8
            elif pixel_color == (214, 200, 96, 255):
                max_speed = 5
            else:
                max_speed = 15

            hit = False
            #for car collisions
            car_rect = car_one.get_rect(center = (400,300))
            #for vertical tyre walls
            for i in range (-600, 1800, 600): #1800 because plus one
                tyre_rect = tyre_wall.get_rect(topleft = (x+1600, y+i))
                if car_rect.colliderect(tyre_rect):
                    #if car is going right
                    if x_change >= 0:
                        #moves the car back by 8
                        x = x - 8
                    #if car is going left
                    elif x_change <= 0:
                        x = x + 8
                    hit = True
            for i in range (-1200, 2400, 600):
                tyre_rect = tyre_wall.get_rect(topleft = (x, y+i))
                if car_rect.colliderect(tyre_rect):
                    x = x - 8
                    hit = True
                tyre_rect = tyre_wall.get_rect(topleft = (x+2360, y+i))
                if car_rect.colliderect(tyre_rect):
                    x = x + 8
                    hit = True
            #for horizontal tyre walls
            for i in range (0, 2400, 800):
                tyre_rect = tyre_wall_hori.get_rect(topleft=(x+i, y -1200))
                if car_rect.colliderect(tyre_rect):
                    y = y - 8
                    hit = True
                tyre_rect = tyre_wall_hori.get_rect(topleft=(x +i, y +2360))
                if car_rect.colliderect(tyre_rect):
                    y = y + 8
                    hit = True

            #if the car has crashed
            if hit:
                #if the car is traveling faster than 3
                if x_change >= 3 or y_change >= 3 :
                    print('game over')
                    #stops the current sounds and plays the crash sound
                    accelerate_sound.stop()
                    decelerate_sound.stop()
                    crash_sound.play()
                    #calls game over screen
                    self.game_over(lap_times, crashed = True)

            finish_rect = finish.get_rect(topleft=(x + 175, y + 200))
            if car_rect.colliderect(finish_rect):
                if y_change <= 0:
                    y = y + 15

            # Accelerate.
            x_change += accel_x
            y_change += accel_y

            #when the acceleration is 0 (when no button is pressed) x value decreases by 0.92 of current value
            if accel_x == 0:
                x_change *= 0.92
            if accel_y == 0:
                y_change *= 0.92

            # If max_speed is exceeded.
            # Make x_change value positive and multiply it with the max_speed.
            #stops the car exceeding 15 speed
            if abs(x_change) >= max_speed:
                x_change = x_change / abs(x_change) * max_speed

            if abs(y_change) >= max_speed:
                y_change = y_change / abs(y_change) * max_speed

            if abs(x_change) >= (max_speed * ((2 ** (1 / 2)) / 2)) and abs(y_change) >= (max_speed * ((2 ** (1 / 2)) / 2)):
                x_change = x_change / abs(x_change) * (max_speed * ((2 ** (1 / 2)) / 2))
                y_change = y_change / abs(y_change) * (max_speed * ((2 ** (1 / 2)) / 2))

            # Move the object.
            x += x_change
            y += y_change

            #lap timing
            end_time = pygame.time.get_ticks()
            elapsed_time = end_time - start_time

            # pausing the game when the escape key is pressed
            if keys[pygame.K_ESCAPE]:
                is_paused = True
                #gets the time
                start_pause = pygame.time.get_ticks()
                #paused screen actions
                while is_paused:
                    keys = pygame.key.get_pressed()
                    screen.fill((105, 228, 146))
                    #screen text
                    draw_text(275,100, 100, (61,79,31), screen, 'PAUSED')
                    draw_text(200,325, 50, (61,79,31), screen, 'Press RETURN to resume')
                    draw_text(198,375,50, (61,79,31,), screen, 'Press Q to leave the game')
                    draw_text(250,415, 30, (61,79,31,), screen, '(All current progress will be lost)')
                    # check for the game closing
                    #check for keyboard inputs
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                        if keys[pygame.K_q]:
                            self.start_screen()
                    #update screen
                    pygame.display.update()
                    # check for the return key to unpause the game
                    is_paused = not pygame.key.get_pressed()[pygame.K_RETURN]

                #gets the time
                end_pause = pygame.time.get_ticks()
                end_time = pygame.time.get_ticks()
                elapsed_time = end_time - start_time

                #finds the difference between the times whilst it is paused - the paused time
                paused_time = end_pause - start_pause
                #adds all paused times together
                total_paused_time = total_paused_time + paused_time

            #finds the time that has passed, when not paused
            net_elapsed_time = elapsed_time - total_paused_time - 3000

            #prints the time
            ms = int(net_elapsed_time % 1000)
            s = int(net_elapsed_time / 1000 % 60)
            m = int(net_elapsed_time / 60000 % 60)

            #format the time
            time = f'{m}:{s}:{ms}'

            #where to take collision from
            front_of_car = (400, 230)

            #check to see if collides with the finsh line
            finish_collision = False
            if finish_rect.collidepoint(front_of_car):
                finish_collision = True

            #if it does collide then get the lap time
            if finish_collision:
                lapclock.tick()
                lap_time = lapclock.get_time()
                ms = int(lap_time % 1000)
                s = int(lap_time / 1000 % 60)
                crossed_start = crossed_start + 1
                #m = int(lap_time / 60000 % 60)
                #check if lap has been 2 seconds
                if lap_time < 2000:
                    pass
                else:
                    #changes the milliseconds to 3 digits long
                    while len(str(ms)) < 3:
                        ms = str(ms) + '0'
                    #changes the seconds to 2 digits long
                    if len(str(s)) == 1:
                        s = '0' + str(s)


                    #check to see how many times the finish line has been crossed
                    if crossed_start < 2:
                        pass
                    else:
                       #format the lap time
                        lap_time = f'{s}:{ms}'
                        print('lap', lap_counter, ':', lap_time)
                        lap_counter = lap_counter + 1
                        #add lap time to the list of lap times
                        lap_times.append(lap_time)
                        print(lap_times)

            #only allows 3 laps to happen
            if lap_counter == 4:
                #write the total lap to the leaderboard
                with open('Total_Leaderboard.txt', 'a') as file:
                    file.write(time + ' - ' + username + '\n')
                #write each individual lap time to the other leaderboard
                with open('Lap_Leaderboard.txt', 'a') as file:
                    for i in range(0, 3):
                        file.write(lap_times[i] + ' - ' + username + '\n')

                times = list()
                total_times = list()
                # open file to read
                with open('Lap_Leaderboard.txt', 'r') as file:
                    for line in file:
                        # adds time to list of times
                        times.append(line)
                    # sorts the list
                    times.sort()
                #open file to write
                with open('Lap_Leaderboard.txt', 'w') as file:
                    #writes the sorted list back into the text file
                    for time in times:
                        file.write(time)
                #opens total times to read
                with open('Total_Leaderboard.txt', 'r') as file:
                   for line in file:
                       #adds time to list
                       total_times.append(line)
                   #sorts list
                   total_times.sort()
                #opens file to write
                with open('Total_Leaderboard.txt', 'w') as file:
                   #writes the sorted list back into the text file
                   for time in total_times:
                       file.write(time)

                #end the game
                self.game_over(lap_times, crashed = False)


            #finds the speed using pythagoras
            total_speed = int(((x_change ** 2) + (y_change ** 2)) ** (1 / 2))

            #check if increasing speed
            if prev_speed > total_speed:
                accelerate_sound.stop()
                decelerate_sound.play()
            #check is decreasing the speed
            elif prev_speed < total_speed:
                decelerate_sound.stop()
                accelerate_sound.play()


            #sounds for top speed
            if total_speed == 15:
                accelerate_sound.stop()
                top_speed_sound.play()
                #plays sound from beginning
            elif total_speed == 0:
                decelerate_sound.stop()
                accelerate_sound.stop()
            else:
                top_speed_sound.stop()
                # stops sound

            #converts to a string
            total_speed = str(total_speed)
            prev_speed = int(total_speed)
            # puts speed and lap information on screen
            speed_text = font.render(('Speed: ' + total_speed), True, (255, 255, 255))
            time_text = font.render(time, True, (255, 255, 255))
            lap_number = font.render(('Lap: ' + str(lap_counter)), True, (255, 0, 0))

            #white background
            screen.fill((255, 255, 255))
            #circuit background
            draw_all()
            #check the pixel colour
            pixel_color = screen.get_at(color_position)
            #play the correct animation
            if pixel_color == (20, 160, 46, 255):
                gravel_ani = False
                grass_ani = True
            elif pixel_color == (214, 200, 96, 255):
                grass_ani = False
                gravel_ani = True
            else:
                grass_ani = False
                gravel_ani = False
            #car
            screen.blit(car_one, car_rect)
            #speed
            screen.blit(speed_text, (370, 500))
            #lap number
            screen.blit(lap_number, (50, 10))
            #time
            screen.blit(time_text, (370, 100))
            #grass animations
            if grass_ani:
                #checks to see where in the list it is
                if iteration > len(grass_animation_imgs) - 1:
                    #if it is at the end, restart at the start of the list
                    iteration = 0
                grass_image = grass_animation_imgs[iteration]
                #show the image at the position in the list, at the corresponding coordinates
                screen.blit(grass_image, color_position)
                iteration = iteration + 1
            #gravel animation
            if gravel_ani:
                # checks to see where in the list it is
                if iteration > len(gravel_animation_imgs) - 1:
                    # if it is at the end, restart at the start of the list
                    iteration = 0
                gravel_image = gravel_animation_imgs[iteration]
                # show the image at the position in the list, at the corresponding coordinates
                screen.blit(gravel_image, color_position)
                iteration = iteration + 1

            #start sequence
            while starting:

                image_time += 1
                if image_time < 1000:
                    screen.blit(start1, (250, 100))
                elif image_time < 2000:
                    screen.blit(start2, (250, 100))
                elif image_time < 3000:
                    screen.blit(start3, (250, 100))
                elif image_time > 3000:
                    starting = False
                pygame.display.update()

            if elapsed_time < 4000:
                screen.blit(start_go, (250, 100))

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
            #end_starting = pygame.time.get_ticks()
            pygame.display.flip()
            pygame.display.update()

    #menu screen
    def menu_screen(self, running = True):
        global sound_volume
        global music_volume
        pygame.mixer.music.unpause()

        # import and scale the + - images
        def load_scale_image(image_file, x_pos, y_pos):
            image = pygame.image.load(image_file)
            image = pygame.transform.scale(image, (30, 30))
            screen.blit(image, (x_pos, y_pos))
            image_rect = image.get_rect()
            image_rect.center = (x_pos, y_pos)
            return image, image_rect

        while running:
            pygame.mixer.music.set_volume(music_volume)
            #get the mouse position on the screen

            #make the menu screen
            screen.fill((105, 228, 146))
            #draws the text onto the screen
            draw_text(300, 100, 100, (61, 79, 31), screen, 'MENU')
            draw_text(150, 450, 50, (61, 79, 31), screen, 'Press BACKSPACE to go back')
            draw_text(150, 350, 50, (61, 79, 31), screen, 'Press L to see the leaderboard')
            draw_text(233, 250, 40, (61, 79, 31), screen, 'SOUNDS:          ' + str(sound_volume))
            draw_text(50, 300, 40, (61,79, 31), screen, 'BACKGROUND MUSIC:          ' + str(music_volume))
            #add the sound buttons

            # load + - images to screen
            sound_add, sound_add_rect = load_scale_image('add.png', 375, 248)
            sound_sub, sound_sub_rect = load_scale_image('subtract.png', 505, 248)
            background_add, background_add_rect = load_scale_image('add.png', 375, 298)
            background_sub, background_sub_rect = load_scale_image('subtract.png', 505, 298)

            keys = pygame.key.get_pressed()
            #need to add ability to resume game where it was paused
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            #increase/decrease the corresponding volumes depending on which image is pressed
                if event.type == pygame.MOUSEBUTTONDOWN:  # Detects a single mouse click
                    mouse_pos = pygame.mouse.get_pos()
                    if sound_volume > 1 or sound_volume < 0:
                        pass
                    else:
                        if sound_add_rect.collidepoint(mouse_pos):
                            sound_volume += 0.1
                        if sound_sub_rect.collidepoint(mouse_pos):
                            sound_volume -= 0.1
                        if background_add_rect.collidepoint(mouse_pos):
                            music_volume += 0.1
                        if background_sub_rect.collidepoint(mouse_pos):
                            music_volume -= 0.1

            #goes to start screen
            if keys[pygame.K_BACKSPACE]:
                self.start_screen()

            #goes to leaderboard screen
            if keys[pygame.K_l]:
                self.leaderboard()

            pygame.display.flip()
            pygame.display.update()

    #leaderboard screen
    def leaderboard(self, running = True):
        while running:
            #colors background and adds text onto screen
            screen.fill((105, 228, 146))
            keys = pygame.key.get_pressed()
            #draws text onto the screen
            draw_text(130, 100, 100, (61,79, 31), screen, 'LEADERBOARDS')
            draw_text(150, 450, 50, (61,79,31), screen, 'Press BACKSPACE to go back')
            draw_text(100, 200, 40, (61,79,31), screen, 'Best Lap Time:')
            draw_text(450, 200, 40, (61,79,31), screen, 'Best Total Time:')
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if keys[pygame.K_BACKSPACE]:
                    self.menu_screen()
            #lists for adding times too
            lap_top_scores = 5
            total_top_scores = 5
            laps = list()
            totals = list()

            #opens lap file to read
            with open ('Lap_Leaderboard.txt', 'r') as file:
                for line in file:
                    #adds time to the laps list - taking away the last letter ('\n')
                    laps.append(line [:-1])

            #if the list is less than 5 then it will only print the number of times in the list
            if len(laps) < 5:
                lap_top_scores = len(laps)
            #if the list is zero, then no data will show
            if len(laps) == 0:
                draw_text(100, 250, 35, (61, 79, 31), screen, 'No data available yet')
            else:
                # for the top five times, print it to the screen
                for i in range (lap_top_scores):
                    draw_text(100, 250+(i*35), 35, (61,79,31), screen, (str(i+1) + ': ' + laps[i]))
            #opens total file to read
            with open ('Total_Leaderboard.txt', 'r') as file:
                for line in file:
                    #adds time to the totals list - taking away the last letter ('\n')
                    totals.append(line [:-1])

            # if the list is less than 5 then it will only print the number of times in the list
            if len(totals) < 5:
                total_top_scores = len(totals)
            #if the list is zero then no data will show
            if len(totals) == 0:
                draw_text(450, 250, 35, (61, 79, 31), screen, 'No data available yet')
            else:
                # for the top five times, print it to the screen
                for j in range (total_top_scores):
                    draw_text(450, 250+(j*35), 35, (61, 79, 31), screen, (str(j+1) + ': ' + totals[j]))


            pygame.display.flip()
            pygame.display.update()


    #game finished screen - depending if you crashed or not
    def game_over(self, lap_times, crashed, running = True):
        while running:
            #if the user crashed show this screen
            if crashed:
                screen.fill((228, 76, 76))
            #if the user completes 3 laps, show this screen

            else:
                screen.fill((240, 178, 161))

            keys = pygame.key.get_pressed()
            #text that appears on both game over screens
            draw_text(200, 150, 100, (0, 0, 0), screen, 'GAME OVER')
            draw_text(75, 300, 60, (0, 0, 0), screen, 'Press BACKSPACE to return home')
            draw_text(130, 450, 60, (0,0,0), screen, 'Press ENTER to play again')
            # if the user crashed, show this screen
            if crashed:
                draw_text(255, 225, 75, (0, 0, 0), screen, 'You Crashed')
            #if the user completed 3 laps, show this screen
            elif not crashed:
                for i in range (0, 3):
                    #prints lap times
                    draw_text(300, 350 + (i*30), 50, (0,0,0), screen, 'Lap' + str(i+1) + ': ' + lap_times[i])

            #exit game
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            #goes back to start screen
            if keys[pygame.K_BACKSPACE]:
                self.start_screen()
            if keys[pygame.K_RETURN]:
                self.playing_screen()

            #update screen
            pygame.display.flip()
            pygame.display.update()



game = Game()

pygame.quit()
