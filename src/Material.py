from PyQt5.QtSql import QSqlQueryModel, QSqlQuery
from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtWidgets import QTableView


class Model(QSqlQueryModel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.refresh()

    def refresh(self):
        sql = '''
              select mtype.type, mat.name, mat.min_quantity, mat.quantity,
              (
              select string_agg(name, ', ') from (
                 select name from suppliers
                 where id in (
                    select supplier_id from suppliers_materials
                    where material_id = mat.id
              )) as supplier_names
              )
              from materials as mat
              inner join material_type as mtype
              on mat.material_type = mtype.id;
        '''
        self.setQuery(sql)

class View(QTableView):
    def __init__(self, parent=None):
        super(). __init__(parent)
        model = Model(parent=self)
        self.setModel(model)
        model.setHeaderData(0, Qt.Horizontal, "Тип")
        model.setHeaderData(1, Qt.Horizontal, "Наименование")
        model.setHeaderData(2, Qt.Horizontal, "Минимальное количество")
        model.setHeaderData(3, Qt.Horizontal, "Остаток")
        model.setHeaderData(4, Qt.Horizontal, "Поставщики")
        self.setSelectionBehavior(self.SelectRows)
        self.setSelectionMode(self.SingleSelection)
        vh = self.verticalHeader()
        vh.setSectionResizeMode(vh.Fixed)
        hh = self.horizontalHeader()
        hh.setSectionResizeMode(hh.ResizeToContents)
        hh.setSectionResizeMode(4, hh.Stretch)
