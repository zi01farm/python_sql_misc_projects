import pyodbc
import json

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


class Categories:
    def __init__(self, category_id, category_name, description, picture):
        self.table_name = 'Categories'
        self.CategoryID = category_id
        self.CategoryName = category_name
        self.Description = description
        self.Picture = picture


class CustomerDemographics:
    def __init__(self, customer_type_id, customer_desc):
        self.table_name = 'CustomerDemographics'
        self.CustomerTypeID = customer_type_id
        self.CustomerDesc = customer_desc


class Customers:
    def __init__(self, customer_id, company_name, contact_name, contact_title,
                 address, city, region, postal_code, country, phone, fax):
        self.table_name = 'Customers'
        self.CustomerID = customer_id
        self.CompanyName = company_name
        self.ContactName = contact_name
        self.ContactTitle = contact_title
        self.Address = address
        self.City = city
        self.Region = region
        self.PostalCode = postal_code
        self.Country = country
        self.Phone = phone
        self.Fax = fax


class Suppliers:
    def __init__(self, supplier_id, company_name, contact_name, contact_title,
                 address, city, region, postal_code, country, phone, fax,
                 home_page):
        self.table_name = 'Suppliers'
        self.SupplierID = supplier_id
        self.CompanyName = company_name
        self.ContactName = contact_name
        self.ContactTitle = contact_title
        self.Address = address
        self.City = city
        self.Region = region
        self.PostalCode = postal_code
        self.Country = country
        self.Phone = phone
        self.Fax = fax
        self.HomePage = home_page


class RowCreator:
    def __init__(self):
        self.new_records_list = []

    def create_row(self):
            choice = input('What table to you want to create a row into? ')
            if choice == 'Region':
                region_id = "'" + input('RegionID: ') + "'"
                region_description = "'" + input('RegionDescription:  ') + "'"
                row_object = Region(region_id, region_description)
                self.new_records_list.append(row_object.__dict__)
                with open('rows_created.json','w') as json_file:
                    json.dump(self.new_records_list, json_file)
                return row_object
            elif choice == 'Shippers':
                shipper_id = "'" + input('ShipperID:  ') + "'"
                company_name = "'" + input('CompanyName:  ') + "'"
                phone = "'" + input('Phone:  ') + "'"
                row_object = Shippers(shipper_id, company_name, phone)
                self.new_records_list.append(row_object.__dict__)
                with open('rows_created.json','w') as json_file:
                    json.dump(self.new_records_list, json_file)
                return row_object




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
        except pyodbc.ProgrammingError:
            sql_add =  "INSERT INTO " + self.table_name + "(" + column_string + ") VALUES(" + value_string + ")"
            connector.execute(sql_add)
            connector.commit()
        except:
            print('there has been a major error')


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
        self.table_name = ""

    def run(self):
        print('program start')
        self.connection()
        self.table_name = input('what table would you like to access?  ')
        if self.table_name.upper() == 'REGION':
            print('columns: RegionID, RegionDescription')
        elif self.table_name.upper() == 'SHIPPERS':
            print('columns: ShipperID, CompanyName, Phone')
        while True:
            choice = input('what operation would you like to perform? (CRUD or NO)  ')
            if choice.upper() == 'R':
                select_string = input('which columns would you like to access? (* as all)  ')
                self.read(self.table_name, select_string)
            elif choice.upper() == 'C':
                self.insert()
            elif choice.upper() == 'U':
                update_string = input('what would you like to change?  ')
                condition_string = input('where is the row located?  ')
                self.update(self.table_name, update_string, condition_string)
            elif choice.upper() == 'D':
                delete_string = input('where is the row that you want to delete located?  ')#
                self.delete(self.table_name, delete_string)
            elif choice.upper() == 'NO':
                break


    def connection(self):
        print('please input server details')
        server = input('server: ')
        database_name = input('database name: ')
        user_name = input('username:  ')
        password = input('password:  ')
        connector = Connection(server, database_name, user_name, password).make_connection()
        self.connector = connector

    def insert(self):
        row = RowCreator().create_row()
        insert_object = InsertOperation(row)
        insert_object.do_it(self.connector)

    def read(self, table_name, select_string='*'):
        read_object = ReadOperation(self.table_name, select_string)
        read_object.do_it(self.connector)

    def delete(self, table_name, condition):
        delete_object = DeleteOperation(table_name, condition)
        delete_object.do_it(self.connector)

    def update(self, table_name, column_name, condition):
        update_object = UpdateOperation(table_name, column_name, condition)
        update_object.do_it(self.connector)


# region_row = Region("'7'")
# # ship_row = Shippers("'5'","'Small Ships'","'998'")
# main_program = ProgramMain()
# main_program.connection('localhost,1433','Northwind','sa','Passw0rd2018')
#
# # main_program.update("Region","RegionDescription = 'Far away","RegionID = 4")
# main_program.insert(region_row)
# # main_program.delete("Region","RegionID = 6")
# main_program.read("Region","*")

new_rows = RowCreator()
new_rows.create_row()
new_rows.create_row()
