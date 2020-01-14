import pprint
import pyautogui

def testScreenDetails():
    print(pyautogui.position())
    print(pyautogui.size())
    print(pyautogui.PAUSE)

def testMoveMouse():
    x, y = pyautogui.size()
    pyautogui.moveTo(x / 2, y / 2, duration=3)

def testScreenshot():
    print(pyautogui.screenshot())

def testFindImage():
    print(pyautogui.locateOnScreen('/Users/eedrah/Desktop/point-of-interest.png', grayscale=True, confidence=0.9))

def testFindAllImages():
    pprint.pprint(list(pyautogui.locateAllOnScreen('/Users/eedrah/Desktop/point-of-interest.png', confidence=0.9)))

def main():
    # testScreenDetails()
    # testMoveMouse()
    # testScreenshot()
    # testFindAllImages()

    import timeit
    print(timeit.timeit("testFindImage()", number=10, setup="from __main__ import testFindImage") / 10)
    # print(sum(timeit.repeat("testFindImage()", number=1, repeat=10, setup="from __main__ import testFindImage")) / 10)

if __name__ == '__main__':
    main()
