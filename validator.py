from helpers import set_name, set_description, set_price, set_quantity
def valid(data):
    try:
        data.keys()
        if "username" in data.keys() and "password" in data.keys() and "email" in data.keys() and "role" in data.keys():
            if type(data["username"]) == str and type(data["password"]) == str and type(data["email"]) == str and type(data["role"]) ==  int and 3<=len(data["username"])<=20 and 5<=len(data["password"])<=25 and 5<=len(data["email"])<=35 and (data["role"] != 0 or data["role"] != 1) :
                if "course" in data.keys():
                    if "name" in data.keys() and "price" in data.keys() :
                        if set_name()
                    else:
                        return False
                
                return True
            else:
                return False

        else:
            return False
    except:
        return False