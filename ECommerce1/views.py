import pyodbc
from django.shortcuts import render
import requests                                 # To use request package in current program

from ECommerce1.models import search
from ECommerce1.models import keys

# This section is for All Publications
def connsql(request):
    conn = pyodbc.connect(r'Driver={sql server};'
                        r'Server=DESKTOP-BMVVDK6\SQLEXPRESS;'
                        r'Database=Example;'
                        r'Trusted_Connection=yes;')
    cursor = conn.cursor()
    # populate auto list
    cursor.execute("select distinct keyword from search")
    result = cursor.fetchall()
    if request.method =="POST":
        keywords=request.POST.get('keyword')
        cursor2 = conn.cursor()

        cursor2.execute("select * from search where keyword= ?", keywords)
        result2 = cursor2.fetchall()

        return render(request,'Index.html',{'keys':result,'search':result2})
    else:

        cursor3=conn.cursor()
        cursor3.execute("select * from search")
        result3 = cursor3.fetchall()
        return render(request,'Index.html',{'keys':result,'search':result3})


# This Section is for the Open road media selection.
def connsql_ORM(request):
    conn = pyodbc.connect(r'Driver={sql server};'
                        r'Server=DESKTOP-BMVVDK6\SQLEXPRESS;'
                        r'Database=Example;'
                        r'Trusted_Connection=yes;')
    cursor4 = conn.cursor()
    # populate auto list
    cursor4.execute("select distinct keyword from search where asin IN ('B008F4NSXO','B008UX8YPC','B00EBO23WO', 'B00U7Y5TI2', 'B01N49MWZH', 'B06XRSTBMN')")
    result = cursor4.fetchall()
    if request.method =="POST":
        keywords=request.POST.get('keyword')
        cursor5 = conn.cursor()

        cursor5.execute("select * from search where asin IN('B008F4NSXO','B008UX8YPC','B00EBO23WO', 'B00U7Y5TI2', 'B01N49MWZH', 'B06XRSTBMN') and keyword= ?", keywords)
        result2 = cursor5.fetchall()

        return render(request,'ORM.html',{'keys':result,'search':result2})
    else:

        cursor6=conn.cursor()
        cursor6.execute("select * from search where asin IN('B008F4NSXO','B008UX8YPC','B00EBO23WO', 'B00U7Y5TI2', 'B01N49MWZH', 'B06XRSTBMN')")
        result3 = cursor6.fetchall()

        return render(request,'ORM.html',{'keys':result,'search':result3})


#This section is for popularity

def connsql_POP(request):
    conn = pyodbc.connect(r'Driver={sql server};'
                        r'Server=DESKTOP-BMVVDK6\SQLEXPRESS;'
                        r'Database=Example;'
                        r'Trusted_Connection=yes;')

    cursor7 = conn.cursor()
    cursor7.execute("select Cast(sales_rank as int),publication_date,page,title,author from search WHERE ISNUMERIC(sales_rank) = 1 Order by sales_rank DESC ")
    result4 = cursor7.fetchall()
    return render(request, 'Popular.html', { 'search': result4})