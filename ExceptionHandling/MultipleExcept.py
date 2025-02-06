def disp(a,b):
    try:
        print(a/b)
    except ZeroDivisionError:
        print('ZeroDivisionError Occurred and Handled')
    except NameError:
        print('Name error occurred and Handled')
    except TypeError:
        print('Type Error Occurred and Handled')
    except:
        print('Some error occurred and Handled')
disp(10,0)

