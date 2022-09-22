import sys
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel, QSqlQueryModel
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import re


class DataGrid(QWidget):
    def __init__(self, parent=None):
        super(DataGrid, self).__init__(parent)
        # 声明数据库连接
        self.db = None
        # 布局管理器
        self.layout = QVBoxLayout()
        # 查询模型
        self.queryModel = QSqlQueryModel()
        # 表格视图
        self.tableView = QTableView()
        self.tableView.setModel(self.queryModel)
        #
        self.totalPageLabel = QLabel()
        self.currentPageLabel = QLabel()
        self.switchPageLineEdit = QLineEdit()
        self.prevButton = QPushButton("Prev")
        self.nextButton = QPushButton("Next")
        self.switchPageButton = QPushButton("Switch")
        # 当前页
        self.currentPage = 1
        # 总页数
        self.totalPage = 1
        # 总记录数
        self.totalRecordCount = None
        # 每页记录数
        self.pageRecordCount = 4

        self.initUI()
        self.initializedModel()
        self.setUpConnect()
        self.updateStatus()

    def initUI(self):
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.layout.addWidget(self.tableView)

        hLayout = QHBoxLayout()
        hLayout.addWidget(self.prevButton)
        hLayout.addWidget(self.nextButton)
        hLayout.addWidget(QLabel("跳转到"))
        self.switchPageLineEdit.setFixedWidth(40)
        hLayout.addWidget(self.switchPageLineEdit)
        hLayout.addWidget(QLabel("页"))
        hLayout.addWidget(self.switchPageButton)
        hLayout.addWidget(QLabel("当前页："))
        hLayout.addWidget(self.currentPageLabel)
        hLayout.addWidget(QLabel("总页数："))
        hLayout.addWidget(self.totalPageLabel)
        hLayout.addStretch(1)

        self.layout.addLayout(hLayout)
        self.setLayout(self.layout)

        self.setWindowTitle("DataGrid")
        self.resize(600, 300)

    def setUpConnect(self):
        self.prevButton.clicked.connect(self.onPrevPage)
        self.nextButton.clicked.connect(self.onNextPage)
        self.switchPageButton.clicked.connect(self.onSwitchPage)

    def initializedModel(self):
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("/home/user/test.db")
        if not self.db.open():
            return False
        self.queryModel.setHeaderData(0, Qt.Horizontal, "ID")
        self.queryModel.setHeaderData(1, Qt.Horizontal, "Name")
        self.queryModel.setHeaderData(2, Qt.Horizontal, "Sex")
        self.queryModel.setHeaderData(3, Qt.Horizontal, "Age")
        # 获取表的所有记录数
        sql = "SELECT * FROM student"
        self.queryModel.setQuery(sql, self.db)
        self.totalRecordCount = self.queryModel.rowCount()
        if self.totalRecordCount % self.pageRecordCount == 0:
            self.totalPage = self.totalRecordCount / self.pageRecordCount
        else:
            self.totalPage = int(self.totalRecordCount / self.pageRecordCount) + 1
        # 显示第1页
        sql = "SELECT * FROM student limit %d,%d" % (0, self.pageRecordCount)
        self.queryModel.setQuery(sql, self.db)

    def onPrevPage(self):
        self.currentPage -= 1
        limitIndex = (self.currentPage - 1) * self.pageRecordCount
        self.queryRecord(limitIndex)
        self.updateStatus()

    def onNextPage(self):
        self.currentPage += 1
        limitIndex = (self.currentPage - 1) * self.pageRecordCount
        self.queryRecord(limitIndex)
        self.updateStatus()

    def onSwitchPage(self):
        szText = self.switchPageLineEdit.text()
        pattern = re.compile('^[0-9]+$')
        match = pattern.match(szText)
        if not match:
            QMessageBox.information(self, "提示", "请输入数字.")
            return
        if szText == "":
            QMessageBox.information(self, "提示", "请输入跳转页面.")
            return
        pageIndex = int(szText)
        if pageIndex > self.totalPage or pageIndex < 1:
            QMessageBox.information(self, "提示", "没有指定的页，清重新输入.")
            return

        limitIndex = (pageIndex - 1) * self.pageRecordCount
        self.queryRecord(limitIndex)
        self.currentPage = pageIndex
        self.updateStatus()

    # 根据分页查询记录
    def queryRecord(self, limitIndex):
        sql = "SELECT * FROM student limit %d,%d" % (limitIndex, self.pageRecordCount)
        self.queryModel.setQuery(sql)

    # 更新空间状态
    def updateStatus(self):
        self.currentPageLabel.setText(str(self.currentPage))
        self.totalPageLabel.setText(str(self.totalPage))
        if self.currentPage <= 1:
            self.prevButton.setEnabled(False)
        else:
            self.prevButton.setEnabled(True)

        if self.currentPage >= self.totalPage:
            self.nextButton.setEnabled(False)
        else:
            self.nextButton.setEnabled(True)

    # 界面关闭时关闭数据库连接
    def closeEvent(self, event):
        self.db.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DataGrid()
    window.show()
    sys.exit(app.exec_())
