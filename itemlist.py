import sys
import random
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class ItemList(QWidget):

    # randomItems 함수의 재료들
    numList = [0, 1, 2, 3, 4, 5, 6, 7]
    items = ['아이폰', '레노버 노트북', '커버낫 티셔츠', '버즈 프로', '선글라스', '나이키 신발', '핸드크림', '30cm 자']
    itemsPrice = ['1,000,000', '1,000,000', '30,000', '70,000', '20,000', '150,000', '8,000', '700']
    presentItemsList = []

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        itemList = QLabel('물건 목록', self)

        self.itemBox = QTextEdit(self)
        self.myItemBox = QTextEdit(self)

        buyButton = QPushButton("Buy", self)
        sellButton = QPushButton("Sell", self)

        self.presentItemsBox = QComboBox(self)
        if len(self.presentItemsList) != 0:
            self.presentItemsBox.addItem(self.presentItemsList[0])
            self.presentItemsBox.addItem(self.presentItemsList[1])
            self.presentItemsBox.addItem(self.presentItemsList[2])
            self.presentItemsBox.addItem(self.presentItemsList[3])

        hbox = QHBoxLayout()
        hbox.addWidget(itemList)
        hbox.addStretch(1)

        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.itemBox)
        hbox2.addWidget(self.myItemBox)

        hbox3 = QHBoxLayout()
        hbox3.addWidget(self.presentItemsBox)
        hbox3.addWidget(buyButton)
        hbox3.addWidget(sellButton)
        hbox3.addStretch(1)


        vbox = QVBoxLayout()
        vbox.addLayout(hbox)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)
        vbox.addStretch(1)
        self.setLayout(vbox)

        #상품 4개 뽑기
        self.randomItems()
        self.randomItems()
        self.randomItems()
        self.randomItems()

        #창 생성
        self.setGeometry(300, 300, 1400, 300)
        self.setWindowTitle('Game')
        self.show()


    #무작위 상품 선정
    def randomItems(self):
        num = self.numList.index(random.choice(self.numList)) #numList의 아무 숫자의 인덱스를 고름
        self.presentItemsList.append(self.items[num])
        self.itemBox.append('이름 : '+self.items.pop(num)+', '+self.itemsPrice.pop(num)) #인덱스에 해당하는 상품 이름과 가격을 표시
        self.itemBox.append('') #한줄 공백
        self.numList.pop(num) #한번 쓴 인덱스는 제거(중복 방지)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ItemList()
    sys.exit(app.exec_())
