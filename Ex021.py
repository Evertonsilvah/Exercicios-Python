#Para tocar MP3 é necessário importar um módulo. Pygame é um modulo de jogos e pode ser usado.
import pygame
#Necessário usar a função abaixo para iniciar o Pygame
pygame.init()

#Para carregar o arquivo MP3 desejado. Para facilitar, deixar na mesma pasta com nome simples.
pygame.mixer.music.load('ex021.mp3')
#Para iniciar a musica
pygame.mixer.music.play()
input('Pressione a tecla "Enter" para acabar a musica.')
