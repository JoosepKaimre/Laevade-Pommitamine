import os

import cv2 as cv
import numpy as np


def kasutaja_laud_pildilt(pildi_nimi):
    pilt_rgb = cv.imread(os.path.join(os.path.dirname(__file__), "pildid", pildi_nimi))
    pilt_hall = cv.cvtColor(pilt_rgb, cv.COLOR_BGR2GRAY)

    templatede_andmed = [(" ", os.path.join(os.path.dirname(__file__), "pildid", "T.png"), 0.8),
                         ("O", os.path.join(os.path.dirname(__file__), "pildid", "L.png"), 0.8)]

    leitud_sümbolid = []
    for template_andmed in templatede_andmed:
        sümbol = template_andmed[0]
        sümboli_pildi_nimi = template_andmed[1]
        piir = template_andmed[2]

        sümboli_pilt = cv.imread(sümboli_pildi_nimi, 0)

        tulemused = cv.matchTemplate(pilt_hall, sümboli_pilt, cv.TM_CCOEFF_NORMED)
        asukohad = np.where(tulemused >= piir)

        for (x, y) in zip(*asukohad[::-1]):
            leitud_sümbolid.append([x, y, sümbol])

    for leid in leitud_sümbolid:
        y = leid[1]
        leid[1] = 23 * round(y / 23)

    leitud_sümbolid_sorteeritud = sorted(leitud_sümbolid, key=lambda l: [l[1], l[0]])

    väljund = []
    eelmine_x, eelmine_y = (0, 0)
    for (x, y, sümbol) in leitud_sümbolid_sorteeritud:
        if (abs(x - eelmine_x) > 10) or (abs(y - eelmine_y) > 12):
            väljund.append(sümbol)
        eelmine_x, eelmine_y = (x, y)

    # Moodustame leitud sümbolitest ühise pika sõne, mille tagastame
    väljund_sõne = "".join(väljund)

    return [list(väljund_sõne[i:i + 10]) for i in range(0, 100, 10)]
