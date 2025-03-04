import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 370558433 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 1 - p
    m = max(x)
    n = len(x)
    return m / (1 - alpha/2)**(1/n), m / (alpha / 2)**(1/n)

