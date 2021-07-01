# -*- coding: utf-8 -*-
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('fivethirtyeight')

x_vals = []
y_vals = []

index = count()


def animate(i):
    data = pd.read_csv('data.csv')
    x = data['itr']
    y1 = data['att1']
    y2 = data['med1']
    y3 = data['att2']
    y4 = data['med2']

    plt.cla()

    plt.plot(x, y1, label='HighAtenção')
    plt.plot(x, y2, label='HighMeditação')
    plt.plot(x, y3, label='LowMeditação')
    plt.plot(x, y4, label='LowMeditação')

    plt.legend(loc='upper left')
    plt.tight_layout()


ani = FuncAnimation(plt.gcf(), animate, interval=1000)

plt.tight_layout()
plt.show()
