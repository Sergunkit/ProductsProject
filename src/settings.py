db_params = {
  'host' : 'localhost',
  'port' : 5432,
  'user' : 'newuser',
  'dbname' : 'products',
  'password': '12345678'
}


# cd $QTDIR/qtbase/src/plugins/sqldrivers
# mkdir qpsql
# cd qpsql
# qmake "INCLUDEPATH+=/opt/homebrew/Cellar/qt/qpsql/include" "LIBS+=-L/opt/homebrew/Cellar/postgresql/qpsql/lib -lpq" qpsql.pro
# make
# make install
