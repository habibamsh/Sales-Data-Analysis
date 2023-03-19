#Name: Ahmad Alhabib
#Description: This program reads files of sales IDs and sales data, it collects, organizes, and displays the sales by quarter and by the ID that made the sale.
#It also displays the quarter in which the highest sales were made, and the ID with the highest sales in total.

#This function opens and reads the salesperson's IDs file and create a list of the IDs and a list that is a two dimensional list of the sales data by quarter for each salesperson
def getIDs(filename):
    file_open = open(filename,'r')
    file_data = file_open.read().split()
    file_open.close()
    file_data.sort()
    sales_data= []

    for ID in file_data:
        sales_data.append([0.0,0.0,0.0,0.0])
    
    return file_data,sales_data
#This function reads the sales data file and add all the sales data to the sales_data list totaling all the monthly data into the totals for the proper quarter by sales ID
def process_sales_data(filename,id_list,salesData):
    file_open = open(filename,'r')
    
    for line in file_open:
        sale_amount = line.split()
        index_num = id_list.index(sale_amount[0])
        quarter = int((int(sale_amount[1])-1)/3)
        salesData[index_num][quarter] += float(sale_amount[2])
    file_open.close()
#This function produces the printed Annual Sales Report from the data supplied in the id_list and sales_data lists
#and calculate the totals by quarter and determine the maximum sales by a sales person in a quarter and maximum sales by quarter
def print_report(id_list,salesData):
    sales_id = []
    sales_quarter = [0.0,0.0,0.0,0.0]
    
    for sale_by_ID in salesData:
        sales_id.append(sum(sale_by_ID))
        sales_quarter[0] += sale_by_ID[0]
        sales_quarter[1] += sale_by_ID[1]
        sales_quarter[2] += sale_by_ID[2]
        sales_quarter[3] += sale_by_ID[3]
        
    print('\n\n-------Annual Sales Report-------')
    print('\nID\t\tQT1\t\tQT2\t\tQT3\t\tQT4\t\tTotal')
    
    for index in range(len(id_list)):
        print('%s\t\t%.2f\t\t%.2f\t\t%.2f\t\t%.2f\t\t%.2f'%(id_list[index],salesData[index][0],salesData[index][1],salesData[index][2],salesData[index][3],sales_id[index]))
    
    total = sum(sales_quarter)        
    print('Total\t\t%.2f\t\t%.2f\t\t%.2f\t\t%.2f\t\t%.2f'%(sales_quarter[0],sales_quarter[1],sales_quarter[2],sales_quarter[3],total))
    max_sales_by_id = 0.0
    max_sales_id = 0

    for ID in salesData:
        for sale in ID:
            if sale > max_sales_by_id:
                max_sales_by_id = sale
                max_sales_id = salesData.index(ID)
    
    max_sales_of_quarter = max(sales_quarter)
    max_sales_quarter = sales_quarter.index(max_sales_of_quarter)+1
    print('\nMax sales by Salesperson: ID = %s, Amount = $%.2f'%(id_list[max_sales_id],max_sales_by_id))
    print('Max sales by Quarter: Quarter = %d, Amount = $%.2f'%(max_sales_quarter,max_sales_of_quarter))
    print('\n-------End of Sales Report-------')
#This function asks the user for the name of each of the input files and then call the other functions
def main():
    id_list_file = input('Enter the name of the sales ids file: ')
    id_list,salesData = getIDs(id_list_file)
    sales_data_file = input('Enter the name of sales data file: ')
    process_sales_data(sales_data_file,id_list,salesData)
    print_report(id_list,salesData)

Initiate_program = main()
