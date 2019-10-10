set_to_true = True
set_to_false = False

bool_one = 5 != 7
bool_two = 1 + 1 != 2
bool_three = 3 * 3 == 9

def bring_umbrella():
    print("Sacar sombrilla")

# if is_raining:
    # bring_umbrella()

def age_check(age):
    if age > 13:
        return True


# if weekday:
#     wake_up("6:30")
#     ####
#     ####
#     ####
# else:
#     ####
#     ###
#     ###
#     sleep_in()

def thank_you(donation):
    if donation > 1000:
        print("Gracias la mejor donacion")
    elif donation >= 500:
        print("Gracias muy buena donacion")
    elif donation >= 100:
        print("Gracias buena donacion")
    else:
        print("Gracias!")


def divides(a, b):
    try:
        # some statement
        result = a / b
        print(result)
    except ZeroDivisionError:
        ## some statemen
        print("No podemos dividir por cero")
    except ValueError:
        print("Ingrese un valor correcto")
    except SintaxError:
        print("escriba correctamente la sentencia")
    # except Exception as e:
    #     logging.error(traceback.format_exc())


divides(10, 0)

def in_range(num, lower, upper):
  if num >= lower and num <= upper:
    return True
  else:
    return False

print(in_range(5, 10, 20))
