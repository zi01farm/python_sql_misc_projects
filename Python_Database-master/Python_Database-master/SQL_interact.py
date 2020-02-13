import pyodbc


class Region:
    """
    This creates a record object which can be used to insert into the Region table
    (Note: this can only be used for the region table in Northwind.)
    """
    def __init__(self, region_id, region_description):
        self.table_name = 'Region'
        self.RegionID = region_id
        self.RegionDescription = region_description


class Shippers:
    """
    This creates a record object which can be used to insert into the Shippers table
    (Note: this can only be used for the Shippers table in Northwind.)
    """
    def __init__(self, shipper_id, company_name, phone):
        self.table_name = 'Shippers'
        self.ShipperID = shipper_id
        self.CompanyName = company_name
        self.Phone = phone


class Connection:
    """
    This uses the pyodbc package to create a connector object to a specified SQL database
    """
    def __init__(self, server, database_name, user_name, password):
        self.server = server
        self.database_name = database_name
        self.user_name = user_name
        self.password = password

    def make_connection(self):
        docker_northwind = pyodbc.connect('DRIVER={ODBC DRIVER 17 for SQL SERVER};'
                                          'SERVER='+self.server+';'
                                          'DATABASE='+self.database_name+';'
                                          'UID='+self.user_name+';'
                                          'PWD='+self.password)
        cursor = docker_northwind.cursor()
        return cursor


class ReadOperation:
    """
    This CRUD operation will read out the contents of a table or specified columns
    """
    def __init__(self, table, select_string='*'):
        self.select_string = select_string
        self.table = table

    def do_it(self, connector):
        sql_select = "SELECT {} FROM {}".format(self.select_string, self.table)
        connector.execute(sql_select)
        for row in connector:
            print(row)


class InsertOperation:
    """
    this CRUD operation will insert a record object into the corresponding table
    (Note: object attribute table_name must match table being inserted into)
    """
    def __init__(self, record):
        for key, value in record.__dict__.items():
            setattr(self, key, value)

    def do_it(self, connector):
        column_string = ""
        columns = iter(self.__dict__.keys())
        next(columns, None)
        for key in columns:
            column_string += key+','
        if column_string.endswith(','):
            column_string = column_string[:-1]
        value_string = ""
        values = iter(self.__dict__.values())
        next(values, None)
        for value in values:
            value_string += value+','
        if value_string.endswith(','):
            value_string = value_string[:-1]
        try:
            sql_add = "SET IDENTITY_INSERT " + self.table_name + " ON " \
                      "INSERT INTO " + self.table_name + "(" + column_string + ") VALUES(" + value_string + ")" \
                      " SET IDENTITY_INSERT " + self.table_name + " OFF "
            connector.execute(sql_add)
            connector.commit()
        except:
            sql_add = "INSERT INTO " + self.table_name + "(" + column_string + ") VALUES(" + value_string + ")"
            connector.execute(sql_add)
            connector.commit()


class DeleteOperation:
    """
    this CRUD operation deletes a record from a table witha condition to denote which record to be deleted
    I.e. 'ID = 8' will delete the record with the ID of 8
    """
    def __init__(self, table_name, condition):
        self.table_name = table_name
        self.condition = condition

    def do_it(self, connector):
        sql_delete = "DELETE FROM {} WHERE {}".format(self.table_name, self.condition)
        connector.execute(sql_delete)
        connector.commit()


class UpdateOperation:
    """
    this CRUD operation will update a record in a table given a table name, a value to update,
    and a condition to specify the location of the record
    """
    def __init__(self, table_name, column_update, condition):
        self.table_name = table_name
        self.column_update = column_update
        self.condition = condition

    def do_it(self, connector):
        sql_update = "UPDATE {} SET {} WHERE {}".format(self.table_name, self.column_update, self.condition)
        connector.execute(sql_update)
        connector.commit()


class ProgramMain:
    """
    this program allows users to connect to a database and perform CRUD operations on specified tables
    """
    def __init__(self):
        self.connector = ""

    def connection(self, server, database_name, user_name, password):
        connector = Connection(server, database_name, user_name, password).make_connection()
        self.connector = connector

    def insert(self, record_object):
        insert_object = InsertOperation(record_object)
        insert_object.do_it(self.connector)

    def read(self, table_name, select_string):
        read_object = ReadOperation(table_name, select_string)
        read_object.do_it(self.connector)

    def delete(self, table_name, condition):
        delete_object = DeleteOperation(table_name, condition)
        delete_object.do_it(self.connector)

    def update(self, table_name, column_name, condition):
        update_object = UpdateOperation(table_name, column_name, condition)
        update_object.do_it(self.connector)


# region_row = Region("'5'","'Outback'")
# ship_row = Shippers("'4'","'Big Ships'","'999'")
# main_program = ProgramMain()
# main_program.connection('localhost,1433','Northwind','sa','Passw0rd2018')
# main_program.read("Shippers","*")
# main_program.update("Region","RegionDescription = 'Far away","RegionID = 4")
# main_program.insert(ship_row)
# main_program.delete("Shippers","ShipperID = 4")
