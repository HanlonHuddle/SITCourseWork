"""
Author Hanrun Li
SSW 810 assignment8
"""
import datetime

def problem1():
    """ main function """
    start_date_2000 = datetime.datetime.strptime("02/27/2000", "%m/%d/%Y")
    end_date_2000 = start_date_2000 + datetime.timedelta(days=3)
    print(end_date_2000)
    start_date_2017 = datetime.datetime.strptime("02/27/2017", "%m/%d/%Y")
    end_date_2017 = start_date_2017 + datetime.timedelta(days=3)
    print(end_date_2017)
    day1 = datetime.datetime.strptime("10/31/2017", "%m/%d/%Y")
    day2 = datetime.datetime.strptime("01/01/2017", "%m/%d/%Y")
    days = day1 - day2
    print(days)

def main():
    """main entrance for HW08"""
    problem1()
    return 0

if __name__ == "__main__":
    main()
