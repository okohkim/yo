{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOCMTqcZlUDKcoJ0j2//8m+",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/okohkim/yo/blob/main/pong.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "deit-OrFj7KZ"
      },
      "outputs": [],
      "source": [
        "import pygame\n",
        "import sys\n",
        "\n",
        "# Pygame 초기화\n",
        "pygame.init()\n",
        "\n",
        "# 색상 정의\n",
        "white = (255, 255, 255)\n",
        "black = (0, 0, 0)\n",
        "\n",
        "# 화면 크기 설정\n",
        "width, height = 800, 600\n",
        "screen = pygame.display.set_mode((width, height))\n",
        "pygame.display.set_caption(\"Pong Game\")\n",
        "\n",
        "# 공 설정\n",
        "ball_size = 20\n",
        "ball_x = width // 2\n",
        "ball_y = height // 2\n",
        "ball_speed_x = 3\n",
        "ball_speed_y = 3\n",
        "\n",
        "# 패들 설정\n",
        "paddle_width = 10\n",
        "paddle_height = 100\n",
        "paddle_speed = 6\n",
        "paddle1_x = 50\n",
        "paddle1_y = height // 2 - paddle_height // 2\n",
        "paddle2_x = width - 50 - paddle_width\n",
        "paddle2_y = height // 2 - paddle_height // 2\n",
        "\n",
        "# 점수 초기화\n",
        "score1 = 0\n",
        "score2 = 0\n",
        "\n",
        "# 폰트 설정\n",
        "font = pygame.font.Font(None, 74)\n",
        "\n",
        "# 게임 루프\n",
        "while True:\n",
        "    for event in pygame.event.get():\n",
        "        if event.type == pygame.QUIT:\n",
        "            pygame.quit()\n",
        "            sys.exit()\n",
        "\n",
        "    # 키 입력 처리\n",
        "    keys = pygame.key.get_pressed()\n",
        "    if keys[pygame.K_w] and paddle1_y > 0:\n",
        "        paddle1_y -= paddle_speed\n",
        "    if keys[pygame.K_s] and paddle1_y < height - paddle_height:\n",
        "        paddle1_y += paddle_speed\n",
        "    if keys[pygame.K_UP] and paddle2_y > 0:\n",
        "        paddle2_y -= paddle_speed\n",
        "    if keys[pygame.K_DOWN] and paddle2_y < height - paddle_height:\n",
        "        paddle2_y += paddle_speed\n",
        "\n",
        "    # 공 위치 업데이트\n",
        "    ball_x += ball_speed_x\n",
        "    ball_y += ball_speed_y\n",
        "\n",
        "    # 공이 위아래 벽에 부딪혔을 때 방향 전환\n",
        "    if ball_y <= 0 or ball_y >= height - ball_size:\n",
        "        ball_speed_y = -ball_speed_y\n",
        "\n",
        "    # 패들에 부딪혔을 때 방향 전환\n",
        "    if (ball_x <= paddle1_x + paddle_width and paddle1_y < ball_y < paddle1_y + paddle_height) or \\\n",
        "       (ball_x >= paddle2_x - ball_size and paddle2_y < ball_y < paddle2_y + paddle_height):\n",
        "        ball_speed_x = -ball_speed_x\n",
        "\n",
        "    # 점수 계산\n",
        "    if ball_x <= 0:\n",
        "        score2 += 1\n",
        "        ball_x, ball_y = width // 2, height // 2\n",
        "    if ball_x >= width:\n",
        "        score1 += 1\n",
        "        ball_x, ball_y = width // 2, height // 2\n",
        "\n",
        "    # 화면 그리기\n",
        "    screen.fill(black)\n",
        "    pygame.draw.rect(screen, white, (paddle1_x, paddle1_y, paddle_width, paddle_height))\n",
        "    pygame.draw.rect(screen, white, (paddle2_x, paddle2_y, paddle_width, paddle_height))\n",
        "    pygame.draw.ellipse(screen, white, (ball_x, ball_y, ball_size, ball_size))\n",
        "\n",
        "    # 점수 표시\n",
        "    score_text = font.render(f\"{score1} - {score2}\", True, white)\n",
        "    screen.blit(score_text, (width // 2 - score_text.get_width() // 2, 10))\n",
        "\n",
        "    pygame.display.flip()\n",
        "\n",
        "    pygame.time.Clock().tick(60)"
      ]
    }
  ]
}