import sys

def parse_file(file_name):
    parsed_data = {}
    with open(file_name, 'r') as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            splitted = line.split(",")
            if len(splitted) == 2 and splitted[0] != 'cookie':
                cookie = splitted[0]
                date = splitted[1][:10]

                if date in parsed_data:
                    cookieCounts = parsed_data[date]
                    if cookie in cookieCounts:
                        cookieCounts[cookie] += 1
                    else:
                        cookieCounts[cookie] = 1
                else:
                    parsed_data[date] = {}
                    parsed_data[date][cookie] = 1
    
    return parsed_data


def most_active_cookie(cookieCountsByDate, date):
    output = []
    if date in cookieCountsByDate:
        cookieCounts = cookieCountsByDate[date]
        most_active = max(cookieCounts.values())

        for cookie, freq in cookieCounts.items():
            if freq == most_active:
                output.append(cookie)
    return output


def main():
    n = len(sys.argv)
    if n != 4:
        print("The number of arguments is incorrect.")
        return
    
    cookieLogFile = sys.argv[1]
    date = sys.argv[3]

    cookieCountsByDate = parse_file(cookieLogFile)
    result = most_active_cookie(cookieCountsByDate, date)
    for ele in result:
        print(ele)


if __name__=="__main__":
    main()
