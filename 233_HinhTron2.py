import math


def getDensity(R, OC, firstSegment):
    centered1 = OC - R
    segment1 = OC * (centered1 / firstSegment)
    base1 = 2 * R * (centered1 / firstSegment)
    R2 = (base1 * centered1) / (segment1 * 2 + base1)
    circle2 = R2 * R2 * math.pi
    area2 = centered1 * base1 / 2

    centered2 = centered1 - 2 * R2
    segment2 = segment1 * (centered2 / centered1)
    base2 = base1 * (centered2 / centered1)

    area3 = centered2 * base2 / 2

    area2to3 = area2 - area3

    density = circle2 / area2to3
    density2 = density * area2
    return density2


def sol():
    a, b = map(float, input().split())
    if a > b:
        a, b = b, a
    c = math.sqrt(a * a + b * b)
    R = (a * b) / (a + b + c)
    totalArea = (a * b) / 2
    firstCircle = R * R * math.pi
    OC = math.sqrt(R * R + (b - R) * (b - R))
    firstSegment = b - R
    density = getDensity(R, OC, firstSegment)
    total = (density + firstCircle)/totalArea
    print("%.4f" % total)


if __name__ == "__main__":
    sol()
