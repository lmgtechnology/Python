def process ():
    import argparse, locale, os
    from datetime import datetime, timezone
    from time import strftime
    # locale.setlocale(locale.LC_ALL, '')
    date_format = "%Y%m%d.%H%M%S"
    dt = (datetime.now(timezone.utc).strftime(date_format))
    parser = argparse.ArgumentParser()
    program_file = os.path.basename(__file__)
    debug = 1

    version = "1.0"
    parser.add_argument('hourly_wage', metavar='Hourly_Wage', type=float, help='Hourly wage in US dollars')
    parser.add_argument('hours_worked', metavar='Hours_Worked', type=float, help='Hours worked in pay period')
    parser.add_argument('-v', '--version', action='version', version=(program_file + " Version " + version))

    args = parser.parse_args()

    hourly_wage = args.hourly_wage
    hours_worked = args.hours_worked
    amount = args.hourly_wage
    x = dollar_format(hourly_wage, hours_worked)

    if (debug):
        # print ("Tithe = " + tithe)
        # print ("Check = " + x)
        # print (tithe_dollar)

        print(args)
        print(args.hourly_wage)
        print(args.hours_worked)
        print ("date format = " + date_format)
        print ('dt = ' + dt)

def dollar_format(hourly_wage, hours_worked):
    # check_dollars = (locale.currency(args.hourly_wage, grouping=True))
    import locale
    from pprint import pprint
    locale.setlocale(locale.LC_ALL, '')
    from library_custom import right_justify # Custom library
    fica = 0.0765
    futa_rate = 0.06
    annual_salary = (hourly_wage * 40 * 52)
    formatted_annual_salary = "${:,.2f}".format(annual_salary)
    if (annual_salary > 7000):
        futa_amount = futa_rate * 7000
        formatted_futa_amount = "${:,.2f}".format(futa_amount)
        futa_applied = 1
    else:
        futa_applied = 0
    gross_check = (hourly_wage * hours_worked)
    formatted_gross_check = "${:,.2f}".format(gross_check)
    tithe = (hourly_wage * hours_worked * .10)
    check_dollars = (locale.currency(hourly_wage, grouping=True))
    # hourly_wage = (hourly_wage)
    line_length = 80
    var_length = len(formatted_hourly_wage)
    padding = right_justify(var_length, line_length)
    formatted_hourly_wage = "${:,.2f}".format(hourly_wage)
    formatted_tithe = "${:,.2f}".format(tithe)
    formatted_hours_worked = "{:,.1f}".format(hours_worked)
    formatted_fica_amount = "{:,.2f}".format(gross_check * fica)
    net_check = (gross_check - (gross_check * fica))
    print(f'Hourly Wage : "{formatted_hourly_wage:_>60}"')
    print(f'Hours Worked : "{hours_worked:_>60}"')
    print(f'Annual Salary : "{formatted_annual_salary:_>60}"')
    # print(f'fica_amount = {fica_amount} net_check = {net_check}\n')
    print(f'FICA Tax ==> {formatted_fica_amount:_>60}')
    if (futa_applied):
        print(f'FUTA Tax ==> {formatted_futa_amount:_>60}')
    print(f'tithe: {tithe:_>60}\n')
    return(check_dollars)

    # tithe = args.hourly_wage * .10
    # tithe_dollar = dollar_format(tithe)
    ################################### End initialize ()

def main():
    process()
    # get_args()

if __name__ == "__main__":
    main()