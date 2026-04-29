from pyscript import display
import numpy as np
import matplotlib.pyplot as plt
from js import document
import logging
logging.getLogger('matplotlib').setLevel(logging.ERROR)

# removing the font cache message
plt.figure()
plt.plot([0, 1], [0, 1])
plt.close()

days = np.array(['Mon', 'Tue', 'Wed', 'Thurs', 'Fri'])
absences = np.zeros(5, dtype=int)

def add_absence(e):
    day_index = int(document.getElementById("day").value)
    num_absences = int(document.getElementById("absences").value)

    absences[day_index] += num_absences

    plt.figure(figsize=(6,4))
    plt.plot(days, absences, marker="o", linestyle="-", color="palegoldenrod")
    plt.title("10-Emerald\'s Attendance Sheet")
    plt.xlabel("Days")
    plt.ylabel("Absences")

    display(plt.gcf(), target="plot")
    plt.close()